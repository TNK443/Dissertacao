# SABiO e SABiOx na construção da OntoPrivacy

## 1. SABiO

O **Systematic Approach for Building Ontologies (SABiO)** é uma abordagem de Engenharia de Ontologias orientada à construção sistemática de ontologias de domínio. A abordagem distingue ontologias de referência e ontologias operacionais e organiza atividades de desenvolvimento e apoio.

Na OntoPrivacy, o SABiO foi utilizado principalmente para estruturar:

1. **propósito e requisitos** — definição do domínio, do objetivo, dos usos pretendidos e das Questões de Competência;
2. **aquisição de conhecimento** — análise de legislação, normas, literatura e ontologias relacionadas;
3. **captura da conceituação** — seleção e harmonização dos conceitos;
4. **formalização** — representação em OntoUML de classes, relações, especializações, cardinalidades e restrições;
5. **avaliação** — verificação de cobertura das QCs, coerência estrutural e rastreabilidade;
6. **documentação** — modelo, catálogo, matrizes, cenários e decisões.

## 2. Questões de Competência

As Questões de Competência expressam perguntas que a ontologia deve ser capaz de representar e responder. Elas foram utilizadas para:

- delimitar o escopo;
- orientar a aquisição de conhecimento;
- justificar a inclusão de conceitos e relações;
- avaliar a cobertura do modelo.

A OntoPrivacy possui sete QCs canônicas, documentadas em `04_VALIDACAO/`.

## 3. SABiOx

O **SABiOx** estende e detalha o SABiO com uma perspectiva iterativa e incremental. Na pesquisa, ele apoiou a compreensão de que a ontologia foi refinada em sucessivos ciclos de análise, modelagem, revisão e documentação.

O uso de SABiOx não transforma a versão final em ontologia operacional. A OntoPrivacy permanece uma ontologia de referência conceitual.

## 4. Correspondência entre atividades e artefatos

| Atividade | Artefato no repositório |
|---|---|
| Propósito e requisitos | `ONTOPRIVACY.md` e Questões de Competência |
| Aquisição de conhecimento | `05_RASTREABILIDADE/MATRIZ_CONCEITO_FONTE_v2.*` |
| Captura e conceituação | Catálogo de Conceitos e Relações |
| Formalização | `01_MODELO/OntoPrivacy_v2.asta` e PNG |
| Avaliação | `04_VALIDACAO/` |
| Documentação | README, Catálogo, matrizes e Registro de Decisões |

## 5. Limite metodológico

O repositório documenta uma ontologia de referência. Não há, nesta versão, implementação integral em OWL, OCL, SHACL ou outra linguagem de raciocínio operacional.

## Referências principais

- FALBO, R. A. SABiO: Systematic Approach for Building Ontologies. 2014.
- AGUIAR, C. Z.; SOUZA, V. E. S. SABiOx: the Extended Systematic Approach for Building Ontologies. 2024.
