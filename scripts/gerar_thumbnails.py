# -*- coding: utf-8 -*-
"""
Gera thumbnails/capas automáticas para os posts do site.

Cada post é um "page bundle": <seção>/posts/AAAA-MM-DD-slug/index.qmd, com a
capa e os anexos na mesma pasta. Quem manda é a lista SECOES, mais abaixo;
hoje só uma seção entra, e o resto do site usa capa padrão fixa.

  • Organização e Apresentação de Dados (modo "relatorio")
      Abre o relatório HTML embutido no post (iframe de relatorios/...) e
      fotografa o elemento mais colorido (gráfico, mapa, figura).

  • Cursos e Eventos (modo "cartaz")
      Todo curso e evento tem cartaz de divulgação. Basta soltar o arquivo
      na pasta do post (cartaz.jpg, poster.png, ou qualquer imagem) que ele
      vira a capa. O cartaz costuma ser quadrado ou em pé, e o card é 16:9:
      recortar cortaria justamente o título e as datas, então o cartaz entra
      inteiro, centralizado, sobre um fundo feito dele mesmo (a própria
      imagem ampliada e desfocada). Não precisa de Chrome, só de Pillow.

O modo "pagina" continua implementado e disponível: ele abre a página já
renderizada em docs/, esconde navbar/rodapé e fotografa a melhor figura do
corpo ou, na falta dela, o topo do texto. Nenhuma seção usa esse modo hoje,
porque para posts curtos ele produzia o retrato do próprio texto. Para voltar
a usá-lo, basta acrescentar a seção em SECOES.

O recorte é 16:9 (1200×675), salvo como thumbnail.png na pasta do próprio
post, e o `image:` é preenchido no front matter automaticamente.

Posts sem capa própria e fora de SECOES ficam com a capa padrão da seção,
declarada como `image-placeholder:` no cabeçalho de cada listagem.

Uso:
    python scripts/gerar_thumbnails.py                  # todos os posts sem capa
    python scripts/gerar_thumbnails.py --force          # regenera tudo
    python scripts/gerar_thumbnails.py vigitel-2019-2023 2026-06-22-populacao-e-pib

Automático: este script está registrado como `pre-render` no _quarto.yml, e
a cada `quarto render` (completo) ele roda sozinho e gera a capa de qualquer
post que ainda não tenha `image:`. Nesse modo ele nunca aborta o render do
site: se algo der errado, apenas avisa e o post fica para a próxima.

Requisitos: Google Chrome instalado + `pip install selenium pillow`.
"""

from __future__ import annotations

import argparse
import io
import math
import os
import re
import subprocess
import sys
import time
from pathlib import Path

# Pillow e selenium são checados em separado: o modo "cartaz" só precisa do
# Pillow, e seria bobagem deixar de gerar a capa de um evento porque a máquina
# não tem Chrome/selenium para os modos que fotografam página.
try:
    from PIL import Image, ImageChops, ImageFilter, ImageStat
    PIL_OK, ERRO_PIL = True, ""
except ImportError as _e:
    PIL_OK, ERRO_PIL = False, str(_e)

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    SELENIUM_OK, ERRO_SELENIUM = True, ""
except ImportError as _e:          # sem selenium o site ainda renderiza
    SELENIUM_OK, ERRO_SELENIUM = False, str(_e)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = Path(__file__).resolve().parents[1]
# Pasta de saída: o Quarto informa a dele; fora do render, vale o output-dir.
SITE = Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR") or (RAIZ / "docs"))
if not SITE.is_absolute():
    SITE = RAIZ / SITE

# Seções do site que ganham capa automática (os posts ficam em <pasta>/posts/)
#
# Análises: a capa sai de um gráfico de verdade, feito pelo estudante, e vale
# mais que qualquer desenho genérico. Cursos e Eventos: a capa é o cartaz de
# divulgação do próprio evento, que sempre existe.
#
# Oportunidades continua fora: edital não tem cartaz nem gráfico, e o "melhor
# visual" acabava sendo o retrato do próprio texto da página, com o título
# repetido dentro da imagem e meio quadro em branco. Segue com a capa padrão
# azul (images/capa-padrao-azul.svg), declarada como image-placeholder na
# listagem.
SECOES = [
    {"pasta": "O_que_fazemos/ensino/organizacao-e-apresentacao-de-dados", "modo": "relatorio"},
    {"pasta": "eventos", "modo": "cartaz"},
]

