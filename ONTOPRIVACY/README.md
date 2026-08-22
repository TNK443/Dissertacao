<div align="center">

# 🧠 OntoPrivacy — Ontologia de Privacidade de Dados

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

A **OntoPrivacy** é uma ontologia de referência de domínio, em nível conceitual, destinada a representar um núcleo selecionado de conceitos relacionados à **privacidade de dados pessoais**. A ontologia é fundamentada principalmente na **Lei Geral de Proteção de Dados Pessoais (LGPD)** e na **ABNT NBR ISO/IEC 29100:2020**, utiliza o **SABiO** como orientação metodológica, adota a **Unified Foundational Ontology (UFO)** como fundamentação ontológica e é representada em **OntoUML**.

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

## 🖼️ Modelo conceitual

<p align="center">
  <img src="./01_MODELO/OntoPrivacy_v2.png" alt="OntoPrivacy v2 — diagrama conceitual" width="1000">
</p>

> **Legenda acadêmica:** Ontologia de Privacidade de Dados — OntoPrivacy v2.  
> **Arquivo técnico:** `OntoPrivacy_v2.png`.

---

## 🔢 Inventário da versão final

| Elemento | Quantidade |
|---|---:|
| Conceitos | **43** |
| Relações | **21** |
| Generalizações | **36** |
| Conjuntos de generalização | **7** |
| Restrições próprias | **1** |
| Atributos | **1** |
| Questões de Competência | **7** |
| Cenários de validação | **14** |

---

## 🧭 Arquitetura conceitual

A leitura da OntoPrivacy é organizada por três `relators` centrais:

```mermaid
flowchart LR
    D["Dado"] --> DP["Dado Pessoal"]
    DP --> I["Identificabilidade\n<<relator>>"]
    I --> T["Titular de DP"]
    DP --> TDP["Tratamento de Dados Pessoais\n<<relator>>"]
    P["Partes interessadas\ne agentes"] --> TDP
    O["Operações de TDP"] --> TDP
    F["Finalidade\n<<mode>>"] --> TDP
    T --> C["Consentimento\n<<relator>>"]
    CTRL["Controlador"] --> C
    TDP --> C
    F --> C
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
│   ├── OntoPrivacy_v2.asta
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

| QC | Formulação objetiva |
|---|---|
| **QC1** | Quais dados são pessoais, sensíveis, pseudonimizados ou anonimizados, e em quais coleções estão organizados? |
| **QC2** | A quem cada dado pessoal se refere e como ocorre a identificação: direta ou indireta? |
| **QC3** | Quem participa do tratamento e qual papel desempenha? |
| **QC4** | Quais operações de tratamento são realizadas sobre os dados pessoais? |
| **QC5** | Para qual finalidade o tratamento é realizado, quem a define e a quem é informada? |
| **QC6** | Quem consente com qual tratamento, perante qual controlador e para quais finalidades? |
| **QC7** | Que dados resultam da anonimização ou pseudonimização e qual condição de identificação permanece? |

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
    AS --> EI["Estudo I — API Pix"]
    GERPD --> EII["Estudo II — Tibico"]
    V1 -->|evolução| V2["OntoPrivacy v2 — versão final"]
```

A pasta `OntoPrivacy/` documenta a versão final. As aplicações históricas permanecem nos diretórios [`../ANOTACAO_SEMANTICA/`](../ANOTACAO_SEMANTICA/) e [`../GERPD/`](../GERPD/).

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
