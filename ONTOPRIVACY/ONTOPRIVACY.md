# OntoPrivacy — Descrição conceitual e documental

## 1. Identificação

- **Nome:** OntoPrivacy — Ontologia de Privacidade de Dados.
- **Natureza:** ontologia de referência de domínio.
- **Nível:** conceitual.
- **Versão acadêmica final:** OntoPrivacy v2.
- **Arquivos técnicos congelados:** `OntoPrivacy_v2.asta` e `OntoPrivacy_v2.png`.
- **Domínio:** privacidade de dados pessoais.
- **Contexto de aplicação:** enriquecimento semântico de artefatos de Engenharia de Software.
- **Fontes centrais:** LGPD e ABNT NBR ISO/IEC 29100:2020.
- **Método principal:** SABiO, com apoio iterativo de SABiOx.
- **Fundamentação ontológica:** UFO, principalmente UFO-A.
- **Linguagem de modelagem:** OntoUML.

## 2. Propósito

A OntoPrivacy foi desenvolvida para fornecer uma conceituação compartilhada sobre elementos essenciais da privacidade de dados. Seu propósito é reduzir ambiguidades entre terminologia normativa, organizacional e técnica, permitindo que conceitos do domínio sejam relacionados a artefatos de Engenharia de Software.

A ontologia apoia, especialmente:

1. a identificação e classificação de dados relacionados a pessoas naturais;
2. a representação de titulares, controladores, operadores, terceiros e outras partes interessadas;
3. a caracterização de situações e operações de tratamento;
4. a representação de Finalidades e Consentimento;
5. a distinção entre anonimização, pseudonimização e seus resultados;
6. o enriquecimento semântico de descrições OpenAPI;
7. a organização e rastreabilidade de aspectos de privacidade em Engenharia de Requisitos.

## 3. Escopo e não objetivos

A OntoPrivacy representa um **núcleo selecionado** do domínio. Ela não busca:

- reproduzir integralmente a LGPD;
- determinar Base Legal;
- decidir licitude;
- certificar conformidade;
- avaliar a validade jurídica do Consentimento;
- modelar exaustivamente direitos, obrigações, sanções, riscos, controles e políticas;
- substituir análise jurídica, técnica, organizacional ou de segurança;
- funcionar, nesta versão, como ontologia operacional completa ou raciocinador automático.

## 4. Evolução e política de versões

### OntoPrivacy v1

A OntoPrivacy v1 corresponde à versão inicial desenvolvida e aplicada no trabalho publicado por Mori Junior et al. (2025). Ela é a base semântica histórica:

- da abordagem de anotação semântica;
- da especificação anotada da API Pix;
- do Privacy Finder;
- do GERPD v1.0;
- dos Estudos I e II.

### OntoPrivacy v2

A OntoPrivacy v2 é a evolução conceitual final apresentada na dissertação. Ela incorpora, entre outros refinamentos:

- `Dado` como `kind`;
- `Dado Pessoal` como `role`;
- `Identificabilidade` como `relator`;
- `Dado Pseudonimizado` como especialização de Dado Pessoal;
- `Finalidade` como `mode` do Tratamento de Dados Pessoais;
- `Agente Legal` como `category`;
- revisão da classificação de participantes, operações e estruturas de dados;
- remoção de conceitos intermediários como Informação, Ator, TDP Autorizado, Ator Autorizado e Ator Desautorizado.

A v2 não foi aplicada retroativamente aos estudos.

## 5. Fontes de conhecimento

### Fontes normativas principais

- **Lei nº 13.709/2018 — LGPD:** ancoragem normativa brasileira, incluindo dados pessoais, dados sensíveis, dados anonimizados, titular, agentes, Consentimento, Finalidade, tratamento e operações.
- **ABNT NBR ISO/IEC 29100:2020:** complementação técnica e terminológica, incluindo atores, papéis, tratamento, identificabilidade, anonimização e pseudonimização.

### Fundamentação metodológica e ontológica

- **SABiO:** processo sistemático para construção de ontologias de domínio.
- **SABiOx:** detalhamento iterativo e incremental do ciclo de desenvolvimento.
- **UFO:** categorias ontológicas para análise de identidade, rigidez, dependência e relações.
- **OntoUML:** linguagem de modelagem conceitual fundamentada em UFO.

### Comparação e reúso conceitual

Foram consideradas contribuições de COPri v.2, IEEE Std 7007-2021, GDPRtEXT, GConsent, PrOnto, DPV, DICON/PCO, POWoT e Linked USDL Privacy. O Mapeamento Sistemático apoiou a identificação do estado da arte, dos modelos relacionados e das lacunas de aplicação em Engenharia de Software.

## 6. Desenvolvimento com SABiO

O SABiO orienta a construção de ontologias de domínio de forma sistemática. Na OntoPrivacy, o processo foi organizado nos seguintes movimentos:

1. **definição do propósito e dos requisitos:** delimitação do domínio, dos usos pretendidos e das Questões de Competência;
2. **aquisição de conhecimento:** análise de leis, normas, literatura, ontologias e vocabulários relacionados;
3. **captura e conceituação:** seleção, comparação, harmonização e organização dos conceitos;
4. **formalização:** representação de classes, relações, generalizações, cardinalidades e restrições em OntoUML;
5. **avaliação:** verificação da cobertura das QCs, da coerência estrutural e da rastreabilidade das fontes;
6. **documentação:** elaboração do modelo, catálogo, matrizes, cenários e registros de decisão.

O SABiOx foi utilizado como apoio para compreender o desenvolvimento como processo iterativo e incremental, com revisões sucessivas dos artefatos. A OntoPrivacy final, entretanto, permanece caracterizada como ontologia de referência conceitual.

## 7. Fundamentação em UFO

A UFO é uma ontologia de fundamentação utilizada para analisar a natureza dos elementos representados. Nesta pesquisa, “UFO” refere-se principalmente à **UFO-A**, responsável pelos aspectos estruturais do modelo conceitual.

Três noções são centrais:

- **identidade:** permite distinguir tipos que fornecem um princípio de identidade daqueles que apenas o herdam;
- **rigidez:** distingue classificações essenciais de papéis ou fases contingentes;
- **dependência:** explicita se uma entidade existe independentemente, depende de um portador ou depende de participantes relacionais.

### Estereótipos utilizados

| Estereótipo | Interpretação | Exemplos na OntoPrivacy |
|---|---|---|
| `kind` | tipo fundamental que fornece identidade | Dado, Pessoa Natural, Pessoa Jurídica |
| `subkind` | especialização rígida que herda identidade | Entidade Organizacional, Operação de TDP, Coleta |
| `role` | papel antirrígido dependente de relação | Dado Pessoal, Titular de DP, Dado Pseudonimizado |
| `roleMixin` | papel comum a entidades com diferentes identidades | Parte Interessada, Controlador, Operador, Terceiro |
| `category` | tipo rígido não sortal que agrega diferentes tipos fundamentais | Agente Legal |
| `relator` | entidade relacional dependente de múltiplos participantes | Identificabilidade, TDP, Consentimento |
| `mode` | propriedade intrínseca dependente de um portador | Finalidade, Anonimidade |
| `collective` | totalidade composta por membros uniformes | Conjunto de Dados |

### Relações utilizadas

| Relação | Função |
|---|---|
| `mediation` | liga um `relator` aos participantes de que depende |
| `material` | representa uma relação direta fundamentada por uma estrutura relacional |
| `characterization` | liga um `mode` ao indivíduo que ele caracteriza |
| `memberOf` | representa pertencimento de um membro a um coletivo |

## 8. Arquitetura centrada em três `relators`

### 8.1 Identificabilidade

`Identificabilidade <<relator>>` explica por que um Dado desempenha o papel de Dado Pessoal e a qual Titular se refere.

Principais relações:

- baseia-se em um ou mais Dados Pessoais;
- identifica um Titular de DP;
- fundamenta a leitura “Dado Pessoal refere-se a Titular”.

Especializações:

- `Identificabilidade Direta <<subkind>>`;
- `Identificabilidade Indireta <<subkind>>`.

A avaliação da identificabilidade pressupõe um contexto delimitado e meios razoavelmente disponíveis. Esses meios não são modelados detalhadamente nesta versão.

### 8.2 Tratamento de Dados Pessoais

`Tratamento de Dados Pessoais <<relator>>` representa uma situação relacional na qual Dados Pessoais são submetidos a uma Operação ou a um Conjunto de Operações.

Principais elementos:

- abrange Dados Pessoais;
- envolve Partes Interessadas;
- possui Controlador responsável;
- pode ser realizado por Operador;
- é orientado por uma ou mais Finalidades.

Especializações:

- `Operação de TDP <<subkind>>`;
- `Conjunto de Operações de TDP <<subkind>>`.

Operações representadas:

- Alteração;
- Anonimização;
- Armazenamento;
- Coleta;
- Consulta;
- Disponibilização;
- Divulgação;
- Exclusão;
- Pseudonimização;
- Recuperação.

As operações são `subkind`s porque herdam o princípio de identidade do relator TDP, sem introduzir nova identidade relacional.

### 8.3 Consentimento

`Consentimento <<relator>>` representa a manifestação do Titular em relação a determinado TDP e Finalidades.

Principais relações:

- é manifestado por um Titular de DP;
- é dirigido a um ou mais Controladores;
- possui exatamente um TDP em seu escopo;
- refere-se a uma ou mais Finalidades.

Nem todo TDP possui Consentimento. A presença de uma instância de Consentimento não implica validade jurídica, Base Legal suficiente ou conformidade.

## 9. Dados e coleções

### Dado e Dado Pessoal

`Dado <<kind>>` fornece identidade aos elementos informacionais. `Dado Pessoal <<role>>` é o papel assumido por um Dado quando participa de uma relação de Identificabilidade com um Titular.

### Dado Pseudonimizado

`Dado Pseudonimizado <<role>>` especializa Dado Pessoal. Todo Dado Pseudonimizado deve participar de pelo menos uma Identificabilidade Indireta.

### Dado Anonimizado e Anonimidade