LARGURA_THUMB, ALTURA_THUMB = 1200, 675          # 16:9, mesmo dos cards
TAM_MINIMO = (300, 160)                          # menor elemento aceitável (px)
NOTA_MINIMA = 4.0                                # colorfulness mínima p/ valer
ESPERA_RENDER = 5                                # segundos p/ plotly/leaflet etc.

# Modo "cartaz": arquivos que o script reconhece como cartaz do evento, e os
# nomes que têm preferência quando a pasta tem mais de uma imagem.
EXT_CARTAZ = (".jpg", ".jpeg", ".png", ".webp")
NOMES_CARTAZ = ("cartaz", "poster", "capa", "banner", "arte", "flyer")

# Elementos que costumam carregar os visuais de um documento Quarto
SELETORES_VISUAIS = [
    ".cell-output-display", ".quarto-figure", "figure",
    ".js-plotly-plot", ".plotly", ".leaflet-container",
    "img", "svg", "canvas",
]


def renderiza_pagina_nova(post: Path) -> bool:
    """Renderiza só o post recém-criado, para a 'foto da página' ter de onde
    sair no primeiro render. Renders parciais não disparam os scripts de
    projeto do Quarto, então não há recursão, e CS_THUMBS_NESTED é o cinto
    de segurança caso esse comportamento mude."""
    rel = post.relative_to(RAIZ).as_posix()
    env = dict(os.environ, CS_THUMBS_NESTED="1")
    try:
        r = subprocess.run(f'quarto render "{rel}"',
                           cwd=str(RAIZ), env=env, shell=True,
                           capture_output=True, timeout=600)
        return r.returncode == 0
    except Exception:
        return False


def acha_relatorio(texto_qmd: str, bundle: Path) -> Path | None:
    """Descobre qual HTML de relatorios/ o post embute (dentro do bundle)."""
    m = re.search(r'iframe\s+src="(relatorios/[^"]+\.html)"', texto_qmd)
    if m:
        candidato = bundle / m.group(1)
        return candidato if candidato.exists() else None
    candidato = bundle / "relatorios" / "relatorio.html"
    return candidato if candidato.exists() else None


def acha_cartaz(bundle: Path) -> Path | None:
    """Descobre o cartaz do evento dentro da pasta do post.

    Vale qualquer imagem solta na pasta - o thumbnail.png gerado por este
    script fica de fora, senão a capa da execução anterior viraria a fonte
    da próxima. Nomes conhecidos (cartaz, poster, capa...) passam na frente;
    havendo empate, a maior imagem vence, que é a arte em tamanho cheio.
    """
    imagens = [p for p in sorted(bundle.iterdir())
               if p.is_file()
               and p.suffix.lower() in EXT_CARTAZ
               and p.stem.lower() != "thumbnail"]
    if not imagens:
        return None
    preferidos = [p for p in imagens
                  if any(n in p.stem.lower() for n in NOMES_CARTAZ)]
    return max(preferidos or imagens, key=lambda p: p.stat().st_size)


