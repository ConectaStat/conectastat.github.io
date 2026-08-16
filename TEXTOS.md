# Mapa de textos do site

Inventário de **todo o texto editável** do ConectaStat, na ordem em que
o visitante encontra. Serve para revisão: reescreva o que quiser dentro dos
blocos citados e devolva. Cada bloco indica o arquivo exato onde ele mora.

Está tudo aqui: títulos, textos corridos, tabelas e os resumos que aparecem nos
cards. Ficam de fora apenas os relatórios enviados pelos estudantes, que são
conteúdo de terceiros e não devem ser reescritos.

**Como devolver correções:** copie o trecho que quiser mudar, reescreva e
devolva indicando o arquivo (cada bloco traz o caminho logo abaixo do título).
Não precisa se preocupar com formatação: negrito, links e acentos são
ajustados na hora de aplicar.

Este documento é gerado a partir dos arquivos do site. Depois de aplicar
correções, refaça com:

```bash
python scripts/gerar_textos.py
```

---

## Mapa do site

```
home/
├── index.qmd ─────────────────── página inicial ................. §1
│   ├── hero ........................ slogan sobre a ilustração
│   ├── disclaimer .................. logo abaixo da hero
│   ├── "O que é o ConectaStat…" .... texto de apresentação
│   ├── oportunidades · cursos e eventos ..... carrosséis
│   └── onde estamos ................ mapa + endereço
├── _quarto.yml ───────────────── rodapé e menu ................. §2 e §3
│
├── estatistica/index.qmd ─────── Estatística .................... §4
├── assessoria/index.qmd ──────── Assessoria e Consultoria
├── acoes/
│   ├── revista-cientifica/index.qmd ── Revista Científica
│   └── lad/index.qmd ───────────────── Laboratório de Análises de Dados
├── cursos/
│   ├── graduacao/index.qmd ─────── Graduação
│   └── pos-graduacao/
│       ├── index.qmd ───────────── Pós-Graduação
│       └── egressos/index.qmd ──── Painel dos Egressos
├── O_que_fazemos/
│   ├── pesquisa/
│   │   ├── index.qmd ───────────── Pesquisa (+ cards)
│   │   └── editais/index.qmd ───── Editais de Pesquisa
│   ├── ensino/
│   │   ├── index.qmd ───────────── Ensino (+ cards)
│   │   ├── organizacao-e-apresentacao-de-dados/
│   │   │   ├── index.qmd ───────── Organização e Apresentação de Dados
│   │   │   └── posts/ ──────────── projetos enviados ............ §5
│   │   ├── softwares/index.qmd ─── Softwares (sem conteúdo ainda)
│   │   ├── materiais/index.qmd ─── Materiais (sem conteúdo ainda)
│   │   └── editais/index.qmd ───── Editais de Ensino
│   └── extensao/
│       ├── index.qmd ───────────── Extensão (+ cards)
│       ├── acoes/index.qmd ─────── Encontros com a Comunidade
│       └── editais/index.qmd ───── Editais de Extensão
│
├── oportunidades/  ┐  cada uma com:
├── eventos/        ┘    index.qmd ── página de arquivo ......... §4
                         posts/ ───── conteúdo datado ........... §5
│
└── enviar.qmd ────────────────── Formulário de envio
```

---

## 1. Página inicial

```
index.qmd
├── hero .................. slogan + ilustração
├── o projeto ............. texto de apresentação
├── em destaque ........... carrossel (notícias + cursos/eventos +
│                           encontros com a comunidade)
├── oportunidades ......... carrossel
└── onde estamos .......... mapa + endereço
```


### Hero (topo da home)

> Slogan sobre a ilustração:
>
>


### Seção da home: Em Destaque

> *(sem texto próprio: a página só exibe a listagem)*


### Seção da home: Oportunidades

> *(sem texto próprio: a página só exibe a listagem)*


### Seção da home: Onde estamos

> *(sem texto próprio: a página só exibe a listagem)*


### Bloco do mapa (endereço)

> Departamento de Estatística da UFLA
> Trevo Rotatório Professor Edmir Sá Santos, s/n
> Campus Universitário, Lavras/MG
> CEP 37203-202 · Caixa Postal 3037


---

## 2. Rodapé (todas as páginas)

`_quarto.yml` › `website: page-footer`


**Disclaimer (canto esquerdo):**

> Site de projeto de extensão vinculado ao Departamento de Estatística da UFLA. Este não é um site institucional da Universidade.

**Ícones:** GitHub, Instagram e LinkedIn (os dois últimos ainda sem link).


---

## 3. Menu do topo

`_quarto.yml` › `website: navbar`


```
Ciência| Estatística| Sociedade   ← slogan à esquerda (leva à home)

  A Estatística
  Nossos Cursos
      └── Graduação
      └── Pós-Graduação
  O Que Fazemos
      └── Pesquisa
      └── Ensino
      └── Extensão
  Ações
      └── Revista Científica
      └── Nossos Livros
      └── Assessoria e Consultoria Estatística
      └── Laboratório de Análises de Dados (LAD)
      └── Cursos e Eventos
  Sobre o ConectaStat
      └── Quem Somos
      └── Uso de IA
      └── Como Contribuir
      └── Entre em Contato
```


