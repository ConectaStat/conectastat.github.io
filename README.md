# Ciência| <br/> Estatística| <br/> Sociedade

Bem-vindo à casa do [ConectaStat](https://conectastat.github.io/), um projeto do [Departamento de Estatística da UFLA](https://des.ufla.br/). Este repositório contém todo o código-fonte e o conteúdo do site, uma plataforma que busca a popularização da estatística e da ciência de dados no sul de Minas.

O site é construído com [Quarto](https://quarto.org) e publicado pelo GitHub Pages. Qualquer pessoa da comunidade do DES pode publicar aqui: não é preciso saber programar, e todo o passo a passo está neste documento.

> Site de projeto vinculado ao Departamento de Estatística da UFLA. Este não é um site institucional da Universidade.

## Índice
1. [Equipe](#coordenação)
2. [Contribuidores](#contribuidores)
3. [Como Publicar](#como-publicar)
## Coordenação

O ConectaStat é conduzido no Departamento de Estatística da UFLA. A Equipe responde pelo rumo do projeto, pela orientação acadêmica e pela revisão do que é publicado.

<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="16.66%"><a href="https://github.com/USUARIO"><img src="https://github.com/USUARIO.png?size=100" width="100px;" alt="Nome do docente"/><br /><sub><b>Nome do docente</b></sub></a><br /><sub>Coordenação</sub></td>
       <td align="center" valign="top" width="16.66%"><a href="https://github.com/Leocarletto"><img src="https://avatars.githubusercontent.com/u/290053745?v=4?s=100" width="100px;" alt="Leonardo Carletto"/><br /><sub><b>Leonardo Carletto</b></sub></a><br /><a href="https://github.com/ConectaStat/conectastat.github.io/commits?author=Leocarletto" a> <a href="https://conectastat.github.io/" title="Codigo">💻</a> 
       <td align="center" valign="top" width="16.66%"><a href="https://github.com/uaipedro"><img src="https://avatars.githubusercontent.com/u/44395968?v=4?s=100" width="100px;" alt="Pedro Mambelli Fernandes"/><br /><sub><b>Pedro Mambelli Fernandes</b></sub></a><br /><a href="https://github.com/ConectaStat/conectastat.github.io/commits?author=uaipedro" title="Código">💻</a></td>
    </tr>
  </tbodz   y>
</table>

> Tabela a preencher: troque `USUARIO` pelo usuário do GitHub de cada docente e o nome exibido. Enquanto estiver assim, a foto aparece quebrada.

## Contribuidores

Lista dos contribuidores dos projetos de Organizacao e apresentacao de dados.

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <<td align="center" valign="top" width="16.66%"><a href="https://github.com/user"><img src="https://github.com/user.png?size=100" width="100px;" alt="Contribuidor"/><br /><sub><b>Nome do Contribuidor</b></sub></a><br /><sub>Contribuidor</sub></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

Este projeto segue a especificação [all-contributors](https://github.com/all-contributors/all-contributors). Toda forma de contribuição é bem-vinda, não só código.

A lista acima se mantém sozinha. Para incluir alguém, basta comentar em qualquer issue ou pull request do repositório:

```
@all-contributors please add @usuario for content
```

Troque `content` pelo tipo de contribuição: `coordenacao`, `content` ou `code`, que são as três marcas do projeto. O robô abre um pull request atualizando a tabela e o arquivo `.all-contributorsrc`.

## Como Publicar

Uma seção do site recebe envios de qualquer pessoa; o resto é publicado pela equipe. A versão para quem chega pelo site está em [Como Contribuir](https://conectastat.github.io/sobre/como-contribuir/).

**1. Organização e Apresentação de Dados: envio aberto.** Não exige experiência com Git. O estudante preenche o [formulário do site](https://conectastat.github.io/enviar.html) e o GitHub abre com a submissão pronta. Assim que ele confirma, o robô monta a página e abre um pedido de publicação para a equipe revisar. A resposta vai na própria submissão.

**2. Oportunidades: importação automática.** Toda segunda-feira, `scripts/importar_editais.py` busca editais novos em três fontes oficiais - [des.ufla.br/editais](https://des.ufla.br/editais) (monitoria e docência voluntária), [prpi.ufla.br](https://prpi.ufla.br/iniciacao-cientifica/editais) (iniciação científica) e [proeec.ufla.br](https://proeec.ufla.br/editais/programa-institucional-de-bolsas-de-extensao) (bolsas de extensão) -, monta a página de cada um e abre um pedido de publicação, a mesma revisão da equipe antes de ir ao ar. Cada fonte já entrega a área: DES pelas palavras do título, PRPI sempre Pesquisa, PROEEC sempre Extensão. Edital do DES que não bate com nenhuma palavra fica só na listagem geral de Oportunidades - é o caso de concursos docentes e de professor substituto, que não são oportunidade para o público do site. Já os de vida interna do departamento (eleição de chefe e subchefe, chefia de gabinete, colegiado) não entram nem na listagem geral: ver `EXCLUIR_PALAVRAS` no script.

**3. As demais seções sao publicados entrando em contato com o [ConectaStat](https://conectastat.github.io/sobre/contato/).** 
