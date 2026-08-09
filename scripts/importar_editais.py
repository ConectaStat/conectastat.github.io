# -*- coding: utf-8 -*-
"""Importa editais novos das fontes oficiais da UFLA para oportunidades/posts/.

Sao tres fontes, uma por area do site (ver FONTES, abaixo):

    Ensino     https://des.ufla.br/editais            (monitoria, docencia)
    Pesquisa   https://prpi.ufla.br/...editais        (PIVIC, PIBIC, PIBITI)
    Extensao   https://proeec.ufla.br/editais/...     (PIBEEC e afins)

O edital tem UM modelo so, o mesmo para as tres (_templates/areas/edital.qmd):
venha de onde vier, ele vira uma pasta de post igual as outras, e aparece na
pagina da area dele pelo mesmo card das demais. As paginas de area nao
descrevem a fonte em prosa - listam os editais, e ponto.

    oportunidades/posts/AAAA-MM-DD-slug/
    └── index.qmd

Cada edital importado recebe `categories: [Oportunidades, Editais]` mais a
area. A PRPI e a PROEEC ja dizem a area pela propria fonte (`areas` em
FONTES); no DES, que publica edital de tudo, a area sai do TITULO, pelas
palavras em AREA_PALAVRAS. Editais do DES que nao batem com nenhuma - concurso
para docente efetivo, professor substituto e afins - continuam aparecendo em
Oportunidades (a listagem geral), mas ficam de fora das paginas de
Ensino/Pesquisa/Extensao: o publico do site e formado por estudantes e
pos-graduandos, e esses editais nao sao uma oportunidade para eles na
maioria dos casos.

Ja os editais de vida interna do departamento - eleicao de chefe e subchefe,
chefia de gabinete, colegiado - nao entram nem na listagem geral: ver
EXCLUIR_PALAVRAS.

So entram editais publicados dentro de JANELA_DIAS: as tres paginas tem anos
de historico, e a maior parte ja venceu. Como a lista vem da mais recente
para a mais antiga, a busca para na primeira pagina em que todo mundo ja e
mais velho que a janela.

Cada post importado carrega, comentado no topo do arquivo, a fonte e o
identificador numerico do edital nela (`<!-- fonte: des-editais-<id> -->`,
`prpi-editais-<id>`, `proeec-editais-<id>`) - e so por ele que uma proxima
execucao reconhece "esse eu ja importei" e pula, sem precisar de nenhum banco
de dados a parte.

Uso:
    python scripts/importar_editais.py             # importa o que faltar
    python scripts/importar_editais.py --dry-run    # so mostra o que faria

Pensado para rodar como o job agendado de
.github/workflows/importar-editais.yml, mas funciona igual na sua maquina.
"""
from __future__ import annotations

import os
import re
import sys
import time
import unicodedata
import urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
DESTINO = RAIZ / "oportunidades" / "posts"
MODELO = RAIZ / "_templates" / "areas" / "edital.qmd"

JANELA_DIAS = 365
PAGINAS_NO_MAXIMO = 6          # trava de seguranca: 6 paginas = 60 editais

# As fontes oficiais, uma por area. Todas rodam Joomla, então a mesma
# extração serve para as três; muda o endereço, o padrão do link de cada
# edital e a área a que ele pertence.
#
#   lista   pagina que lista os editais
#   indice  (opcional) a lista está separada por ano, e esta é a página que
#           lista os anos - é o caso da PRPI. O importador entra nos anos
#           mais recentes e busca os editais lá dentro.
#   item    padrão do link de um edital dentro da página de listagem; o
#           primeiro grupo é o caminho, o segundo é o id na fonte
#   exige   (opcional) só entra se o título contiver esta palavra - as
#           páginas da PRPI e da PROEEC misturam avisos com os editais
#   areas   área fixa; None = deduz do título, por AREA_PALAVRAS (DES)
FONTES = [
    {
        "nome": "des",
        "base": "https://des.ufla.br",
        "lista": "https://des.ufla.br/editais",
        "item": r'<a[^>]+href="(/editais/(\d+)[^"]*)"[^>]*>(.*?)</a>',
        "areas": None,
        "autor": "Departamento de Estatística da UFLA",
    },
    {
        "nome": "prpi",
        "base": "https://prpi.ufla.br",
        "indice": "https://prpi.ufla.br/iniciacao-cientifica/editais",
        "item_indice": r'<a[^>]+href="(/iniciacao-cientifica/editais/(\d+)-[^"]*)"',
        "item": r'<a[^>]+href="(/noticias-prpi/(\d+)-[^"]*)"[^>]*>(.*?)</a>',
        "exige": "edital",
        "areas": ["Pesquisa"],
        "autor": "Pró-Reitoria de Pesquisa e Inovação (PRPI/UFLA)",
    },
    {
        "nome": "proeec",
        "base": "https://proeec.ufla.br",
        "lista": "https://proeec.ufla.br/editais/programa-institucional-de-bolsas-de-extensao",
        "item": r'<a[^>]+href="(/editais/[^"]*?/(\d+)-[^"]*)"[^>]*>(.*?)</a>',
        "exige": "edital",
        "areas": ["Extensão"],
        "autor": "Pró-Reitoria de Extensão, Esporte e Cultura (PROEEC/UFLA)",
    },
]