---

## 4. Páginas das seções


### Estatística
`estatistica/index.qmd`

**Título (aparece no banner):** A Estatística

**Subtítulo:** A ciência de aprender com os dados. E uma das profissões mais promissoras da atualidade.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> ## O que é a Estatística?
>
> A Estatística é a ciência que desenvolve e aplica métodos para **coletar,
> organizar, analisar e interpretar dados**, transformando informação em
> conhecimento e apoiando decisões em condições de incerteza. Ela é a base
> fundamental da Ciência de Dados e está presente em praticamente todas as
> áreas do conhecimento: agricultura, saúde, indústria, finanças, esportes,
> políticas públicas e inteligência artificial.
>
> ## Onde atua o estatístico?
>
> O profissional de Estatística atua em um mercado amplo e em expansão:
>
> - **Ciência de Dados e Inteligência Artificial**: modelagem preditiva,
>   aprendizado de máquina e análise de grandes volumes de dados;
> - **Agronegócio e experimentação**: planejamento e análise de experimentos,
>   melhoramento genético e agricultura de precisão;
> - **Saúde e bioestatística**: ensaios clínicos, epidemiologia e vigilância
>   em saúde pública;
> - **Mercado financeiro e seguros**: análise de risco, precificação e
>   modelagem atuarial;
> - **Indústria e qualidade**: controle estatístico de processos e
>   confiabilidade;
> - **Pesquisa e academia**: desenvolvimento de novos métodos e formação de
>   pessoas.
>
> Pesquisas de mercado apontam a carreira de estatístico e de cientista de
> dados entre as **melhores e mais bem remuneradas profissões** da era digital,
> com demanda muito superior à oferta de profissionais qualificados.
>
> ## Estude Estatística na UFLA
>
> ### Graduação: foco em Ciência de Dados
>
> Embora seja um **Bacharelado em Estatística**, o
> [curso de graduação](../cursos/graduacao/index.qmd) da UFLA tem forte **ênfase
> em Ciência de Dados**: além da base sólida em probabilidade e inferência, o
> estudante aprende programação, bancos de dados e aprendizado de máquina para
> extrair conhecimento de grandes volumes de dados. É o caminho de quem quer
> partir de dados reais, chegar a modelos preditivos e ir muito além.
>
> ### Pós-graduação: foco em Estatística e Experimentação Agropecuária
>
> O [Programa de Pós-Graduação em Estatística e Experimentação Agropecuária
> (PPGEEA)](../cursos/pos-graduacao/index.qmd) oferece **mestrado** e
> **doutorado** com tradição em **estatística e experimentação agropecuária**:
> planejamento e análise de experimentos, melhoramento genético e agricultura
> de precisão. É a formação de quem transforma dados de campo, como as safras
> de café da região de Lavras, em decisões com rigor científico.


### Nossos Cursos › Graduação
`cursos/graduacao/index.qmd`

**Título (aparece no banner):** Graduação