def capa_cartaz(cartaz: Path) -> Image.Image | None:
    """Modo 'cartaz': o cartaz inteiro, centralizado, sobre fundo dele mesmo.

    Cartaz de evento é quadrado ou em pé e carrega o texto que interessa
    (nome, datas, inscrições) espalhado por toda a arte: recortar em 16:9
    cortaria justamente isso. Então a arte entra inteira ("contain") e a
    sobra dos lados é preenchida com a própria imagem ampliada e desfocada -
    o mesmo recurso de player de vídeo, que combina cores com qualquer
    cartaz sem precisar escolher uma cor à mão.
    """
    try:
        with Image.open(cartaz) as arq:
            im = arq.convert("RGB")
            im.load()
    except Exception as e:
        print(f"[!!] não abri o cartaz {cartaz.name}: {e}")
        return None

    # Fundo: a própria arte cobrindo o quadro inteiro, desfocada e suavizada
    fundo = recorta_16x9(im.copy())
    fundo = fundo.filter(ImageFilter.GaussianBlur(radius=28))
    fundo = Image.blend(fundo, Image.new("RGB", fundo.size, (255, 255, 255)), 0.28)

    # Frente: a arte inteira, o mais alta possível dentro do quadro
    frente = im.copy()
    frente.thumbnail((LARGURA_THUMB, ALTURA_THUMB), Image.LANCZOS)
    fundo.paste(frente, ((LARGURA_THUMB - frente.width) // 2,
                         (ALTURA_THUMB - frente.height) // 2))
    return fundo


def colorido(im: Image.Image) -> float:
    """Métrica de colorfulness de Hasler–Süsstrunk (sem numpy)."""
    im = im.convert("RGB")
    im.thumbnail((320, 320))
    r, g, b = im.split()
    rg = ImageChops.difference(r, g)                    # |R - G|
    meio = ImageChops.add(r, g, scale=2.0)              # (R + G) / 2
    yb = ImageChops.difference(meio, b)                 # |(R+G)/2 - B|
    s_rg, s_yb = ImageStat.Stat(rg), ImageStat.Stat(yb)
    desvio = math.hypot(s_rg.stddev[0], s_yb.stddev[0])
    media = math.hypot(s_rg.mean[0], s_yb.mean[0])
    return desvio + 0.3 * media


def recorta_16x9(im: Image.Image, do_topo: bool = False) -> Image.Image:
    """Recorte 16:9 + redimensiona para o tamanho da thumbnail."""
    im = im.convert("RGB")
    w, h = im.size
    alvo = LARGURA_THUMB / ALTURA_THUMB
    if w / h > alvo:                                    # largo demais: corta lados
        novo_w = int(h * alvo)
        x = (w - novo_w) // 2
        im = im.crop((x, 0, x + novo_w, h))
    else:                                               # alto demais: fica com o topo
        novo_h = int(w / alvo)
        y = 0 if do_topo else max(0, (h - novo_h) // 3)  # viés p/ cima: títulos
        im = im.crop((0, y, w, y + novo_h))
    return im.resize((LARGURA_THUMB, ALTURA_THUMB), Image.LANCZOS)


def abre_chrome() -> webdriver.Chrome:
    op = Options()
    op.add_argument("--headless=new")
    op.add_argument("--window-size=1440,1000")
    op.add_argument("--force-device-scale-factor=1")
    op.add_argument("--hide-scrollbars")
    op.add_argument("--disable-gpu")
    op.add_argument("--allow-file-access-from-files")
    driver = webdriver.Chrome(options=op)
    driver.set_page_load_timeout(180)
    return driver


def candidatos_visuais(driver, escopo: str) -> list:
    """Elementos visíveis e grandes o bastante, sem duplicar retângulos."""
    seletor = ", ".join(f"{escopo} {s}".strip() for s in SELETORES_VISUAIS)
    els = driver.execute_script(
        """
        const vistos = new Set();
        const saida = [];
        for (const el of document.querySelectorAll(arguments[0])) {
          const r = el.getBoundingClientRect();
          if (r.width < arguments[1] || r.height < arguments[2]) continue;
          const st = getComputedStyle(el);
          if (st.visibility === 'hidden' || st.display === 'none') continue;
          const chave = [Math.round(r.width/8), Math.round(r.height/8),
                         Math.round((r.top + window.scrollY)/8)].join('|');
          if (vistos.has(chave)) continue;   // mesmo retângulo já coletado
          vistos.add(chave);
          saida.push(el);
        }
        return saida.slice(0, 40);
        """,
        seletor, TAM_MINIMO[0], TAM_MINIMO[1],
    )
    return els or []


def espera_carregar(driver) -> None:
    for _ in range(60):
        if driver.execute_script("return document.readyState") == "complete":
            break
        time.sleep(0.5)
    time.sleep(ESPERA_RENDER)                            # plotly/leaflet/fontes


def melhor_elemento(driver, escopo: str) -> Image.Image | None:
    """Fotografa os candidatos e devolve o mais colorido (ou None)."""
    melhor, melhor_nota = None, 0.0
    for el in candidatos_visuais(driver, escopo):
        try:
            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", el)
            time.sleep(0.15)
            png = el.screenshot_as_png
        except Exception:
            continue
        im = Image.open(io.BytesIO(png))
        if im.width < TAM_MINIMO[0] or im.height < TAM_MINIMO[1]:
            continue
        nota = colorido(im)
        if nota > melhor_nota:
            melhor, melhor_nota = im, nota
    if melhor is None or melhor_nota < NOTA_MINIMA:
        return None
    return melhor


def capa_relatorio(driver, relatorio: Path) -> Image.Image | None:
    """Modo 'relatorio': elemento mais colorido do relatório embutido."""
    driver.get(relatorio.resolve().as_uri())
    espera_carregar(driver)
    return melhor_elemento(driver, escopo="")


def capa_pagina(driver, pagina: Path) -> Image.Image | None:
    """Modo 'pagina': figura colorida do corpo ou foto do topo da página."""
    driver.get(pagina.resolve().as_uri())
    espera_carregar(driver)
    # Esconde a moldura do site: a capa é a página, não o navbar/rodapé
    driver.execute_script("""
        for (const sel of ['.navbar', '.nav-footer', '#quarto-back-to-top',
                           '.quarto-title-tools', '#quarto-header']) {
          document.querySelectorAll(sel).forEach(el => el.style.display = 'none');
        }
        window.scrollTo(0, 0);
    """)
    time.sleep(0.3)

    im = melhor_elemento(driver, escopo="main")
    if im is not None:
        return im

    # Sem figura colorida: "foto da página", com título + primeiras linhas.
    # Viewport no tamanho exato da capa (16:9) para o texto preencher o quadro;
    # via CDP para não sofrer com o scaling de DPI do Windows.
    driver.execute_cdp_cmd("Emulation.setDeviceMetricsOverride", {
        "width": LARGURA_THUMB, "height": ALTURA_THUMB,
        "deviceScaleFactor": 1, "mobile": False,
    })
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(0.4)
    foto = Image.open(io.BytesIO(driver.get_screenshot_as_png()))
    driver.execute_cdp_cmd("Emulation.clearDeviceMetricsOverride", {})
    return recorta_16x9(foto, do_topo=True)


def insere_image_no_front_matter(arquivo: Path, caminho_thumb: str) -> None:
    texto = arquivo.read_text(encoding="utf-8")
    if re.search(r"(?m)^image:", texto):
        texto = re.sub(r'(?m)^image:.*$', f'image: "{caminho_thumb}"', texto, count=1)
    elif re.search(r"(?m)^date:.*$", texto):
        texto = re.sub(
            r"(?m)^(date:.*)$",
            lambda m: f'{m.group(1)}\nimage: "{caminho_thumb}"',
            texto, count=1,
        )
    else:
        # sem date: insere antes do --- que fecha o front matter
        linhas = texto.split("\n")
        for i in range(1, len(linhas)):
            if linhas[i].strip() == "---":
                linhas.insert(i, f'image: "{caminho_thumb}"')
                break
        texto = "\n".join(linhas)
    arquivo.write_text(texto, encoding="utf-8", newline="\n")


def main() -> int:
    # Disparado por um render aninhado deste próprio script? Sai em silêncio.
    if os.environ.get("CS_THUMBS_NESTED"):
        return 0

    # Rodando como pre-render do Quarto (env presente) => modo automático:
    # nunca aborta o render do site, apenas avisa.
    modo_auto = bool(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR"))

    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("slugs", nargs="*", help="posts específicos (sem .qmd)")
    ap.add_argument("--force", action="store_true",
                    help="regenera mesmo quem já tem image:")
    args = ap.parse_args([] if modo_auto else None)

    if not PIL_OK:
        print(f"[!!] capas automáticas indisponíveis ({ERRO_PIL}). "
              f"Instale com: pip install pillow")
        return 0 if modo_auto else 1
    if not SELENIUM_OK:
        print(f"[--] sem selenium ({ERRO_SELENIUM}): só as capas de cartaz "
              f"serão geradas. Instale com: pip install selenium")

    if modo_auto:
        print("[Capas automáticas] verificando posts sem thumbnail")

    try:
        return gera_capas(args, modo_auto)
    except Exception as e:
        if modo_auto:
            print(f"[!!] gerador de capas falhou ({e}), e o render do site segue")
            return 0
        raise


def gera_capas(args, modo_auto: bool) -> int:
    driver = None
    gerados, pulados = 0, 0

    for secao in SECOES:
        # Um post = uma pasta: <seção>/posts/AAAA-MM-DD-slug/index.qmd
        posts = sorted((RAIZ / secao["pasta"] / "posts").glob("*/index.qmd"))
        if args.slugs:
            posts = [p for p in posts
                     if p.parent.name in args.slugs
                     or any(p.parent.name.endswith(f"-{s}") for s in args.slugs)]
        if not posts:
            continue

        for post in posts:
            bundle = post.parent
            nome = bundle.name                      # AAAA-MM-DD-slug
            texto = post.read_text(encoding="utf-8")
            if not args.force and re.search(r"(?m)^image:", texto):
                if not modo_auto:
                    print(f"[ok] {nome}: já tem capa (image: no front matter)")
                pulados += 1
                continue

            if secao["modo"] == "cartaz":
                origem = acha_cartaz(bundle)
                if origem is None:
                    if not modo_auto:
                        print(f"[--] {nome}: sem cartaz na pasta do post "
                              f"(cartaz.jpg, poster.png...); fica com a capa padrão")
                    continue
                print(f"[..] {nome}: montando a capa a partir de {origem.name}...")
                im = capa_cartaz(origem)
                if im is None:
                    continue
                destino = bundle / "thumbnail.png"
                im.save(destino, optimize=True)
                insere_image_no_front_matter(post, "thumbnail.png")
                print(f"[ok] {nome}: capa gerada em {destino.relative_to(RAIZ)}")
                gerados += 1
                continue

            if not SELENIUM_OK:
                continue

            if secao["modo"] == "relatorio":
                origem = acha_relatorio(texto, bundle)
                if origem is None:
                    print(f"[!!] {nome}: relatório HTML não encontrado em "
                          f"{bundle.name}/relatorios/. Envie uma thumbnail manualmente")
                    continue
            else:
                origem = SITE / secao["pasta"] / "posts" / nome / "index.html"
                if not origem.exists() and modo_auto:
                    # post novo, nunca renderizado: renderiza só ele para a capa
                    print(f"[..] {nome}: primeira renderização da página "
                          f"(para a foto da capa)...")
                    renderiza_pagina_nova(post)
                if not origem.exists():
                    print(f"[!!] {nome}: página não encontrada em "
                          f"{SITE.name}/. Rode `quarto render` antes deste script")
                    continue

            if driver is None:
                print("Abrindo o Chrome headless...")
                driver = abre_chrome()

            print(f"[..] {nome}: analisando {origem.name} ({secao['modo']})...")
            if secao["modo"] == "relatorio":
                im = capa_relatorio(driver, origem)
            else:
                im = capa_pagina(driver, origem)
            if im is None:
                print(f"[!!] {nome}: nenhum visual aproveitável. "
                      f"Envie uma thumbnail manualmente")
                continue

            destino = bundle / "thumbnail.png"
            recorta_16x9(im).save(destino, optimize=True)
            insere_image_no_front_matter(post, "thumbnail.png")
            print(f"[ok] {nome}: capa gerada em {destino.relative_to(RAIZ)}")
            gerados += 1

    if driver is not None:
        driver.quit()
    print(f"\nConcluído: {gerados} gerada(s), {pulados} já existiam.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
