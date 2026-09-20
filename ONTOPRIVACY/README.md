<div align="center">

# 🧠 OntoPrivacy - Ontologia de Privacidade de Dados

**Ontologia de referência de domínio para representação conceitual de privacidade de dados e enriquecimento semântico de artefatos de Engenharia de Software**

![Versão acadêmica](https://img.shields.io/badge/vers%C3%A3o%20acad%C3%AAmica-v2-1f6feb?style=flat-square)
![Status](https://img.shields.io/badge/status-congelada-2ea043?style=flat-square)
![Conceitos](https://img.shields.io/badge/conceitos-43-0f766e?style=flat-square)
![Relações](https://img.shields.io/badge/rela%C3%A7%C3%B5es-21-0f766e?style=flat-square)
![Método](https://img.shields.io/badge/m%C3%A9todo-SABiO-d97706?style=flat-square)
![Fundamentação](https://img.shields.io/badge/fundamenta%C3%A7%C3%A3o-UFO%20%7C%20OntoUML-6f42c1?style=flat-square)

</div>

---

## 📌 Sobre a OntoPrivacy

A **OntoPrivacy** é uma **ontologia de referência de domínio**, em nível conceitual, destinada a representar um núcleo selecionado de conceitos relacionados à **privacidade de dados pessoais**. A ontologia é fundamentada principalmente na **Lei Geral de Proteção de Dados Pessoais (LGPD)** e na **ABNT NBR ISO/IEC 29100:2020**, utiliza o **SABiO** como orientação metodológica, adota a **Unified Foundational Ontology (UFO)** como fundamentação ontológica e é representada em **OntoUML**.

Seu propósito é fornecer uma conceituação compartilhada para apoiar:

- comunicação e aprendizagem sobre o domínio;
- redução de ambiguidades jurídico-técnicas;
- organização e rastreabilidade de conceitos de privacidade;
- enriquecimento semântico de descrições OpenAPI;
- apoio semântico à Engenharia de Requisitos de Privacidade de Dados.

> [!IMPORTANT]
> A OntoPrivacy não representa integralmente a LGPD, não determina Base Legal, não avalia licitude, não certifica conformidade e não substitui análise jurídica, técnica ou organizacional.

---

## 🏷️ Nota de versionamento

Na dissertação, a versão final congelada é denominada **OntoPrivacy v2**. Os arquivos técnicos preservam o identificador interno `v2`:

- `OntoPrivacy_v2.asta`;
- `OntoPrivacy_v2.png`.

A **OntoPrivacy v1** é a versão histórica publicada em Mori Junior et al. (2025) e efetivamente utilizada na abordagem de anotação, no GERPD v1.0 e nos Estudos I e II. A versão v2 é uma evolução conceitual posterior e não foi aplicada retroativamente.

Leia a política completa em [`VERSIONAMENTO.md`](./VERSIONAMENTO.md).

---

## 🌐 Modelo Conceitual

<p align="center">
  <img src="./01_MODELO/OntoPrivacy_v2.png" alt="OntoPrivacy v2 - Diagrama Conceitual" width="1000">
</p>

> **Legenda acadêmica:** Ontologia de Privacidade de Dados - OntoPrivacy v2.  
> **Arquivo técnico:** `OntoPrivacy_v2.png`.

---

## 🔢 Inventário da versão final

| Elemento | Quantidade |
|---|:---:|
| Conceitos | **43** |
| Relações | **21** |
| Generalizações | **36** |
| Conjuntos de generalização | **07** |
| Restrições próprias | **01** |
| Atributos | **01** |
| Questões de Competência | **07** |
| Cenários de validação | **14** |

---

## 🧭 Arquitetura conceitual

A leitura da OntoPrivacy é organizada por três `relators` centrais:

[![](https://mermaid.ink/img/pako:eNp9U02P2jAQ_SuRVyu1UmAT8gG4CIlCkZC2AlU5telhFhtwm9jIdrR0Eb-nh5576m33j3ViEg5taXLJTN6892bGPpK1YpxQsinU43oH2uY6lx4-t7fePWiQX4B6ky2Xlhvv1Yobo8DcLfUWpHiCl-8vP7l53dasCzBmxjee5gVYpb2NKAp6M4_eJfPEN1arr5zepJPw7XDShJ1HweyO9vYHf60KpelNOKnfNzVnyzv7lJMZMJWTz16nM_ZmqybhnQ0V-OOCXTnIAhEjMX7-0Vh5_jW6E-M8l6OH8YJhO2Ij1vAgCsGAcUwiBaW0QbdkC8eVIVcmbFWA9hhHhb_lMmfpmmCmwUKJosrVo3HTOBfmmnTNt8J94NgFDl8jHBgYJOQenPfRjgPF26olVi33XDebqeUy5_dP4Ly1W-L-L17nQsJ5Iv8oyVxi-p8-p0qaerSu1WuNTbMP98iBWDwABc5Ct1rTi1Iz1Utifg6JT7ZaMEKtrrhPSq5LqENyrGE5sTteonOKn5qz6tBxRyonuTxh6R7kR6XKtlqrarsjdAOFwajaM7B8JmCrobxkNZeM66mqpCU0TIPYJ5wJbOb9-da4y-OYCT2SA6G9XtwNo2CYpuEgTXpRjBXfCO2H3ShIwjDux2kwjPrJySdPzkvQHaSD_jAZBnEvidIwHJx-A5wqJ9A?type=png)](https://mermaid.live/edit#pako:eNp9U02P2jAQ_SuW0UqtFNiEfAAuQqJQJKStQFVObXqYxQbcJjGyHS27iN_TQ8899bb7xzr5olJbmlwykzfvvRmPT3SjuKCMJjrJt6l62OxB2zIg-NzckDvQkH8BRqY7kVthyKu1MEaBuV3pHeTyCV6-vfwQ5nVbs0nBmLnYEi1SsEqTrUxT1ln478JF6Bir1VfBOtHUezuaNmH3QXK7Z_3D0dmoVGnW8abl-6bkbHnnnxI6B64S-pl0uxMyXzcJUhtK8ccFu64gS0SM5eT5e2Pl-ef4Vk6SJB_fT5Yc25FbuYF7mUoOXGASKRhjDbolW1ZcMXLF0hYpaMIFKvwtF1eWrgnGGixkKKqqejRuGufSXJMu-dZ4Hjh2icPXCAcOBgkFgfo82nGgeFu1wqrVQejmZEq5uPL7J3DR2s1wBy5eFzKHeiL_KImrxOw_fc5UbsrRVq1ea2wWf7hDDsTiAqQ4C91qzS5KzVQviUUdUofutOSUWV0Ih2ZCZ1CG9FTCEmr3IkPnDD-14MWxW61UQpP8jKUHyD8qlbXVWhW7PWVbSA1GxYGDFXMJOw2_ISLnQs9UkVvKvMh1HSq4xF7e1xenuj8VMWUneqSs3w96nu-OosgbRmHfDwKHPlI28Hq-G3peMAgid-QPwrNDnyorbm8YDQejcOQG_dCPPG94_gUioCkZ)

```mermaid
flowchart
    %% Laranja: Agentes (Pessoas/Organizações)
    classDef relator fill:#F3E5F5,stroke:#6A1B9A,stroke-width:2px,color:#1A1A1A;

    D["Dado"] --> DP["Dado Pessoal"]
    DP --> I["<i>«relator»</i>\n<b>Identificabilidade<b>"]:::relator
    I --> T["Titular de DP"]
    DP --> TDP["<i>«relator»</i>\n<b>Tratamento de Dados Pessoais<b>"]:::relator
    P["Partes interessadas\ne agentes"] --> TDP
    O["Operações de TDP"] --> TDP
    F["<i>«mode»</i>\nFinalidade"] --> TDP
    T --> C["<i>«relator»</i>\n<b>Consentimento<b>"]:::relator
    CTRL["Controlador"] --> C
    TDP --> C
    F --> C
```

```mermaid
flowchart LR
    %% --------------------------------------------------------
    %% PALETA DE CORES LÓGICA E ELEGANTE (MATERIAL DESIGN)
    %% --------------------------------------------------------
    %% Azul: Objetos passivos e dados
    classDef dado fill:#E3F2FD,stroke:#1565C0,stroke-width:2px,color:#1A1A1A;
    
    %% Ciano: Subtipos e operações
    classDef subkind fill:#E0F7FA,stroke:#00838F,stroke-width:2px,color:#1A1A1A;
    
    %% Laranja: Agentes (Pessoas/Organizações)
    classDef ator fill:#FFF3E0,stroke:#E65100,stroke-width:2px,color:#1A1A1A;
    
    %% Verde: Modos e Finalidades
    classDef mode fill:#E8F5E9,stroke:#2E7D32,stroke-width:2px,color:#1A1A1A;
    
    %% Roxo: Relatores (O "contrato" ou elo que une as partes)
    classDef relator fill:#F3E5F5,stroke:#6A1B9A,stroke-width:2px,color:#1A1A1A;

    %% --------------------------------------------------------
    %% AGRUPAMENTO 1: IDENTIFICABILIDADE
    %% --------------------------------------------------------
    subgraph G1 ["<b>1. IDENTIFICABILIDADE</b>&nbsp;"]
        D("<i>«kind»</i>\n<b>Dado</b>"):::dado
        DP("<i>«role»</i>\n<b>Dado Pessoal</b>"):::dado
        I("<b>Identificabilidade</b>\n<i>«relator»</i>"):::relator
        
        %% Sub-tipos de Identificabilidade
        IDIR("<i>«subkind»</i>\n<b>Direta</b>"):::subkind
        IIND("<i>«subkind»</i>\n<b>Indireta</b>"):::subkind
        
        T("<i>«role»</i>\n<b>Titular de DP</b>"):::ator
        
        %% Conexões Internas do G1
        D -->DP
        DP -->|possibilita a| I
        I -->|pode ser| IDIR
        I -->|pode ser| IIND
        I -->|refere-se ao| T
    end

    %% --------------------------------------------------------
    %% AGRUPAMENTO 2: TRATAMENTO DE DADOS PESSOAIS
    %% --------------------------------------------------------
    subgraph G2 ["<b>2. TRATAMENTO DE DADOS PESSOAIS (TDP)</b>&nbsp;"]
        TDP("<i>«relator»</i>\n<b>Tratamento de Dados Pessoais (TDP)</b>"):::relator
        
        O("<i>«subkind»</i>\n<b>Operação de TDP</b>"):::subkind
        CO("<i>«subkind»</i>\n<b>Conj. de Operações</b>"):::subkind
        
        P("<i>«rolemixin»</i>\n<b>Partes e Agentes</b>"):::ator
        CTRL("<i>«rolemixin»</i>\n<b>Controlador</b>"):::ator
        OPR("<i>«rolemixin»</i>\n<b>Operador</b>"):::ator
        
        F("<i>«mode»</i>\n<b>Finalidade</b>"):::mode
        
        %% Conexões Internas do G2
        O -->|compõe um| CO
        O -->|é abrangida pelo| TDP
        CO -->|é abrangido pelo| TDP
        
        CTRL -.->|é tipo de| P
        OPR -.->|é tipo de| P
        P -->|envolvidas no| TDP
        
        TDP -->|possui uma ou mais| F
    end

    %% --------------------------------------------------------
    %% AGRUPAMENTO 3: CONSENTIMENTO
    %% --------------------------------------------------------
    subgraph G3 ["<b>3. CONSENTIMENTO</b>&nbsp;"]
        C("<i>«relator»</i>\n<b>Consentimento</b>"):::relator
    end

    %% --------------------------------------------------------
    %% CONEXÕES ENTRE OS AGRUPAMENTOS (CROSS-LINKS)
    %% --------------------------------------------------------
    
    %% Ligação Dado Pessoal -> TDP
    DP -->|é abrangido pelo| TDP
    
    %% Ligações do Consentimento
    T -->|manifesta o| C
    C -->|é dirigido ao| CTRL
    C -->|é relativo ao| TDP
    C -->|determina as| F

    %% --------------------------------------------------------
    %% ESTILIZAÇÃO DAS CAIXAS (CLEAN DESIGN)
    %% --------------------------------------------------------
    %% Fundos neutros (cinza super claro) para não ofuscar os nós coloridos
    style G1 fill:#F8F9FA,stroke:#B0BEC5,stroke-width:2px,color:#37474F,stroke-dasharray: 5 5,rx:10,ry:10
    style G2 fill:#F8F9FA,stroke:#B0BEC5,stroke-width:2px,color:#37474F,stroke-dasharray: 5 5,rx:10,ry:10
    style G3 fill:#F8F9FA,stroke:#B0BEC5,stroke-width:2px,color:#37474F,stroke-dasharray: 5 5,rx:10,ry:10
```

### 1. Identificabilidade

Explica por que um `Dado` desempenha o papel de `Dado Pessoal` e a qual `Titular de DP` ele se refere. Pode ser **Direta** ou **Indireta**.

### 2. Tratamento de Dados Pessoais

Representa a situação relacional na qual `Dados Pessoais` são abrangidos por uma `Operação de TDP` ou por um `Conjunto de Operações`, envolvendo `Partes Interessadas`, `Controladores`, `Operadores` e `Finalidades`.

### 3. Consentimento

Representa a manifestação do `Titular de DP`, dirigida a um ou mais `Controladores`, relativa a um `TDP` e a `Finalidades` determinadas. A existência de `Consentimento` no modelo não implica validade jurídica ou licitude.

Leia a descrição completa em [`ONTOPRIVACY.md`](./ONTOPRIVACY.md).

---

## 🗂️ Estrutura deste diretório

```text
ONTOPRIVACY/
├── README.md
├── ONTOPRIVACY.md
├── VERSIONAMENTO.md
├── CHANGELOG.md
├── 01_MODELO/
│   ├── README.md
│   └── OntoPrivacy_v2.png
├── 02_METODOLOGIA/
│   ├── README.md
│   ├── SABIO_E_SABIOX.md
│   └── UFO_E_ONTOUML.md
├── 03_CATALOGO/
│   ├── README.md
│   ├── CATALOGO_ONTOPRIVACY_v2.xlsx
│   ├── CATALOGO_CONCEITOS_ONTOPRIVACY_v2.md
│   ├── CATALOGO_RELACOES_ONTOPRIVACY_v2.md
│   └── CATALOGO_ELEMENTOS_COMPLEMENTARES_v2.md
├── 04_VALIDACAO/
│   ├── README.md
│   ├── QUESTOES_COMPETENCIA_ONTOPRIVACY_v2.md
│   ├── MATRIZ_QC_CONCEITO_RELACAO_v2.md
│   ├── MATRIZ_COBERTURA_QC_v2.xlsx
│   ├── CENARIOS_VALIDACAO_ONTOPRIVACY_v2.md
│   ├── RELATORIO_VALIDACAO_CONCEITUAL_v2.md
│   └── LIMITES_ESCOPO_QCS_v2.md
├── 05_RASTREABILIDADE/
│   ├── README.md
│   ├── MATRIZ_CONCEITO_FONTE_v2.xlsx
│   ├── MATRIZ_CONCEITO_FONTE_v2.md
│   └── REGISTRO_DECISOES_ONTOPRIVACY_v2.md
├── 06_HISTORICO/
│   ├── README.md
│   └── OntoPrivacy_v1.png
└── 07_REFERENCIAS/
    └── REFERENCIAS.md
```

---

## 🧩 Navegação rápida

| Diretório / arquivo | Conteúdo | Quando consultar |
|---|---|---|
| [`ONTOPRIVACY.md`](./ONTOPRIVACY.md) | descrição acadêmica detalhada | para compreender propósito, conceitos, relações e limites |
| [`01_MODELO/`](./01_MODELO/) | ASTA e PNG canônicos | para abrir ou visualizar o modelo |
| [`02_METODOLOGIA/`](./02_METODOLOGIA/) | SABiO, SABiOx, UFO e OntoUML | para compreender método e fundamentação |
| [`03_CATALOGO/`](./03_CATALOGO/) | catálogo de conceitos, relações e elementos | para consultar definições e classificações |
| [`04_VALIDACAO/`](./04_VALIDACAO/) | QCs, cenários e cobertura | para examinar a avaliação conceitual |
| [`05_RASTREABILIDADE/`](./05_RASTREABILIDADE/) | fontes e decisões | para rastrear a origem e a governança dos elementos |
| [`06_HISTORICO/`](./06_HISTORICO/) | OntoPrivacy v1 e evolução | para compreender a versão aplicada nos estudos |
| [`07_REFERENCIAS/`](./07_REFERENCIAS/) | referências bibliográficas | para citação e aprofundamento |

---

## ✅ Questões de Competência

| QC | Questões de Competência | Dimensão |
|:---:|---|:---:|
| **QC1** | Quais dados são pessoais, sensíveis, pseudonimizados ou anonimizados? | Dados e Classificação |
| **QC2** | A quem cada dado pessoal se refere e como ocorre a identificação: direta ou indireta? | Titular e Identificabilidade |
| **QC3** | Quem participa do tratamento e qual papel desempenha? | Participantes e Papéis |
| **QC4** | Quais operações de tratamento são realizadas sobre os dados pessoais? | Tratamento, Dados e Operações |
| **QC5** | Para qual finalidade o tratamento é realizado, quem a define e a quem é informada? | Finalidade e Responsabilidade |
| **QC6** | Quem consente com qual tratamento, perante qual controlador e para quais finalidades? | Consentimento |
| **QC7** | Que dados resultam da anonimização ou pseudonimização e qual condição de identificação permanece? | Operação e condições resultantes |

As versões formais e o mapeamento completo estão em [`04_VALIDACAO/`](./04_VALIDACAO/).

---

## 🔬 Avaliação conceitual

A avaliação da OntoPrivacy foi conduzida por meio de:

- catálogo de conceitos e relações;
- matriz de rastreabilidade Conceito–Fonte;
- análise de cobertura das sete QCs;
- sete cenários positivos;
- sete cenários negativos ou limítrofes;
- inspeção da mobilização dos 43 conceitos e das 21 relações.

O resultado indica que as sete QCs são conceitualmente respondíveis. Essa avaliação é **conceitual e documental**: não corresponde a validação jurídica, prova de completude do domínio ou execução de raciocinador formal.

---

## 🔗 Relação com os demais artefatos

```mermaid
flowchart TD
    V1["OntoPrivacy v1"] --> AS["ANOTACAO_SEMANTICA"]
    V1 --> GERPD["GERPD v1.0"]
    AS --> EI["Estudo I: API Pix"]
    GERPD --> EII["Estudo II: Tibico"]
    V1 -->|evolução| V2["OntoPrivacy v2\n(Versão Final)"]
```

A pasta `ONTOPRIVACY/` documenta a versão final. As aplicações históricas permanecem nos diretórios [`../ANOTACAO_SEMANTICA/`](../ANOTACAO_SEMANTICA/) e [`../GERPD/`](../GERPD/).

---

## 📖 Ordem recomendada de leitura

1. `README.md`;
2. `ONTOPRIVACY.md`;
3. `02_METODOLOGIA/SABIO_E_SABIOX.md`;
4. `02_METODOLOGIA/UFO_E_ONTOUML.md`;
5. `03_CATALOGO/README.md`;
6. `04_VALIDACAO/README.md`;
7. `VERSIONAMENTO.md`.

---

## 📚 Publicação relacionada à versão inicial

MORI JUNIOR, D.; NARDI, J. C.; RUY, F. B.; TEIXEIRA, G. F. **Apoio na adoção da Lei Geral de Proteção de Dados Pessoais por meio de anotações semânticas em descrições de serviços Web**. *Em Questão*, v. 31, e-139608, 2025. DOI: `10.1590/1808-5245.31.139608`.

---

<div align="center">

**OntoPrivacy · Ontologia de Privacidade de Dados**  
**Conceitos · Privacidade de Dados · LGPD · ISO/IEC 29100 · Engenharia de Software**

*`Material complementar de pesquisa acadêmica | versão 1.0, agosto de 2026.`*

</div>
