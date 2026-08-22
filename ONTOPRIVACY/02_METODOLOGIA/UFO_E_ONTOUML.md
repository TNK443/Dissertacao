# UFO e OntoUML na OntoPrivacy

## 1. Por que utilizar uma ontologia de fundamentação

Uma ontologia de domínio pode conter ambiguidades quando todos os elementos são representados apenas como classes genéricas. A **Unified Foundational Ontology (UFO)** fornece categorias e meta-propriedades para analisar a natureza dos elementos do domínio.

Na OntoPrivacy, UFO é utilizada principalmente para responder questões como:

- o conceito fornece identidade ou a herda?
- a classificação é essencial ou contingente?
- o conceito depende de outro indivíduo ou de uma relação?
- uma associação deve ser representada por uma entidade relacional própria?

Neste repositório, “UFO” refere-se principalmente à **UFO-A**, responsável pelos aspectos estruturais do modelo.

## 2. Meta-propriedades centrais

### Identidade

Distingue tipos fundamentais que fornecem princípio de identidade daqueles que o herdam. `Pessoa Natural`, `Pessoa Jurídica` e `Dado` fornecem identidade; `Titular de DP` e `Dado Pessoal` a herdam.

### Rigidez

Distingue classificações essenciais de classificações contingentes. Uma pessoa não deixa de ser Pessoa Natural sem perder sua identidade; porém, pode deixar de desempenhar o papel de Titular em determinado contexto.

### Dependência

Explicita a necessidade de um portador ou de participantes relacionais. Finalidade depende de um TDP; Consentimento depende de Titular, Controlador, TDP e Finalidades.

## 3. OntoUML

**OntoUML** é uma linguagem de modelagem conceitual fundamentada em UFO. Ela especializa UML por meio de estereótipos com semântica ontológica explícita.

## 4. Estereótipos empregados

| Estereótipo | Natureza | Exemplos |
|---|---|---|
| `kind` | tipo fundamental | Dado; Pessoa Natural; Pessoa Jurídica |
| `subkind` | especialização rígida | Entidade Organizacional; Coleta; Anonimização |
| `role` | papel relacional de um único provedor de identidade | Dado Pessoal; Titular de DP; Dado Pseudonimizado |
| `roleMixin` | papel comum a entidades com identidades distintas | Controlador; Operador; Terceiro; Parte Interessada |
| `category` | abstração rígida para múltiplos tipos fundamentais | Agente Legal |
| `relator` | entidade relacional | Identificabilidade; TDP; Consentimento |
| `mode` | propriedade intrínseca dependente | Finalidade; Anonimidade |
| `collective` | coletivo de membros | Conjunto de Dados |

## 5. Relações empregadas

| Relação | Leitura na OntoPrivacy |
|---|---|
| `mediation` | TDP abrange Dados Pessoais; Identificabilidade identifica Titular |
| `material` | Dado Pessoal refere-se a Titular; Controlador instrui Operador |
| `characterization` | Finalidade caracteriza TDP; Anonimidade caracteriza Dado Anonimizado |
| `memberOf` | Dado integra Conjunto de Dados |

## 6. Os três `relators`

### Identificabilidade

Reifica a relação pela qual Dados Pessoais permitem identificar um Titular. Sua existência evita tratar “ser pessoal” apenas como atributo intrínseco do dado.

### Tratamento de Dados Pessoais

Reifica a situação na qual dados, participantes, operações e Finalidades estão relacionados. As operações específicas são `subkind`s desse relator.

### Consentimento

Reifica a manifestação do Titular perante Controladores em relação a um TDP e a Finalidades determinadas.

## 7. Conjuntos de generalização

- `{disjoint}` — subclasses mutuamente exclusivas;
- `{complete}` — subclasses cobrem integralmente o supertipo;
- `{overlapping}` — uma instância pode pertencer a mais de uma subclasse;
- `{incomplete}` — outras subclasses podem existir.

## 8. Limites assumidos

A versão atual mantém alguns aspectos para evolução futura, como relações de derivação semanticamente registradas, identificadores estáveis e implementação operacional. Esses limites não alteram o propósito conceitual da versão congelada.

## Referências principais

- GUIZZARDI, G. Ontological Foundations for Structural Conceptual Models. 2005.
- GUIZZARDI, G. et al. Towards Ontological Foundations for Conceptual Modeling: The Unified Foundational Ontology (UFO) Story. 2015.
- GUIZZARDI, G. et al. UFO: Unified Foundational Ontology. Applied Ontology, 2022.
- OntoUML Specification Documentation.