`Dado Anonimizado <<role>>` é resultado de Anonimização e é caracterizado por `Anonimidade <<mode>>` no contexto considerado.

### Dados sensíveis

`DP Sensível <<role>>` é abstrato e possui as categorias representadas:

- DP Biométrico;
- DP Etnia;
- DP Político;
- DP Religião;
- DP Saúde.

O conjunto é deliberadamente sobreposto e incompleto.

### Coleções

- `Conjunto de Dados <<collective>>` organiza Dados;
- `Banco de Dados DP <<subkind>>` especializa Conjunto de Dados e organiza Dados Pessoais.

## 10. Agentes e papéis

### Agente Legal

`Agente Legal <<category>>` reúne `Pessoa Natural <<kind>>` e `Pessoa Jurídica <<kind>>`.

### Organização

`Entidade Organizacional <<subkind>>` especializa Pessoa Jurídica, com `Agência` e `Autoridade Pública` como especializações.

### Papéis

- `Parte Interessada na Privacidade <<roleMixin>>`;
- `Agente de Tratamento <<roleMixin>>`;
- `Controlador <<roleMixin>>`;
- `Operador <<roleMixin>>`;
- `Terceiro <<roleMixin>>`;
- `Titular de DP <<role>>`.

Essas classificações expressam que os papéis dependem do contexto e não constituem a identidade essencial da pessoa ou organização.

## 11. Finalidade

`Finalidade <<mode>>` expressa o propósito determinado que orienta e delimita um TDP.

Relações principais:

- TDP é orientado por Finalidade;
- Controlador define Finalidade;
- Finalidade é informada ao Titular;
- Consentimento refere-se a Finalidade.

Finalidade e Base Legal são conceitos distintos. A OntoPrivacy representa Finalidade, mas mantém Base Legal fora do núcleo conceitual.

## 12. Anonimização e pseudonimização

A ontologia distingue operação, resultado e condição:

```text
Anonimização -> Dado Anonimizado -> Anonimidade
Pseudonimização -> Dado Pseudonimizado -> Identificabilidade Indireta
```

Essa separação impede que processo, dado resultante e propriedade sejam tratados como sinônimos.

## 13. Questões de Competência

| QC | Formulação objetiva |
|---|---|
| QC1 | Quais dados são pessoais, sensíveis, pseudonimizados ou anonimizados, e em quais coleções estão organizados? |
| QC2 | A quem cada dado pessoal se refere e como ocorre a identificação: direta ou indireta? |
| QC3 | Quem participa do tratamento e qual papel desempenha? |
| QC4 | Quais operações de tratamento são realizadas sobre os dados pessoais? |
| QC5 | Para qual finalidade o tratamento é realizado, quem a define e a quem é informada? |
| QC6 | Quem consente com qual tratamento, perante qual controlador e para quais finalidades? |
| QC7 | Que dados resultam da anonimização ou pseudonimização e qual condição de identificação permanece? |

## 14. Avaliação conceitual

A versão final foi documentada e avaliada por meio de:

- Catálogo OntoPrivacy;
- Matriz Conceito–Fonte;
- Matriz QC–Conceito–Relação;
- sete cenários positivos;
- sete cenários negativos ou limítrofes;
- inspeção estrutural do modelo;
- registro de limites e decisões.

Resultados documentados:

- 43 de 43 conceitos mobilizados por pelo menos uma QC;
- 21 de 21 relações mobilizadas por pelo menos uma QC;
- sete QCs conceitualmente respondíveis;
- nenhum cenário exigiu alteração silenciosa do modelo.

## 15. Limites da avaliação

A avaliação é conceitual e documental. Ela não:

- executa consultas sobre uma base de instâncias;
- usa raciocinador formal;
- comprova completude do domínio;
- avalia conformidade jurídica;
- mede efetividade técnica de anonimização;
- valida o ciclo de vida do Consentimento;
- determina papéis sem evidência contextual.

## 16. Aplicação em Engenharia de Software

A OntoPrivacy oferece uma base semântica para duas formas de enriquecimento:

### Anotação semântica de OpenAPI

A versão histórica v1 foi utilizada para associar elementos técnicos de uma especificação OpenAPI a conceitos de privacidade por meio de extensões `x-`.

### Engenharia de Requisitos

A versão histórica v1 fundamentou o GERPD v1.0, que organiza dados, participantes, operações, finalidades, requisitos e rastreabilidade.

A versão final v2 amplia e refina a conceituação, mas não reclassifica retroativamente os estudos.

## 17. Artefatos relacionados

- arquivo editável em Astah;
- diagrama PNG;
- catálogo em Markdown e Excel;
- Matriz Conceito–Fonte;
- Questões de Competência;
- matriz de cobertura;
- cenários e relatório de validação;
- Registro de Decisões;
- documentação metodológica.

## 18. Citação da versão histórica publicada

MORI JUNIOR, D.; NARDI, J. C.; RUY, F. B.; TEIXEIRA, G. F. Apoio na adoção da Lei Geral de Proteção de Dados Pessoais por meio de anotações semânticas em descrições de serviços Web. *Em Questão*, v. 31, e-139608, 2025. DOI: 10.1590/1808-5245.31.139608.