# Título do edital -> área(s) de Oportunidades por área do site (ver módulo
# acima). Só vale para o DES, que publica edital de tudo; PRPI e PROEEC já
# vêm com a área definida pela fonte. Um edital pode bater em mais de uma;
# quem não bate em nenhuma segue sem área (só na listagem geral).
#
# O nome da área é escrito exatamente como as páginas filtram (ver
# `template-params: categoria:` em O_que_fazemos/*/index.qmd): "Extensão"
# com acento, senão o card é importado e nunca aparece na página da área.
AREA_PALAVRAS = {
    "Ensino": ["monitor", "monitoria", "docencia voluntaria", "docente voluntario"],
    "Pesquisa": ["mestrado", "doutorado", "ppgee", "iniciacao cientifica",
                 "pos-doutorado", "bolsista de pesquisa", "pibic", "pibiti", "pivic"],
    "Extensão": ["extensao", "proec", "proeec", "pibeec", "voluntariado"],
}

# Editais de vida interna do departamento - eleição de chefe e subchefe,
# composição de colegiado, chefia de gabinete e afins. Não são oportunidade
# para ninguém de fora do quadro de servidores, e o público do site é de
# estudantes: entram no site do DES, não neste. Quem bater aqui é ignorado
# na importação, mesmo que também bata em AREA_PALAVRAS.
EXCLUIR_PALAVRAS = [
    "chefe", "chefia", "subchefe", "sub-chefe", "gabinete",
    "eleicao", "eleicoes", "colegiado", "conselho", "camara",
    "coordenador de curso", "coordenacao de curso",
    "representante", "comissao eleitoral",
]

# Só os 3 primeiros caracteres do mês (sem acento, minúsculo): o site do
# DES ora escreve o mês por extenso ("Maio"), ora abreviado ("Mai") - com
# 3 letras as duas formas caem na mesma chave.
MESES = {
    "jan": 1, "fev": 2, "mar": 3, "abr": 4, "mai": 5, "jun": 6,
    "jul": 7, "ago": 8, "set": 9, "out": 10, "nov": 11, "dez": 12,
}


# ---------------------------------------------------------------- básico
def sem_acento(texto: str) -> str:
    return unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()


def slug(texto: str) -> str:
    t = re.sub(r"[^a-zA-Z0-9]+", "-", sem_acento(texto)).strip("-").lower()
    return re.sub(r"-{2,}", "-", t)[:70] or "edital"


def baixa(url: str) -> str:
    """1 nova tentativa antes de desistir: o site do DES é lento às vezes,
    e uma execução agendada não tem ninguém olhando para tentar de novo."""
    req = urllib.request.Request(url, headers={"User-Agent": "conexao-estatistica-bot"})
    for tentativa in (1, 2):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode("utf-8", errors="replace")
        except Exception:
            if tentativa == 2:
                raise
            time.sleep(2)


def texto_limpo(html: str) -> str:
    t = re.sub(r"<[^>]+>", " ", html)
    t = re.sub(r"&nbsp;", " ", t)
    return " ".join(t.split())


def anota(chave: str, valor: str) -> None:
    saida = os.environ.get("GITHUB_OUTPUT")
    if saida:
        with open(saida, "a", encoding="utf-8") as f:
            f.write(f"{chave}={valor}\n")