**Subtítulo:** Bacharelado em Estatística com ênfase em Ciência de Dados.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> ## Sobre o curso
>
> O curso de **Graduação em Estatística** da UFLA iniciou suas atividades no
> semestre 2024/1 e forma profissionais preparados para atuar com análise de
> dados, modelagem estatística e ciência de dados em empresas, instituições de
> pesquisa e órgãos públicos.
>
> Com uma ampla formação os alunos são expostos aos mais variados tipos de situações, alguns exemplos são os projetos de **Organização e Apresentação de Dados** em que cada aluno escolhe uma base de dados publica para desenvolver uma analise exploratória e desenvolver um relatório do assunto, isso tudo desde o primeiro período! Esses projetos podem ser visualizados
> [aqui](../../O_que_fazemos/ensino/organizacao-e-apresentacao-de-dados/index.qmd).
>
> ## Matriz curricular
>
> A matriz curricular está organizada em núcleos de formação, cursados ao longo
> de 8 semestres:
>
> | Núcleo | Conteúdos principais |
> |---|---|
> | **Base matemática** | Cálculo, Álgebra Linear, Matemática Discreta |
> | **Probabilidade e Inferência** | Probabilidade, Inferência Estatística, Processos Estocásticos |
> | **Modelagem estatística** | Modelos de Regressão, Planejamento e Análise de Experimentos, Análise Multivariada, Séries Temporais |
> | **Computação e dados** | Programação, Estatística Computacional, Bancos de Dados, Aprendizado de Máquina |
> | **Formação complementar** | Amostragem, Controle de Qualidade, Estatística Espacial, disciplinas eletivas |
> | **Prática profissional** | Projetos orientados, Estágio Supervisionado, Trabalho de Conclusão de Curso |
>
> A matriz oficial completa, com ementas e pré-requisitos detalhados, está no
> [site do DES/UFLA](https://des.ufla.br/graduacao). Ou veja aqui, módulo a
> módulo:
>
> ### 1º módulo
>
> | Código | Disciplina | Créditos | Requisito |
> |---|---|:---:|:---:|
> | GES110 | Matemática para Estatística I | 8 | - |
> | GES136 | Introdução aos Planos Experimentais | 4 | - |
> | GES139 | Organização e Apresentação de Dados | 8 | - |
> | GES140 | Vivência Profissional em Estatística | 2 | - |
>
> ### 2º módulo
>
> | Código | Disciplina | Créditos | Requisito |
> |---|---|:---:|:---:|
> | GES113 | Probabilidade I | 8 | GES110 |
> | GES135 | Fundamentos de Programação | 4 | - |
> | GES137 | Matemática para Estatística II | 10 | GES110 |
>
> ### 3º módulo
>
> | Código | Disciplina | Créditos | Requisito |
> |---|---|:---:|:---:|
> | GES116 | Matemática para Estatística III | 8 | GES137 |
> | GES117 | Probabilidade II | 6 | GES113 |
> | GES134 | Estrutura de Dados | 8 | GES135 |
> | GES141 | Consultoria em Estatística I | 2 | GES136 |
>
> ### 4º módulo
>
> | Código | Disciplina | Créditos | Requisito |
> |---|---|:---:|:---:|
> | GES118 | Inferência Estatística I | 8 | GES113 |
> | GES119 | Modelos Lineares I | 8 | GES113 |
> | GES142 | Amostragem | 4 | GES113 |
>
> ### 5º módulo
>
> | Código | Disciplina | Créditos | Requisito |
> |---|---|:---:|:---:|
> | GES122 | Modelos Lineares II | 8 | GES119 |
> | GES123 | Planejamento e Análise de Experimentos | 4 | GES136 |
> | GES124 | Inferência Estatística II | 8 | GES118 |
>
> ### 6º módulo
>
> | Código | Disciplina | Créditos | Requisito |
> |---|---|:---:|:---:|
> | GES125 | Séries Temporais | 4 | GES124 |
> | GES126 | Estatística Computacional | 6 | GES135 |
> | GES127 | Consultoria em Estatística II | 4 | GES141 |
> | GES130 | Ciência de Dados e Big Data | 4 | GES134 |
> | GES138 | Técnicas Multivariadas | 4 | GES124 |
>
> ### 7º módulo
>
> | Código | Disciplina | Créditos | Requisito |
> |---|---|:---:|:---:|
> | GES128 | Modelos Lineares Generalizados | 6 | GES119 |
> | GES129 | Inferência Bayesiana | 4 | GES118 |
> | GES131 | Mineração de Dados e Aprendizagem de Máquinas | 6 | GES134 |
>
> ### 8º módulo
>
> | Código | Disciplina | Créditos | Requisito |
> |---|---|:---:|:---:|
> | EES5889 | Estágio Supervisionado | 0 | - |


### Nossos Cursos › Pós-Graduação
`cursos/pos-graduacao/index.qmd`

**Título (aparece no banner):** Pós-Graduação

**Subtítulo:** Programa de Pós-Graduação em Estatística e Experimentação Agropecuária: mestrado e doutorado.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> A UFLA abriga diversos [Programas de Pós-Graduação](https://prpg.ufla.br/mostrapg/pt-br/ultimas-noticias/82-programas-de-pos-graduacao),
> e o [Painel de Perfil dos Ingressantes](https://paineis.ufla.br/pos-graduacao/120-painel/418-perfil-ingressantes-pos-graduacao-stricto-sensu){target="_blank"}
> mostra quem entra no stricto sensu, por gênero, idade, região de origem e
> formação. Aqui tratamos com maior afinidade o de
> **Estatística e Experimentação Agropecuária (PPGEEA)**, com cursos de
> **mestrado** e **doutorado**, formando pesquisadores e docentes com sólida
> base teórica e forte vocação aplicada.
>
> ## Estatística e Experimentação Agropecuária
>
> O Programa de Pós-Graduação em Estatística e Experimentação Agropecuária concentra suas atividades no estudo e desenvolvimento de métodos estatísticos modernos para a análise de dados nas diversas áreas do conhecimento, mas com especial atenção à Estatística e Experimentação Agropecuária. O objetivo principal do programa é formar recursos humanos e garantir sua qualificação, aprimorando seus conhecimentos em Estatística e Experimentação para o exercício de atividades de docência e de pesquisa em instituições de ensino, pesquisa e em empresas, públicas ou privadas. As linhas de pesquisa são: Estatística Experimental e Aplicada, Teoria Matemática e Métodos Estatísticos, Análise Multivariada e Estatística Espacial, sendo que estas envolvem:
>
> - **Estatística Experimental:** planejamento de experimentos, análise de dados oriundos de estudos agropecuários e interpretação dos resultados obtidos;
>
> - **Análise de regressão e séries temporais:** estimação e predição de modelos lineares e não lineares e análise de dados cronológicos;
>
> - **Teoria e métodos estatísticos:** estudos de dinâmica de populações, inferência bayesiana e modelagem estatística e métodos de comparações múltiplas;
>
> - **Estatística genética e genômica:** ênfase na avaliação genética, em métodos de predição de valores genéticos e em inferências sobre parâmetros genéticos;
>
> - **Métodos multivariados:** proposição e avaliação de testes e análise de estabilidade de cultivares;
>
> - **Métodos computacionais:** uso de métodos computacionais intensivos e técnicas de data science na aplicação e desenvolvimento de métodos estatísticos;
>
> - **Estatística espacial:** análise de dados correlacionados espacialmente e espaço-temporalmente, em estudos de geoestatística, processos pontuais e análise de dados de áreas.
>
> ## Ingresso
>
>  - O processo seletivo ocorre anualmente, com início do curso no primeiro semestre de cada ano. Eventualmente, também são realizados processos seletivos para o segundo semestre.
>
> ## O Programa
>
>  - O programa é financiado com recursos do Programa de Apoio à Pós-Graduação (PROAP) da Coordenação de Aperfeiçoamento de Pessoal de Nível Superior (CAPES), além do financiamento da maioria dos discentes, por meio de bolsas de estudos concedidas pela CAPES, Conselho Nacional de Desenvolvimento Científico e Tecnológico (CNPq) e Fundação de Amparo à Pesquisa do Estado de Minas Gerais (FAPEMIG).              
>
>
> ## Disciplinas
>
> Entre as disciplinas oferecidas regularmente estão:
>
> | Disciplina | Tema |
> |---|---|
> | Inferência Estatística | Estimação, testes de hipóteses e teoria assintótica |
> | Modelos Lineares | Teoria e aplicação de modelos de regressão |
> | Planejamento de Experimentos | Delineamentos experimentais e análise |
> | Estatística Computacional | Simulação, métodos de Monte Carlo e otimização |
> | Modelos Mistos | Efeitos aleatórios e dados longitudinais |
> | Estatística Bayesiana | Inferência bayesiana e métodos MCMC |
> | Séries Temporais | Modelagem e previsão de dados temporais |
>
> A relação completa de disciplinas, docentes e turmas está no
> [portal do PPGEEA no SIGAA](https://sigaa.ufla.br/sigaa/public/programa/portal.jsf?lc=pt_BR&id=1702){target="_blank"}.
>
> ## Projetos de pesquisa
>
> Os projetos de pesquisa em andamento no programa são registrados e consultados
> na [Pró-Reitoria de Pesquisa e Inovação (PRPI/UFLA)](https://prpi.ufla.br/projetos-de-pesquisa){target="_blank"}.
>
> ## Painel dos Egressos
>
> A trajetória dos nossos egressos (setores de atuação, regiões e formação
> continuada) está reunida em um dashboard interativo: o
> [Painel dos Egressos](egressos/index.qmd).


### Nossos Cursos › Pós-Graduação › Painel dos Egressos
`cursos/pos-graduacao/egressos/index.qmd`

**Título (aparece no banner):** Painel dos Egressos

**Subtítulo:** Para onde foram os egressos da Estatística da UFLA: setores, regiões e formação continuada.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> O **Painel dos Egressos** reúne, em um dashboard interativo, a trajetória
> dos egressos da graduação e da pós-graduação em Estatística da UFLA:
> os setores em que atuam, as regiões do país e do exterior para onde foram
> e a formação continuada que seguiram após o curso.


### O Que Fazemos › Pesquisa
`O_que_fazemos/pesquisa/index.qmd`

**Título (aparece no banner):** Pesquisa

**Subtítulo:** A investigação científica desenvolvida no Departamento de Estatística da UFLA.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> ## Núcleos e Grupos de Pesquisa
>
> ## Editais de Pesquisa
>
> [Ver todos os editais de pesquisa »](editais/index.qmd){.listing-mais}


### O Que Fazemos › Pesquisa › Editais
`O_que_fazemos/pesquisa/editais/index.qmd`

**Título (aparece no banner):** Editais de Projetos de Pesquisa

**Subtítulo:** Iniciação científica e demais chamadas ligadas à pesquisa.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> *(sem texto próprio: a página só exibe a listagem)*


### O Que Fazemos › Ensino
`O_que_fazemos/ensino/index.qmd`

**Título (aparece no banner):** Ensino

**Subtítulo:** Iniciativas que fortalecem a formação em Estatística dentro e fora da sala de aula.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> ## Projetos de Ensino, Softwares e Materiais Didáticos
>
> ## Editais de Ensino
>
> [Ver todos os editais »](editais/index.qmd){.listing-mais}

**Cards de tópico desta página:**

> **Organização e Apresentação de Dados**  
> Projetos de análise de dados feitos pelos estudantes de primeiro período da graduação, do dado bruto ao relatório final.
>
> **Softwares**  
> Aplicativos, pacotes e ferramentas computacionais desenvolvidos como apoio ao ensino de Estatística.
>
> **Materiais**  
> Apostilas, tutoriais e recursos didáticos abertos produzidos pelo departamento.
>


### O Que Fazemos › Ensino › Organização e Apresentação de Dados
`O_que_fazemos/ensino/organizacao-e-apresentacao-de-dados/index.qmd`

**Título (aparece no banner):** Organização e Apresentação de Dados

**Subtítulo:** Análises e projetos desenvolvidos pelos estudantes de Estatística da UFLA desde o primeiro período.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> Cada card abaixo é um projeto publicado: análises de dados reais feitas
> pelos nossos estudantes, do dado bruto ao relatório final. Explore os
> trabalhos e, quando estiver pronto, envie o seu.


### O Que Fazemos › Ensino › Softwares
`O_que_fazemos/ensino/softwares/index.qmd`

**Título (aparece no banner):** Softwares

**Subtítulo:** Aplicativos, pacotes e ferramentas computacionais de apoio ao ensino de Estatística.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> Ferramentas computacionais desenvolvidas nos projetos de ensino do
> departamento. Os primeiros itens serão publicados em breve.


### O Que Fazemos › Ensino › Materiais
`O_que_fazemos/ensino/materiais/index.qmd`

**Título (aparece no banner):** Materiais

**Subtítulo:** Apostilas, tutoriais e recursos didáticos abertos de apoio às disciplinas.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> Materiais didáticos produzidos nos projetos de ensino do departamento.
> Os primeiros itens serão publicados em breve.


### O Que Fazemos › Ensino › Editais
`O_que_fazemos/ensino/editais/index.qmd`

**Título (aparece no banner):** Editais de Ensino e docência

**Subtítulo:** Monitorias, docência voluntária e demais chamadas dos projetos de ensino.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> *(sem texto próprio: a página só exibe a listagem)*


### O Que Fazemos › Extensão
`O_que_fazemos/extensao/index.qmd`

**Título (aparece no banner):** Extensão

**Subtítulo:** A Estatística a serviço da comunidade: popularização da ciência e letramento estatístico.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> ## Projetos de Extensão
>
> ## Editais de Extensão
>
> [Ver todos os editais de extensão »](editais/index.qmd){.listing-mais}


### O Que Fazemos › Extensão › Encontros com a Comunidade
`O_que_fazemos/extensao/acoes/index.qmd`

**Título (aparece no banner):** Encontros com a Comunidade

**Subtítulo:** Cursos, palestras, parcerias e atividades levadas à comunidade.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> Os encontros do Departamento de Estatística com a comunidade: cursos abertos,
> palestras em escolas, parcerias com instituições e ações de divulgação
> científica. Cada encontro publicado aqui entra também no **Em Destaque** da
> página inicial, junto com as notícias e os eventos. Os primeiros serão
> publicados em breve.


### O Que Fazemos › Extensão › Editais
`O_que_fazemos/extensao/editais/index.qmd`

**Título (aparece no banner):** Editais de Projetos de Extensão

**Subtítulo:** Chamadas e editais ligados aos projetos de extensão.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> *(sem texto próprio: a página só exibe a listagem)*


### Ações › Revista Científica
`acoes/revista-cientifica/index.qmd`

**Título (aparece no banner):** Revista Científica

**Subtítulo:** Brazilian Journal of Biometrics, periódico científico ligado ao Departamento de Estatística da UFLA.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> O Departamento de Estatística da UFLA é responsável pela publicação da
> **Brazilian Journal of Biometrics (BJB)**, revista oficial da [Região
> Brasileira da Sociedade Internacional de Biometria
> (RBras)](https://rbras.org.br/){target="_blank"}.
>
> O objetivo geral da BJB é publicar artigos de pesquisa originais que
> explorem, promovam e ampliem métodos de ciência de dados, estatística e
> matemática aplicados às ciências biológicas.
>
> A BJB não cobra taxa de submissão nem de publicação: os modelos em Word e
> LaTeX estão disponíveis no [site da
> revista](https://biometria.ufla.br/index.php/BBJ){target="_blank"}, e o envio
> de artigos é feito pelo [sistema de submissão da
> BJB](https://biometria.ufla.br/index.php/BBJ/login?source=%2Findex.php%2FBBJ%2Fsubmission){target="_blank"}.
>
> [Conhecer a revista](https://biometria.ufla.br/index.php/BBJ){target="_blank"}


### Ações › Nossos Livros
`acoes/livros/index.qmd`

**Título (aparece no banner):** Nossos Livros

**Subtítulo:** Livros publicados pela Editora UFLA e escritos por docentes do Departamento de Estatística.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> [Ver todos os títulos na Editora UFLA »](https://www.editoraufla.com.br/){target="_blank"}


### Ações › Assessoria e Consultoria Estatística
`assessoria/index.qmd`

**Título (aparece no banner):** Assessoria e Consultoria Estatística

**Texto da página:**

> *(sem texto próprio: a página só exibe a listagem)*


### Ações › Laboratório de Análises de Dados (LAD)
`acoes/lad/index.qmd`

**Título (aparece no banner):** LAD

**Subtítulo:** Laboratório de Análises de Dados do Departamento de Estatística da UFLA.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> ## O Laboratório
>
> O **Laboratório de Análises de Dados (LAD)** é uma das ações do
> [Departamento de Estatística](https://des.ufla.br/) da Universidade Federal
> de Lavras.
>
> Esta página está em construção. Em breve ficam aqui a apresentação do
> laboratório, as atividades que ele desenvolve e a forma de solicitar
> atendimento.
>
> ## Enquanto isso
>
> - Para falar com a equipe do departamento, veja [entre em
>   contato](../../sobre/contato/index.qmd).


### Ações › Cursos e Eventos (arquivo)
`eventos/index.qmd`

**Título (aparece no banner):** Cursos e Eventos

**Subtítulo:** Cursos, minicursos, seminários, palestras, workshops e defesas.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> *(sem texto próprio: a página só exibe a listagem)*


### Oportunidades (arquivo)
`oportunidades/index.qmd`

**Título (aparece no banner):** Oportunidades

**Subtítulo:** Editais internos e oportunidades de estudo.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> *(sem texto próprio: a página só exibe a listagem)*


### Enviar conteúdo (formulário do site)
`enviar.qmd`

**Título (aparece no banner):** Envie seu projeto

**Subtítulo:** Publique a sua análise em Organização e Apresentação de Dados.  
*(hoje oculto no site; fica só no código)*

**Texto da página:**

> ## Como funciona
>
> Este formulário publica em **Projetos › Ensino › [Organização e Apresentação de
> Dados](O_que_fazemos/ensino/organizacao-e-apresentacao-de-dados/index.qmd)**, a
> seção dos projetos de análise feitos pelos estudantes da graduação. É o único
> caminho automatizado do site.
>
> Editais, eventos, softwares, materiais didáticos e ações de extensão **não
> passam por aqui**: são publicados pela equipe do site, a pedido dos docentes e
> da chefia do departamento. Veja [Como
> Contribuir](sobre/como-contribuir/index.qmd).
>
> Preencha o formulário abaixo **sem sair do site**. Ao enviar, o GitHub abre em
> outra aba com a submissão **já preenchida**: é só revisar, anexar os arquivos
> e confirmar. Basta estar logado no GitHub (a conta é gratuita).
>
> A partir daí o robô monta a página sozinho e a equipe do departamento revisa
> antes de publicar. Você recebe a resposta na própria submissão.
>
> Os **arquivos** são anexados na tela do GitHub que abre: a imagem de capa e o
> relatório, em `.html` (compactado em `.zip`) ou `.pdf`. Basta arrastar cada um
> para o campo correspondente antes de clicar em *Create*. O relatório aparece
> **inteiro dentro da página** do projeto, e não como um link para sair dela.
> Havendo escolha, prefira `.html`: ele se integra à página, com índice na
> lateral, enquanto o `.pdf` fica dentro de uma moldura e não abre embutido em
> boa parte dos celulares.


---

## 5. Conteúdo datado (posts já publicados)


### Oportunidades: posts publicados (11)


#### Edital Nº 006/2026 - Docência Voluntária - DES 2ºsem/2026
`oportunidades/posts/2026-07-27-edital-no-006-2026-docencia-voluntaria-des-2osem-2026/index.qmd`

**Resumo (aparece no card):** O Chefe do Departamento de Estatística do Instituto de Ciências Exatas e Tecnológicas da Universidade Federal de Lavras torna pública a abertura das inscrições para a docência voluntária no Componente Curricular listado no quadro a seguir.

> O Chefe do Departamento de Estatística do Instituto de Ciências Exatas e Tecnológicas da Universidade Federal de Lavras torna pública a abertura das inscrições para a docência voluntária no Componente Curricular listado no quadro a seguir.
>
> [Ler o edital completo »](https://des.ufla.br/editais/141-edital-n-006-2026-docencia-voluntaria-des-2-sem-2026)

#### Edital Nº 005/2026 - Seleção de monitores remunerados para o 2º semestre de 2026
`oportunidades/posts/2026-07-13-edital-no-005-2026-selecao-de-monitores-remunerados-para-o-2o-semestre/index.qmd`

**Resumo (aparece no card):** O Chefe do Departamento de Estatística do Instituto de Ciências Exatas e Tecnológicas da Universidade Federal de Lavras torna pública a abertura das inscrições para a monitoria remunerada nos Componentes Curriculares listados no quadro a seguir.

> O Chefe do Departamento de Estatística do Instituto de Ciências Exatas e Tecnológicas da Universidade Federal de Lavras torna pública a abertura das inscrições para a monitoria remunerada nos Componentes Curriculares listados no quadro a seguir.
>
> [Ler o edital completo »](https://des.ufla.br/editais/139-edital-n-005-2026-selecao-de-monitores-remunerados-para-2-2026)

#### Edital PRPI Nº 03/2026 - PIBITI/CNPq
`oportunidades/posts/2026-05-20-edital-prpi-no-03-2026-pibiti-cnpq/index.qmd`

**Resumo (aparece no card):** A Pró-Reitoria de Pesquisa e Inovação (PRPI) da Universidade Federal de Lavras (UFLA) torna público este edital e convida todos(as) os(as) servidores(as) docentes e técnico(a)-administrativos(as) desta instituição e pesquisadores(as) externos(as) credenciados(as) como docentes permanentes em prog...

> A Pró-Reitoria de Pesquisa e Inovação (PRPI) da Universidade Federal de Lavras (UFLA) torna público este edital e convida todos(as) os(as) servidores(as) docentes e técnico(a)-administrativos(as) desta instituição e pesquisadores(as) externos(as) credenciados(as) como docentes permanentes em prog...
>
> [Ler o edital completo »](https://prpi.ufla.br/noticias-prpi/638-oportunidade-de-bolsa-it-aberto-edital-pibiti-cnpq)

#### Edital PRPI Nº 02/2026 - PIBIC/CNPq
`oportunidades/posts/2026-05-19-edital-prpi-no-02-2026-pibic-cnpq/index.qmd`

**Resumo (aparece no card):** A Pró-Reitoria de Pesquisa e Inovação (PRPI) da Universidade Federal de Lavras (UFLA) torna público este edital e convida todos(as) os(as) servidores(as) docentes e técnicos(as)-administrativos(as) desta instituição e pesquisadores(as) externos(as) credenciados(as) como docentes permanentes em pr...

> A Pró-Reitoria de Pesquisa e Inovação (PRPI) da Universidade Federal de Lavras (UFLA) torna público este edital e convida todos(as) os(as) servidores(as) docentes e técnicos(as)-administrativos(as) desta instituição e pesquisadores(as) externos(as) credenciados(as) como docentes permanentes em pr...
>
> [Ler o edital completo »](https://prpi.ufla.br/noticias-prpi/637-edital-pibic-cnpq-em-breve)

#### Edital Nº 003/2026 - Seleção de monitores voluntários para 2026
`oportunidades/posts/2026-05-06-edital-no-003-2026-selecao-de-monitores-voluntarios-para-2026/index.qmd`

**Resumo (aparece no card):** O Chefe em exercício do Departamento de Estatística do Instituto de Ciências Exatas e Tecnológicas da Universidade Federal de Lavras torna pública a abertura das inscrições para a monitoria voluntária nos Componentes Curriculares listados no quadro a seguir.

> O Chefe em exercício do Departamento de Estatística do Instituto de Ciências Exatas e Tecnológicas da Universidade Federal de Lavras torna pública a abertura das inscrições para a monitoria voluntária nos Componentes Curriculares listados no quadro a seguir.
>
> [Ler o edital completo »](https://des.ufla.br/editais/137-edital-n-003-2026-selecao-de-monitores-voluntarios-para-2026)

#### Edital PRPI Nº 01/2026 - PIVIC/UFLA
`oportunidades/posts/2026-03-18-edital-prpi-no-01-2026-pivic-ufla/index.qmd`

**Resumo (aparece no card):** A Pró-Reitoria de Pesquisa e Inovação (PRPI) da Universidade Federal de Lavras torna público este edital e convida todos os servidores docentes, técnico-administrativos desta instituição e pesquisadores externos credenciados como docentes permanentes em programas de pós-graduação da UFLA, a parti...

> A Pró-Reitoria de Pesquisa e Inovação (PRPI) da Universidade Federal de Lavras torna público este edital e convida todos os servidores docentes, técnico-administrativos desta instituição e pesquisadores externos credenciados como docentes permanentes em programas de pós-graduação da UFLA, a parti...
>
> [Ler o edital completo »](https://prpi.ufla.br/noticias-prpi/634-edital-prpi-n-01-2026-pivic-ufla-fluxo-continuo)

#### Edital Nº 002/2026 - Seleção de monitores voluntários para 2026
`oportunidades/posts/2026-03-18-edital-no-002-2026-selecao-de-monitores-voluntarios-para-2026/index.qmd`

**Resumo (aparece no card):** O Chefe do Departamento de Estatística do Instituto de Ciências Exatas e Tecnológicas da Universidade Federal de Lavras torna pública a abertura das inscrições para a monitoria voluntária nos Componentes Curriculares listados no quadro a seguir.

> O Chefe do Departamento de Estatística do Instituto de Ciências Exatas e Tecnológicas da Universidade Federal de Lavras torna pública a abertura das inscrições para a monitoria voluntária nos Componentes Curriculares listados no quadro a seguir.
>
> [Ler o edital completo »](https://des.ufla.br/editais/136-edital-n-002-2026-selecao-de-monitores-voluntarios-para-2026)

#### Edital Nº 001/2026 - Docência Voluntária - DES 1ºsem/2026
`oportunidades/posts/2026-01-12-edital-no-001-2026-docencia-voluntaria-des-1osem-2026/index.qmd`

**Resumo (aparece no card):** O Chefe em exercício do Departamento de Estatística do Instituto de Ciências Exatas e Tecnológicas da Universidade Federal de Lavras torna pública a abertura das inscrições para a docência voluntária no Componente Curricular listado no quadro a seguir.

> O Chefe em exercício do Departamento de Estatística do Instituto de Ciências Exatas e Tecnológicas da Universidade Federal de Lavras torna pública a abertura das inscrições para a docência voluntária no Componente Curricular listado no quadro a seguir.
>
> [Ler o edital completo »](https://des.ufla.br/editais/134-edital-n-001-2026-docencia-voluntaria-des-1-sem-2026)

#### Edital Nº 003/2025 - Seleção de monitores remunerados para 2026
`oportunidades/posts/2025-11-27-edital-no-003-2025-selecao-de-monitores-remunerados-para-2026/index.qmd`

**Resumo (aparece no card):** O Chefe do Departamento de Estatística do Instituto de Ciências Exatas e Tecnológicas da Universidade Federal de Lavras torna pública a abertura das inscrições para a monitoria remunerada nos Componentes Curriculares listados no quadro a seguir.

> O Chefe do Departamento de Estatística do Instituto de Ciências Exatas e Tecnológicas da Universidade Federal de Lavras torna pública a abertura das inscrições para a monitoria remunerada nos Componentes Curriculares listados no quadro a seguir.
>
> [Ler o edital completo »](https://des.ufla.br/editais/133-edital-n-003-2025-selecao-de-monitores-remunerados-para-2026)

#### Edital PIBEEC 01/2025
`oportunidades/posts/2025-10-31-edital-pibeec-01-2025/index.qmd`

**Resumo (aparece no card):** A Pró-Reitoria de Extensão e Cultura da Universidade Federal de Lavras torna público este edital e convida os discentes desta instituição a participarem do Programa Institucional de Bolsas de Extensão, Esporte e Cultura, em conformidade com o que estabelece este edital e a Resolução CUNI Nº 028, ...

> A Pró-Reitoria de Extensão e Cultura da Universidade Federal de Lavras torna público este edital e convida os discentes desta instituição a participarem do Programa Institucional de Bolsas de Extensão, Esporte e Cultura, em conformidade com o que estabelece este edital e a Resolução CUNI Nº 028, ...
>
> [Ler o edital completo »](https://proeec.ufla.br/editais/47-teste-prog-proj/659-edital-pibeec-01-2025)

#### Edital PIBEC 07/2025
`oportunidades/posts/2025-09-09-edital-pibec-07-2025/index.qmd`

**Resumo (aparece no card):** A Pró-Reitoria de Extensão, Esporte e Cultura (PROEEC) da Universidade Federal de Lavras (UFLA), considerando o disposto, e em conformidade com a Resolução Normativa Nº 028 do Conselho Universitário, de 06 de junho de 2022, alterada pela Resolução Normativa nº 074, de 16 de março de 2023, torna p...

> A Pró-Reitoria de Extensão, Esporte e Cultura (PROEEC) da Universidade Federal de Lavras (UFLA), considerando o disposto, e em conformidade com a Resolução Normativa Nº 028 do Conselho Universitário, de 06 de junho de 2022, alterada pela Resolução Normativa nº 074, de 16 de março de 2023, torna p...
>
> [Ler o edital completo »](https://proeec.ufla.br/editais/programa-institucional-de-bolsas-de-extensao/648-edital-pibec-07-2025)


### Cursos e Eventos: posts publicados (4)


#### XVII Programa de Verão DES-ICET/UFLA 2026
`eventos/posts/2026-01-15-programa-de-verao-2026/index.qmd`

**Resumo (aparece no card):** Edição 2026 do tradicional Programa de Verão do Departamento de Estatística, com disciplinas e atividades de formação.

> O Programa de Verão do DES-ICET/UFLA chega à sua XVII edição, oferecendo
> disciplinas e atividades de aperfeiçoamento em Estatística durante o período
> de verão.
>
> [Saiba mais »](https://des.ufla.br/eventos/135-xvii-programa-de-verao-des-icet-ufla-2026)

#### XVII Encontro Mineiro de Estatística (MGEST) 2025
`eventos/posts/2025-11-05-xvii-encontro-mineiro-estatistica/index.qmd`

**Resumo (aparece no card):** Evento bienal que, desde 1999, reúne profissionais, docentes e estudantes da área de Estatística de Minas Gerais e do Brasil.

> O Encontro Mineiro de Estatística (MGEST) é um evento bienal que, desde 1999,
> reúne profissionais, docentes e estudantes para a troca de conhecimento e a
> divulgação de pesquisas na área de Estatística.
>
> [Saiba mais »](https://des.ufla.br/eventos/xvii-mgest-2025)

#### V Workshop em Data Science
`eventos/posts/2025-05-20-v-workshop-data-science/index.qmd`

**Resumo (aparece no card):** Workshop voltado à Ciência de Dados, com palestras e atividades sobre métodos estatísticos e aplicações.

> O Workshop em Data Science promove discussões sobre métodos estatísticos,
> aprendizado de máquina e aplicações de Ciência de Dados.
>
> [Saiba mais »](https://des.ufla.br/eventos/v-workshop-em-data-science)

#### Curso de Extensão: Introdução ao Software R
`eventos/posts/2024-09-01-curso-introducao-software-r/index.qmd`

**Resumo (aparece no card):** Curso de extensão de introdução ao R, ambiente livre para análise estatística e visualização de dados.

> Curso de extensão de introdução ao **R**, ambiente livre e gratuito amplamente
> utilizado para análise estatística, modelagem e visualização de dados.
>
> [Saiba mais »](https://des.ufla.br/cursos-e-palestras/125-curso-de-extensao-introducao-ao-software-r)