# ---------------------------------------------------------------- listagem
def pagina_da_lista(fonte: dict, indice: int) -> str:
    lista = fonte["lista"]
    return lista if indice == 0 else f"{lista}?start={indice * 10}"


def itens_da_lista(fonte: dict, html: str) -> list[tuple[str, str, str]]:
    """[(id, url_absoluta, titulo), ...], na ordem em que aparecem.

    Sem repetir: as tres paginas repetem o mesmo edital no menu lateral e no
    corpo, e sem isso ele seria baixado duas vezes.
    """
    achados, vistos = [], set()
    exige = fonte.get("exige")
    for m in re.finditer(fonte["item"], html, re.S):
        caminho, id_fonte, titulo = m.group(1), m.group(2), texto_limpo(m.group(3))
        if not titulo or id_fonte in vistos:
            continue
        if exige and exige not in sem_acento(titulo).lower():
            continue
        vistos.add(id_fonte)
        achados.append((id_fonte, fonte["base"] + caminho, titulo))
    return achados


def paginas_do_indice(fonte: dict) -> list[str]:
    """Fontes separadas por ano (PRPI): devolve as paginas de ano, da mais
    recente para a mais antiga, limitadas a PAGINAS_NO_MAXIMO. A pagina de
    2026 lista os editais de 2026, e assim por diante."""
    try:
        html = baixa(fonte["indice"])
    except Exception as e:
        print(f"[!!] não abri o índice de {fonte['nome']}: {e}")
        return []
    anos, vistos = [], set()
    for m in re.finditer(fonte["item_indice"], html, re.S):
        if m.group(2) in vistos:
            continue
        vistos.add(m.group(2))
        anos.append(fonte["base"] + m.group(1))
    return anos[:PAGINAS_NO_MAXIMO]


def paginas_da_fonte(fonte: dict) -> list[str]:
    if fonte.get("indice"):
        return paginas_do_indice(fonte)
    return [pagina_da_lista(fonte, i) for i in range(PAGINAS_NO_MAXIMO)]


# ---------------------------------------------------------------- edital
def data_publicacao(html: str) -> date | None:
    m = re.search(r'documentPublished">\s*Publicado:\s*\w+,\s*(\d{1,2})\s+(\w+)\s+(\d{4})', html)
    if not m:
        return None
    dia, mes_nome, ano = m.group(1), sem_acento(m.group(2)).lower(), m.group(3)
    mes = MESES.get(mes_nome[:3])
    if not mes:
        return None
    try:
        return date(int(ano), mes, int(dia))
    except ValueError:
        return None


def resumo_do_corpo(html: str, fonte: dict) -> str:
    """Primeiro parágrafo com conteúdo de verdade. O corpo costuma começar
    com <p> de imagem, de espaçador ou de uma linha só ('Confira:'), que não
    servem de descrição no card - por isso o parágrafo mínimo de 40 letras."""
    corpo = html.split("documentByLine", 1)[-1]
    for m in re.finditer(r"<p[^>]*>(.*?)</p>", corpo, re.S):
        resumo = texto_limpo(m.group(1))
        if len(resumo) >= 40:
            return (resumo[:297] + "...") if len(resumo) > 300 else resumo
    return f"Confira os detalhes completos no site da {fonte['autor']}."


def areas_do_titulo(titulo: str) -> list[str]:
    alvo = sem_acento(titulo).lower()
    return [area for area, palavras in AREA_PALAVRAS.items()
            if any(p in alvo for p in palavras)]


def administrativo(titulo: str) -> bool:
    """Edital de vida interna do departamento (ver EXCLUIR_PALAVRAS)."""
    alvo = sem_acento(titulo).lower()
    return any(p in alvo for p in EXCLUIR_PALAVRAS)


# ---------------------------------------------------------------- escrita
def ja_importado(fonte: dict, id_fonte: str) -> bool:
    marca = f"fonte: {fonte['nome']}-editais-{id_fonte} "
    for post in DESTINO.glob("*/index.qmd"):
        if marca in post.read_text(encoding="utf-8"):
            return True
    return False


def preenche(modelo: str, valores: dict[str, str]) -> str:
    def bloco(m):
        return m.group(2) if valores.get(m.group(1), "").strip() else ""
    texto = re.sub(r"<!--se:(\w+)-->(.*?)<!--/se-->", bloco, modelo, flags=re.S)
    for chave, valor in valores.items():
        texto = texto.replace("{{" + chave + "}}", valor)
    return re.sub(r"\n{3,}", "\n\n", texto).strip() + "\n"


def importa_um(fonte: dict, id_fonte: str, url: str, titulo: str,
               dry_run: bool) -> str | None:
    try:
        pagina = baixa(url)
    except Exception as e:
        print(f"[!!] não abri {url}: {e}")
        return None

    publicado = data_publicacao(pagina)
    if not publicado:
        print(f"[!!] sem data de publicação reconhecível: {url}")
        return None
    if publicado < date.today() - timedelta(days=JANELA_DIAS):
        return "velho"

    # PRPI e PROEEC já dizem a área pela fonte; o DES, que publica edital de
    # tudo, precisa que ela saia do título.
    areas = fonte["areas"] if fonte["areas"] is not None else areas_do_titulo(titulo)
    cats = ["Oportunidades", "Editais"] + list(areas)
    cats_fmt = ", ".join(cats)
    pasta = DESTINO / f"{publicado.isoformat()}-{slug(titulo)}"
    if pasta.exists():
        pasta = pasta.with_name(f"{pasta.name}-{id_fonte}")

    resumo = resumo_do_corpo(pagina, fonte).replace('"', "'")
    valores = {
        "titulo": titulo.replace('"', "'"),
        "resumo": resumo,
        "autor": fonte["autor"],
        "data": publicado.isoformat(),
        "texto": f"<!-- fonte: {fonte['nome']}-editais-{id_fonte} -->\n\n{resumo}",
        "categorias": cats_fmt,
        "link": url,
        "thumbnail": "", "relatorio": "", "relatorio_html": "",
        "relatorio_pdf": "", "apresentacao": "",
    }
    conteudo = preenche(MODELO.read_text(encoding="utf-8"), valores)

    rotulo = f"{pasta.relative_to(RAIZ).as_posix()} ({', '.join(cats[2:]) or 'sem área'})"
    if dry_run:
        print(f"[dry-run] importaria {rotulo}")
        return rotulo
    pasta.mkdir(parents=True, exist_ok=True)
    (pasta / "index.qmd").write_text(conteudo, encoding="utf-8", newline="\n")
    print(f"[ok] importado {rotulo}")
    return rotulo


def importa_fonte(fonte: dict, dry_run: bool) -> list[str]:
    importados: list[str] = []
    print(f"\n--- {fonte['nome'].upper()}: {fonte.get('lista') or fonte['indice']}")

    for numero, endereco in enumerate(paginas_da_fonte(fonte), start=1):
        try:
            html = baixa(endereco)
        except Exception as e:
            print(f"[!!] não abri a página {numero} da listagem: {e}")
            break
        itens = itens_da_lista(fonte, html)
        if not itens:
            break

        parou = False
        for id_fonte, url, titulo in itens:
            if ja_importado(fonte, id_fonte):
                continue
            if administrativo(titulo):
                print(f"[--] pulado (edital administrativo): {titulo}")
                continue
            resultado = importa_um(fonte, id_fonte, url, titulo, dry_run)
            if resultado == "velho":
                parou = True
                break
            if resultado:
                importados.append(resultado)
            time.sleep(0.4)   # cortesia com o site da fonte, não é nosso
        if parou:
            break
    return importados


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    # `--fonte des` roda uma fonte só, útil para testar uma sem bater nas outras
    so_esta = None
    if "--fonte" in sys.argv:
        so_esta = sys.argv[sys.argv.index("--fonte") + 1]

    importados: list[str] = []
    for fonte in FONTES:
        if so_esta and fonte["nome"] != so_esta:
            continue
        try:
            importados += importa_fonte(fonte, dry_run)
        except Exception as e:
            # uma fonte fora do ar não pode derrubar a importação das outras
            print(f"[!!] fonte {fonte['nome']} falhou ({e}); sigo para a próxima")

    print(f"\n{len(importados)} edital(is) {'a importar' if dry_run else 'importado(s)'}.")
    anota("importados", str(len(importados)))
    anota("lista", "; ".join(importados))
    return 0


if __name__ == "__main__":
    sys.exit(main())
