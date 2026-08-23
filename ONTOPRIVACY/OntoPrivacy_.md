# Informações para Repositório GitHub - OntoPrivacy
# 1. Diagnóstico executivo

A OntoPrivacy v2 apresenta uma **estrutura conceitual madura, delimitada e coerente com seu posicionamento como ontologia de referência de domínio**. Seu principal mérito é representar o domínio por meio de três estruturas relacionais centrais:

1. `Identificabilidade <<relator>>`;
2. `Tratamento de Dados Pessoais <<relator>>`;
3. `Consentimento <<relator>>`.

Esses três elementos organizam, respectivamente:

* a relação entre o Dado Pessoal e o Titular;
* a situação na qual os dados são submetidos a operações por participantes que desempenham papéis específicos;
* a manifestação do Titular perante o Controlador em relação a um TDP e às suas Finalidades.

A inclusão de `Finalidade <<mode>>` como propriedade dependente do TDP fortalece consideravelmente a estrutura. A Finalidade deixa de ser restrita ao Consentimento e passa a representar o **propósito que orienta o Tratamento**, mantendo relações específicas com o Controlador, o Consentimento e o Titular.

A conclusão geral é:

> **A OntoPrivacy v2 encontra-se conceitualmente próxima do congelamento. Não há necessidade de nova ampliação do domínio antes da redação da dissertação. As ações imediatas devem concentrar-se em pequenas correções documentais, validação pelas Questões de Competência e sincronização dos artefatos textuais da pesquisa.**

## 1.1 Avaliação global

| Dimensão                             |                     Avaliação | Diagnóstico                                                                                                                             |
| ------------------------------------ | ----------------------------: | --------------------------------------------------------------------------------------------------------------------------------------- |
| Delimitação do domínio               |                     **Forte** | O modelo concentra-se nos conceitos necessários ao tratamento, à identificabilidade, aos participantes, ao consentimento e à finalidade |
| Adequação ao objetivo da dissertação |                     **Forte** | O vocabulário é aplicável à anotação de APIs e à análise de requisitos                                                                  |
| Fundamentação UFO/OntoUML            |                     **Forte** | A maior parte das classificações expressa adequadamente identidade, rigidez e dependência                                               |
| Arquitetura relacional               |                     **Forte** | Os três `relators` oferecem uma organização clara e integrada                                                                           |
| Modelagem da Finalidade              |                     **Forte** | A Finalidade passou a caracterizar o TDP e relacionar Controlador, Consentimento e Titular                                              |
| Tratamento e operações               |                     **Forte** | O TDP fornece identidade às operações classificadas como `subkind`                                                                      |
| Dados e identificabilidade           |                     **Forte** | A pessoalidade do dado é explicada relacionalmente, e não apenas declarada                                                              |
| Consentimento                        |                     **Forte** | É independente da existência do TDP e vinculado a Finalidades determinadas                                                              |
| Definições                           |                       **Boa** | Todos os conceitos têm definição; duas relações exigem correção documental                                                              |
| Correspondência ASTA–PNG             |                     **Forte** | Classes, generalizações e associações principais estão presentes nos dois artefatos                                                     |
| Legibilidade do diagrama único       |       **Intermediária/forte** | O modelo é denso, mas possui agrupamentos e codificação visual consistentes                                                             |

---

## 1.2 Inventário

| Elemento                      |   Quantidade |
| ----------------------------- | -----------: |
| Classificadores               |       **43** |
| Generalizações                |       **36** |
| Associações                   |       **21** |
| Atributos                     |        **1** |
| Restrições                    |        **8** |
| Classificadores abstratos     |        **8** |
| Classificadores com definição | **43 de 43** |
| Associações com definição     | **21 de 21** |

As oito restrições correspondem a:

* sete conjuntos ou condições de generalização;
* uma restrição própria de `Dado Pseudonimizado`.

O único atributo do modelo é:

```text
Finalidade.descrição : string [1]
```

Sua definição interna estabelece que se trata da expressão textual obrigatória e suficientemente individualizada do propósito do TDP.

## 1.3 Distribuição dos estereótipos

| Estereótipo      | Quantidade |
| ---------------- | ---------: |
| `<<subkind>>`    |         18 |
| `<<role>>`       |         10 |
| `<<roleMixin>>`  |          5 |
| `<<kind>>`       |          3 |
| `<<relator>>`    |          3 |
| `<<mode>>`       |          2 |
| `<<category>>`   |          1 |
| `<<collective>>` |          1 |
| **Total**        |     **43** |

Os classificadores abstratos são:

* `Agente Legal`;
* `Parte Interessada na Privacidade`;
* `Agente de Tratamento`;
* `Controlador`;
* `Operador`;
* `Terceiro`;
* `DP Sensível`;
* `Tratamento de Dados Pessoais`.

## 1.4 Distribuição das associações

| Tipo de relação        | Quantidade |
| ---------------------- | ---------: |
| `<<mediation>>`        |         10 |
| `<<characterization>>` |          2 |
| `<<material>>`         |          2 |
| `<<memberOf>>`         |          2 |
| Associação comum       |          5 |
| **Total**              |     **21** |

A quantidade de mediações é coerente com a centralidade dos três `relators` e demonstra que o modelo não se limita a uma taxonomia: ele representa dependências entre dados, participantes e situações relacionais.

---

# 2. Estrutura ontológica geral

A leitura mais adequada da v2 parte dos três `relators`:

```text
IDENTIFICABILIDADE
Por que o dado é pessoal e a quem se refere?

TRATAMENTO DE DADOS PESSOAIS
O que é realizado sobre o dado, por quem e para qual finalidade?

CONSENTIMENTO
Quem concorda, perante qual controlador, com qual tratamento e para quais finalidades?
```

## 2.1 Síntese dos três centros

| `Relator`                      | Questão central                                                                                | Participantes ou elementos relacionados                                        |
| ------------------------------ | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| `Identificabilidade`           | Por que um Dado é pessoal e a quem ele se refere?                                              | Dado Pessoal e Titular de DP                                                   |
| `Tratamento de Dados Pessoais` | O que é realizado, sobre quais dados, por quais participantes e para qual propósito?           | Dado Pessoal, Parte Interessada, Controlador, Operador, Operações e Finalidade |
| `Consentimento`                | Quando há manifestação de concordância, quem a manifesta, a quem é dirigida e qual seu escopo? | Titular, Controlador, TDP e Finalidade                                         |

OntoUML utiliza `Relator` para representar a objetificação de propriedades relacionais, isto é, entidades cuja existência depende dos participantes que conectam. Um `Relator` fornece identidade às suas instâncias e pode ser especializado por `Subkind`, `Phase` ou `Role`. ([OntoUML][1])

---

# 3. Agentes, identidade e papéis

## 3.1 `Agente Legal <<category>>`

A base dos participantes é:

```text
Agente Legal <<category>> {abstract}
├── Pessoa Natural <<kind>>
└── Pessoa Jurídica <<kind>>

{disjoint, complete}
```

Essa estrutura é adequada porque Pessoa Natural e Pessoa Jurídica possuem princípios de identidade distintos. `Agente Legal` não cria uma nova identidade comum; ele agrega propriedades essenciais compartilháveis por entidades pertencentes a diferentes `kind`s.

Uma `Category` é um tipo rígido, abstrato e não sortal, utilizado para reunir indivíduos submetidos a diferentes princípios de identidade. ([OntoUML][2])

A partição `{disjoint, complete}` estabelece que:

* todo Agente Legal é Pessoa Natural ou Pessoa Jurídica;
* nenhum Agente Legal é simultaneamente ambos.

A definição também registra `Pessoa de Direito` e `Sujeito de Direito` como expressões correlatas. Para evitar confusão com “representante legal”, recomenda-se manter esses sinônimos documentados, ainda que `Agente Legal` permaneça como rótulo canônico.

## 3.2 Pessoas jurídicas e entidades organizacionais

A hierarquia organizacional é:

```text
Pessoa Jurídica <<kind>>
└── Entidade Organizacional <<subkind>>
    ├── Agência <<subkind>>
    └── Autoridade Pública <<subkind>>
```

A classificação é coerente com a decisão de tratar Agência e Autoridade Pública como especializações rígidas de uma entidade organizacional juridicamente individualizada.

Essa estrutura atende ao escopo atual sem introduzir:

* órgãos sem personalidade própria;
* unidades administrativas;
* sistemas computacionais como agentes jurídicos;
* componentes internos de organizações.

Esses elementos podem aparecer nos artefatos de Engenharia de Software como participantes técnicos, mas não devem ser automaticamente classificados como Agentes Legais.

## 3.3 `Parte Interessada na Privacidade <<roleMixin>>`

A estrutura é:

```text
Agente Legal <<category>>
└── Parte Interessada na Privacidade <<roleMixin>> {abstract}
```

`Parte Interessada na Privacidade` é um papel aplicável tanto a Pessoas Naturais quanto a Pessoas Jurídicas. Por isso, a utilização de `roleMixin` é mais adequada do que `role`.

Um `RoleMixin` é antirrígido, relacionalmente dependente e aplicável a entidades com diferentes princípios de identidade. A especificação de OntoUML admite explicitamente o padrão no qual um `RoleMixin` atua como papel de uma `Category`, exatamente como ocorre entre Parte Interessada e Agente Legal. ([OntoUML][3])

## 3.4 Agente de Tratamento, Controlador e Operador

```text
Parte Interessada na Privacidade
└── Agente de Tratamento <<roleMixin>> {abstract}
    ├── Controlador <<roleMixin>> {abstract}
    └── Operador <<roleMixin>> {abstract}

{complete}
```

O conjunto `{complete}` expressa que todo Agente de Tratamento é Controlador, Operador ou pode se enquadrar nos dois papéis conforme os contextos considerados.

A ausência de uma disjunção global é adequada porque uma mesma Pessoa Jurídica pode:

* ser Controladora em um TDP;
* ser Operadora em outro;
* manter sua identidade organizacional em ambos.

### Controlador

`Controlador` é definido como o papel desempenhado pelo Agente Legal que possui competência decisória sobre determinado TDP, incluindo a definição de Finalidades e meios.

Ele se relaciona ao modelo por meio de:

```text
Controlador é responsável pelo TDP
Controlador define Finalidade
Controlador instrui Operador
Consentimento é dirigido a Controlador
```

A LGPD define Controlador pela competência para tomar decisões referentes ao tratamento. A associação com a definição da Finalidade é, portanto, uma decisão de modelagem coerente com essa competência decisória. ([Planalto][4])

### Operador

`Operador` é definido como o papel desempenhado pelo Agente Legal que realiza o TDP em nome do Controlador, observando instruções e limites das Finalidades.

Sua relação principal é:

```text
Operador realiza TDP
```

A ligação com a Finalidade é deliberadamente indireta:

```text
Operador → realiza → TDP → é orientado por → Finalidade
```

Essa solução evita uma associação redundante `Operador respeita Finalidade`, preservando a ideia de que o Operador executa o tratamento delimitado pelo propósito definido pelo Controlador.

## 3.5 `Terceiro <<roleMixin>>`

`Terceiro` é uma especialização de Parte Interessada. Sua interpretação é contextual: uma organização pode ser Terceiro em determinado TDP e Controladora em outro.

A opção de não criar uma disjunção global com Agente de Tratamento preserva corretamente essa possibilidade contextual.

## 3.6 `Titular de DP <<role>>`

```text
Pessoa Natural <<kind>>
Parte Interessada na Privacidade <<roleMixin>>
          \             /
           Titular de DP <<role>>
```

O Titular herda identidade de Pessoa Natural e também é classificado como Parte Interessada.

Essa estrutura representa corretamente que:

* o indivíduo existe como Pessoa Natural independentemente de possuir dados no modelo;
* ele desempenha o papel de Titular quando há Dados Pessoais que a ele se referem;
* o papel pode deixar de existir sem que a Pessoa Natural perca sua identidade.

`Role` representa uma especialização antirrígida de um provedor de identidade, cuja instanciação depende de um contexto relacional. ([OntoUML][5])

---

# 4. Dados, classificações e coleções

## 4.1 `Dado <<kind>>`

`Dado` é o provedor de identidade do núcleo informacional:

```text
Dado <<kind>>
├── Dado Pessoal <<role>>
└── Dado Anonimizado <<role>>
```

A definição adotada considera Dado uma unidade informacional individualizada em determinado contexto de representação, registro ou uso.

Essa decisão permite que ocorrências com o mesmo valor lexical sejam tratadas como dados distintos. O CPF presente:

* em um cadastro;
* em um log;
* em uma requisição;
* em um relatório;

pode corresponder a diferentes instâncias de Dado, ainda que o valor representado seja igual.

A classificação como `kind` também permite representar dados não pessoais. Um Dado pode existir sem desempenhar os papéis de Dado Pessoal ou Dado Anonimizado.

## 4.2 `Dado Pessoal <<role>>`

Dado Pessoal é um papel desempenhado por Dado quando há uma relação de Identificabilidade que o conecta a um Titular.

A ontologia, portanto, não trata a pessoalidade apenas como uma etiqueta:

```text
Dado
  +
Identificabilidade
  +
Titular
  =
Dado que desempenha o papel de Dado Pessoal
```

Essa é uma decisão particularmente adequada ao enriquecimento semântico de artefatos de Engenharia de Software. Um campo técnico não deve ser classificado como Dado Pessoal apenas pelo nome; sua interpretação depende da relação que permite associá-lo a uma Pessoa Natural.

A LGPD define Dado Pessoal como informação relacionada a pessoa natural identificada ou identificável, o que sustenta a centralidade da Identificabilidade na OntoPrivacy. ([Planalto][4])

## 4.3 Dado Pessoal Sensível

```text
Dado Pessoal
└── DP Sensível <<role>> {abstract}
    ├── DP Religião
    ├── DP Etnia
    ├── DP Político
    ├── DP Saúde
    └── DP Biométrico

{overlapping, incomplete}
```

A modelagem expressa duas decisões:

* `overlapping`: um mesmo dado pode enquadrar-se em mais de uma categoria;
* `incomplete`: as categorias representadas não esgotam o universo dos dados sensíveis.

A cobertura parcial foi explicitamente aceita para esta versão e não constitui pendência de congelamento.

## 4.4 `Dado Pseudonimizado <<role>>`

```text
Dado Pessoal
└── Dado Pseudonimizado
```

O dado pseudonimizado permanece pessoal porque a associação ao Titular pode ser restabelecida mediante informação adicional.

A ontologia também registra a restrição:

> Todo Dado Pseudonimizado participa de pelo menos uma Identificabilidade Indireta.

Essa combinação é conceitualmente forte:

```text
Pseudonimização
    resulta em
Dado Pseudonimizado
    continua sendo
Dado Pessoal
    participa de
Identificabilidade Indireta
```

A restrição não aparece no PNG, devendo ser apresentada no texto da Seção 3.1 ou no catálogo conceitual.

## 4.5 `Dado Anonimizado <<role>>` e `Anonimidade <<mode>>`

```text
Dado
└── Dado Anonimizado <<role>>
        │
        └── Anonimidade <<mode>>
```

A OntoPrivacy diferencia:

| Elemento           | Natureza                                |
| ------------------ | --------------------------------------- |
| `Anonimização`     | Operação de tratamento                  |
| `Dado Anonimizado` | Papel desempenhado pelo dado resultante |
| `Anonimidade`      | Propriedade intrínseca do resultado     |

Essa separação evita a confusão entre processo, resultado e condição.

A disjunção entre Dado Pessoal e Dado Anonimizado deve ser compreendida no contexto de análise delimitado e considerando os meios razoáveis disponíveis. A ontologia não representa explicitamente os meios, capacidades ou conhecimentos auxiliares utilizados na avaliação da identificabilidade; esse é um limite de escopo da versão, e não uma pendência a ser resolvida agora.

## 4.6 Conjunto de Dados e Banco de Dados DP

```text
Conjunto de Dados <<collective>>
└── Banco de Dados DP <<subkind>>
```

As relações são:

```text
Dado memberOf Conjunto de Dados
Dado Pessoal memberOf Banco de Dados DP
```

Essa estrutura permite distinguir:

* o dado individual;
* o conjunto organizado;
* o banco especificamente constituído por dados pessoais.

A utilização de `collective` é adequada à interpretação de conjunto populado, formado por membros considerados uniformemente no contexto de organização.

---

# 5. Primeiro `<<relator>>`: Identificabilidade

## 5.1 Estrutura

```text
Identificabilidade <<relator>>
├── Identificabilidade Direta <<subkind>>
└── Identificabilidade Indireta <<subkind>>

{disjoint, complete}
```

Mediações:

```text
Identificabilidade baseia-se em Dado Pessoal
Identificabilidade identifica Titular de DP
```

Relação material apresentada:

```text
Dado Pessoal refere-se a Titular de DP
```

A Identificabilidade responde:

> **Por que determinado Dado é pessoal e a qual Pessoa Natural ele se refere?**

## 5.2 Direta e indireta

### Identificabilidade Direta

Representa a situação na qual o Titular pode ser individualizado sem depender de combinação relevante com informação adicional separada.

Exemplos possíveis:

* CPF;
* número de identidade;
* nome acompanhado de contexto inequívoco;
* identificador institucional diretamente associado à pessoa.

### Identificabilidade Indireta

Representa a situação na qual a individualização depende de:

* combinação de dados;
* informação complementar;
* conhecimento auxiliar;
* meios razoavelmente disponíveis no contexto.

Exemplos:

* combinação de idade, profissão e localização;
* identificador pseudonimizado acompanhado de tabela separada;
* conjunto de atributos que, isoladamente, não identifica a pessoa.

O conjunto `{disjoint, complete}` estabelece que cada instância de Identificabilidade é direta ou indireta.

## 5.3 Valor conceitual

Essa estrutura produz uma definição ontológica mais precisa de Dado Pessoal:

> **Dado Pessoal é o papel desempenhado por um Dado quando ele participa de uma Identificabilidade que o vincula direta ou indiretamente a um Titular de DP.**

Também explica o papel Titular:

> **Titular de DP é o papel desempenhado por uma Pessoa Natural identificada por uma Identificabilidade fundamentada em um ou mais Dados Pessoais.**

---

# 6. Segundo `<<relator>>`: Tratamento de Dados Pessoais

## 6.1 Estrutura principal

```text
Tratamento de Dados Pessoais <<relator>> {abstract}
├── Operação de TDP <<subkind>>
└── Conjunto de Operações de TDP <<subkind>>

{disjoint, complete}
```

A decisão representa o TDP como uma **situação relacional**, e não como uma execução temporal detalhada.

Sua definição autoral estabelece que o tratamento conecta:

* uma ou mais Partes Interessadas;
* um ou mais Dados Pessoais;
* uma Operação ou conjunto articulado de Operações;
* um ou mais Controladores responsáveis;
* uma ou mais Finalidades.

## 6.2 Mediações e relações centrais

```text
TDP envolve Parte Interessada
TDP abrange Dado Pessoal
Controlador é responsável pelo TDP
Operador realiza TDP
TDP é orientado por Finalidade
```

Esse conjunto permite responder:

* quais dados são tratados;
* quem participa;
* quem decide;
* quem realiza;
* para qual propósito o tratamento ocorre;
* qual operação ou combinação de operações constitui o tratamento.

## 6.3 Operação de TDP como `<<subkind>>`

A utilização de `subkind` é adequada porque as operações herdam o princípio de identidade fornecido pelo relator TDP.

Assim:

```text
Coleta
    é uma Operação de TDP
    é um Tratamento de Dados Pessoais
    herda a identidade relacional de TDP
```

Não se introduz um novo princípio de identidade para cada modalidade.

## 6.4 Operações representadas

```text
Operação de TDP
├── Alteração
├── Armazenamento
├── Coleta
├── Consulta
├── Pseudonimização
├── Disponibilização
├── Divulgação
├── Exclusão
├── Recuperação
└── Anonimização

{overlapping, incomplete}
```

O conjunto `overlapping` permite que uma situação técnica mais ampla envolva diferentes operações. Por exemplo, um envio de formulário pode envolver:

* Coleta;
* Armazenamento.

Uma leitura de API pode envolver:

* Consulta, pela perspectiva do consumidor;
* Disponibilização, pela perspectiva do provedor.

A incompletude expressa que a OntoPrivacy não pretende representar exaustivamente todas as operações enumeradas pela LGPD ou por outras fontes.

## 6.5 Exclusão e Eliminação

A decisão canônica está refletida no modelo:

```text
Conceito: Exclusão
Sinônimo normativo: Eliminação
```

Na redação da dissertação, a primeira ocorrência pode ser apresentada como:

> **Exclusão — denominada “eliminação” na LGPD — é a operação de tratamento pela qual um dado ou conjunto de dados é excluído, independentemente do procedimento empregado.**

Depois disso, `Exclusão` deve ser usado de forma consistente como rótulo da OntoPrivacy.

---

# 7. Terceiro `<<relator>>`: Consentimento

## 7.1 Estrutura

```text
Consentimento <<relator>>
├── é manifestado por → Titular de DP
├── é dirigido a → Controlador
├── tem escopo → TDP
└── refere-se a → Finalidade
```

O Consentimento representa uma manifestação relacional, e não:

* um atributo booleano;
* um estado do Titular;
* uma propriedade isolada do TDP;
* uma conclusão de licitude.

## 7.2 Leitura conceitual

O relator responde:

> **Quem manifesta concordância, perante qual Controlador, com qual TDP e para quais Finalidades determinadas?**

A definição interna é coerente com esse propósito:

> Consentimento representa a manifestação livre, informada e inequívoca do Titular, dirigida a um ou mais Controladores, relativa a determinado TDP e a uma ou mais Finalidades.

A LGPD define Consentimento como manifestação pela qual o Titular concorda com o tratamento para uma finalidade determinada. Também estabelece que o princípio da Finalidade exige propósitos legítimos, específicos, explícitos e informados ao Titular. ([Planalto][6])

## 7.3 Separação entre Consentimento e existência do TDP

A estrutura permite representar:

```text
TDP sem Consentimento
TDP com um Consentimento
TDP com vários Consentimentos
```

Essa é uma decisão correta porque Consentimento:

* não constitui condição ontológica de existência do tratamento;
* não é a única hipótese jurídica prevista pela LGPD;
* não transforma o TDP em uma entidade automaticamente lícita.

## 7.4 Limite interpretativo

A presença de uma instância de Consentimento não permite inferir automaticamente:

```text
Consentimento válido
TDP lícito
Base legal suficiente
Conformidade com a LGPD
```

A OntoPrivacy representa a estrutura da manifestação, não sua validade jurídica.

---

# 8. Finalidade como elemento integrador

## 8.1 Classificação

```text
Finalidade <<mode>>
descrição : string [1]
```

`Finalidade` é tratada como uma propriedade particularizada e existencialmente dependente de um TDP.

Um `Mode` representa uma propriedade intrínseca dependente de seu portador e deve estar conectado a ele por `Characterization`. A extremidade caracterizada deve corresponder exatamente a um portador. ([OntoUML][7])

Na v2:

```text
TDP <<characterization>> é orientado por Finalidade
```

Cada Finalidade pertence conceitualmente a um TDP específico.

## 8.2 Interpretação ontológica

A definição pode ser condensada como:

> **Finalidade é o modo dependente de um Tratamento de Dados Pessoais que expressa o propósito determinado para o qual o tratamento é realizado, orientando e delimitando suas operações.**

Essa modelagem diferencia:

| Conceito        | Pergunta                                         |
| --------------- | ------------------------------------------------ |
| TDP             | O que é realizado com os dados?                  |
| Operação de TDP | Como o tratamento se concretiza?                 |
| Finalidade      | Para que o tratamento é realizado?               |
| Base legal      | Em qual hipótese jurídica o tratamento se apoia? |

Finalidade e Base Legal não devem ser tratadas como sinônimos.

## 8.3 Relações da Finalidade

### Com o TDP

```text
TDP é orientado por Finalidade
```

Essa é a relação constitutiva principal. A Finalidade existe como propósito daquele TDP.

### Com o Controlador

```text
Controlador define Finalidade
```

O Controlador é o participante que estabelece os objetivos e meios do tratamento.

### Com o Consentimento

```text
Consentimento refere-se a Finalidade
```

A Finalidade não pertence exclusivamente ao Consentimento. Ela pertence ao TDP, e o Consentimento seleciona uma ou mais Finalidades do tratamento ao qual se refere.

Essa decisão permite representar:

```text
TDP-01
├── Finalidade F-01
└── Finalidade F-02

Consentimento C-01
├── tem escopo TDP-01
└── refere-se apenas a F-02
```

Isso é semanticamente mais preciso que duplicar as finalidades dentro de cada Consentimento.

### Com o Titular

```text
Finalidade é informada ao Titular
```

Essa relação explicita a dimensão de transparência entre o propósito do tratamento e a Pessoa Natural à qual os dados se referem.

### Com o Operador

Não há associação direta. O vínculo é obtido por:

```text
Operador realiza TDP
TDP é orientado por Finalidade
```

Essa opção reduz redundância e preserva a centralidade do tratamento.

## 8.4 Implicação da escolha por `mode`

Uma consequência importante é que a Finalidade é uma propriedade particular daquele TDP.

Se dois tratamentos possuem a descrição:

```text
“realizar matrícula acadêmica”
```

a ontologia representa duas instâncias distintas de Finalidade, uma para cada TDP. O texto pode ser igual, mas a propriedade é existencialmente dependente de seu respectivo tratamento.

Essa decisão favorece:

* rastreabilidade;
* delimitação contextual;
* associação ao Consentimento;
* identificação de mudanças de propósito.

Em contrapartida, `Finalidade` não funciona como uma taxonomia reutilizável de categorias genéricas. Caso futuramente seja necessário classificar finalidades em tipos como “prestação de serviço”, “marketing” ou “cumprimento regulatório”, isso exigirá uma estrutura adicional. Tal expansão não é necessária para a dissertação atual.

---

# 9. Anonimização e pseudonimização

## 9.1 Anonimização

```text
Anonimização <<subkind>>
    resulta em
Dado Anonimizado <<role>>
    é caracterizado por
Anonimidade <<mode>>
```

A estrutura distingue:

1. a situação de tratamento;
2. o resultado produzido;
3. a condição intrínseca do resultado.

## 9.2 Pseudonimização

```text
Pseudonimização <<subkind>>
    resulta em
Dado Pseudonimizado <<role>>
    participa de
Identificabilidade Indireta
```

O resultado permanece Dado Pessoal, coerentemente com a possibilidade de reidentificação mediante informação adicional.

## 9.3 Relação entre os três núcleos

Essas duas operações conectam diretamente:

```text
TDP
  ↓
Operação de transformação
  ↓
Dado resultante
  ↓
Identificabilidade ou Anonimidade
```

Elas demonstram que a OntoPrivacy não possui três blocos isolados; os `relators`, papéis e modos formam uma conceituação integrada.

---

# 10. Conjuntos de generalização

| Estrutura                               | Restrição                   | Interpretação                                                      |
| --------------------------------------- | --------------------------- | ------------------------------------------------------------------ |
| Pessoa Natural / Pessoa Jurídica        | `{disjoint, complete}`      | Todo Agente Legal pertence exatamente a uma dessas categorias      |
| Dado Pessoal / Dado Anonimizado         | `{disjoint}`                | Não podem coexistir no mesmo contexto; outros dados são permitidos |
| Identificabilidade Direta / Indireta    | `{disjoint, complete}`      | Toda Identificabilidade possui exatamente uma modalidade           |
| Operação de TDP / Conjunto de Operações | `{disjoint, complete}`      | Todo TDP é unitário ou composto                                    |
| Tipos de operação                       | `{overlapping, incomplete}` | Podem coexistir e não esgotam o domínio                            |
| Controlador / Operador                  | `{complete}`                | Todo Agente de Tratamento assume pelo menos um desses papéis       |
| Categorias sensíveis                    | `{overlapping, incomplete}` | Podem coexistir e não esgotam os dados sensíveis                   |

A utilização dos conjuntos é coerente com a conceituação pretendida e melhora a compreensão do grau de cobertura e exclusividade das especializações.

---

# 11. Pontos fortes consolidados

| Ponto forte                                   | Relevância                                                                     |
| --------------------------------------------- | ------------------------------------------------------------------------------ |
| Arquitetura centrada em três `relators`       | Fornece leitura integrada do domínio                                           |
| Pessoalidade explicada por Identificabilidade | Evita classificar dados sem considerar vínculo com Pessoa Natural              |
| TDP como estrutura relacional                 | Integra dados, participantes, operações e finalidade                           |
| Operações como `subkind`                      | Preserva um único princípio de identidade relacional                           |
| Finalidade como modo do TDP                   | Representa propósito independentemente do Consentimento                        |
| Consentimento ligado às Finalidades do TDP    | Evita consentimento genérico e duplicação conceitual                           |
| Papéis contextuais de agentes                 | Permite que a mesma entidade assuma papéis distintos em diferentes tratamentos |
| Pseudonimizado permanece pessoal              | Mantém coerência com a reidentificação indireta                                |
| Separação operação–resultado–propriedade      | Fortalece anonimização e pseudonimização                                       |
| Partições explícitas                          | Comunicam completude, sobreposição e exclusividade                             |
| Definições presentes em todos os conceitos    | Favorece documentação e rastreabilidade                                        |
| Correspondência ASTA–PNG                      | Reduz divergência entre modelo armazenado e modelo comunicado                  |
| Escopo não exaustivo explicitável             | Mantém comprometimento ontológico controlado                                   |
| Aplicabilidade a artefatos de ES              | Sustenta OpenAPI e Engenharia de Requisitos                                    |

---

# 12. Limites que devem ser declarados, sem modificar a v2

A redação da dissertação deve explicitar que a OntoPrivacy v2:

* representa um núcleo selecionado de privacidade de dados;
* não representa integralmente a LGPD;
* não determina Base Legal;
* não conclui licitude;
* não avalia a validade jurídica do Consentimento;
* não certifica conformidade;
* não representa detalhadamente os meios técnicos de identificabilidade;
* não modela o ciclo de vida temporal do Consentimento;
* não constitui uma ontologia operacional processável por raciocinador;
* não pretende esgotar operações, dados sensíveis, direitos, riscos ou controles.

Esses limites são compatíveis com uma ontologia de referência de domínio e não diminuem sua contribuição.

---

# 13. Questões de Competência recomendadas para a v2

As QCs atualmente registradas no Capítulo 3 ainda incluem Base Legal e atores autorizados/desautorizados, elementos que não pertencem à OntoPrivacy v2. 

Recomenda-se substituir o conjunto atual pelas seguintes questões.

## QC1 — Dados e coleções

> **Quais Dados e Conjuntos de Dados envolvidos em uma situação são classificados como Dado Pessoal, DP Sensível, Dado Pseudonimizado ou Dado Anonimizado, e em quais Bancos de Dados DP estão organizados?**

Elementos mobilizados:

* Dado;
* Dado Pessoal;
* DP Sensível;
* Dado Pseudonimizado;
* Dado Anonimizado;
* Conjunto de Dados;
* Banco de Dados DP.

## QC2 — Titular e identificabilidade

> **A quais Titulares cada Dado Pessoal se refere e por qual modalidade de Identificabilidade, direta ou indireta, esse vínculo é sustentado?**

Elementos mobilizados:

* Dado Pessoal;
* Titular de DP;
* Identificabilidade;
* Identificabilidade Direta;
* Identificabilidade Indireta.

## QC3 — Participantes e papéis

> **Quais Partes Interessadas participam de cada Tratamento de Dados Pessoais e quais papéis desempenham, como Titular, Controlador, Operador ou Terceiro?**

Elementos mobilizados:

* Agente Legal;
* Pessoa Natural;
* Pessoa Jurídica;
* Parte Interessada;
* Titular;
* Controlador;
* Operador;
* Terceiro.

## QC4 — Estrutura e operações do tratamento

> **Quais Dados Pessoais são abrangidos por cada TDP, e esse tratamento corresponde a uma Operação de TDP ou a um Conjunto de Operações? Quais tipos específicos de operação o caracterizam ou compõem?**

Elementos mobilizados:

* TDP;
* Operação de TDP;
* Conjunto de Operações;
* tipos específicos de operação;
* Dado Pessoal.

## QC5 — Finalidade

> **Quais Finalidades orientam cada Tratamento de Dados Pessoais, quais Controladores as definem e a quais Titulares elas são informadas?**

Elementos mobilizados:

* TDP;
* Finalidade;
* Controlador;
* Titular.

## QC6 — Consentimento

> **Quando há Consentimento, qual Titular o manifesta, a quais Controladores é dirigido, qual TDP está em seu escopo e a quais Finalidades ele se refere?**

Elementos mobilizados:

* Consentimento;
* Titular;
* Controlador;
* TDP;
* Finalidade.

## QC7 — Transformações dos dados

> **Quais operações de Anonimização ou Pseudonimização abrangem determinados Dados Pessoais, quais dados resultam dessas operações e qual condição de identificabilidade ou anonimidade permanece?**

Elementos mobilizados:

* Anonimização;
* Pseudonimização;
* Dado Pessoal;
* Dado Anonimizado;
* Dado Pseudonimizado;
* Anonimidade;
* Identificabilidade Indireta.

## 13.1 Cobertura conceitual

| QC  | Cobertura pela v2   |
| --- | ------------------- |
| QC1 | Forte               |
| QC2 | Forte               |
| QC3 | Forte               |
| QC4 | Forte               |
| QC5 | Forte               |
| QC6 | Forte               |
| QC7 | Forte               |

A avaliação é de **respondibilidade conceitual**. Não significa que a v2 já possua uma linguagem operacional de consulta ou inferência.

---

# 14. Cenários mínimos para validação conceitual

| Cenário                                                          | Aspectos verificados                                   |
| ---------------------------------------------------------------- | ------------------------------------------------------ |
| CPF identifica diretamente um aluno                              | Dado Pessoal, Titular e Identificabilidade Direta      |
| CEP, idade e profissão identificam conjuntamente uma pessoa      | Identificabilidade Indireta baseada em múltiplos dados |
| Uma organização é Controladora em TDP-1 e Operadora em TDP-2     | Papéis contextuais e ausência de disjunção global      |
| TDP de matrícula contém Coleta e Armazenamento                   | TDP composto e operações sobrepostas                   |
| TDP possui duas Finalidades sem Consentimento                    | Finalidade independente do Consentimento               |
| Consentimento refere-se a apenas uma das duas Finalidades do TDP | Especificidade da manifestação                         |
| Dado pseudonimizado depende de tabela separada                   | Dado Pessoal e Identificabilidade Indireta             |
| Anonimização produz dados caracterizados por Anonimidade         | Operação, resultado e modo                             |
| Um dado integra dois Conjuntos de Dados                          | Relação de pertencimento                               |
| Dado é simultaneamente biométrico e de saúde                     | Sobreposição de categorias sensíveis                   |
| Terceiro em um TDP torna-se Controlador em outro                 | Contextualidade dos papéis                             |
| API oferece consulta e disponibilização na mesma interação       | Perspectivas complementares das operações              |

Cada cenário deve registrar:

* instâncias consideradas;
* classificações esperadas;
* relações utilizadas;
* QC respondida;
* resultado;
* decisão ou observação.

---

# 15. MAPA da análise

Legenda:

* 🟢 consolidado;
* 🟡 exige ajuste documental ou sincronização.

```text
ONTOPRIVACY v2
│
├── 1. POSICIONAMENTO
│   ├── 🟢 Ontologia de referência de domínio
│   ├── 🟢 Nível conceitual
│   ├── 🟢 Fundamentação principal na LGPD
│   ├── 🟢 Complementação pela ISO/IEC 29100
│   ├── 🟢 Modelagem UFO/OntoUML
│   └── 🟢 Aplicação em artefatos de Engenharia de Software
│
├── 2. IDENTIDADE E PARTICIPANTES
│   ├── 🟢 Agente Legal <<category>>
│   │   ├── Pessoa Natural <<kind>>
│   │   └── Pessoa Jurídica <<kind>>
│   │       └── Entidade Organizacional <<subkind>>
│   │           ├── Agência
│   │           └── Autoridade Pública
│   ├── 🟢 Parte Interessada <<roleMixin>>
│   ├── 🟢 Agente de Tratamento <<roleMixin>>
│   │   ├── Controlador
│   │   └── Operador
│   ├── 🟢 Terceiro <<roleMixin>>
│   └── 🟢 Titular de DP <<role>>
│
├── 3. DADOS
│   ├── 🟢 Dado <<kind>>
│   ├── 🟢 Dado Pessoal <<role>>
│   │   ├── Dado Pseudonimizado
│   │   └── DP Sensível
│   ├── 🟢 Dado Anonimizado <<role>>
│   │   └── Anonimidade <<mode>>
│   ├── 🟢 Conjunto de Dados <<collective>>
│   └── 🟢 Banco de Dados DP <<subkind>>
│
├── 4. RELATOR 1 — IDENTIFICABILIDADE
│   ├── 🟢 baseia-se em Dado Pessoal
│   ├── 🟢 identifica Titular
│   ├── 🟢 Identificabilidade Direta
│   └── 🟢 Identificabilidade Indireta
│
├── 5. RELATOR 2 — TDP
│   ├── 🟢 abrange Dado Pessoal
│   ├── 🟢 envolve Parte Interessada
│   ├── 🟢 Controlador é responsável
│   ├── 🟢 Operador realiza
│   ├── 🟢 é orientado por Finalidade
│   ├── 🟢 Operação de TDP
│   └── 🟢 Conjunto de Operações de TDP
│
├── 6. OPERAÇÕES
│   ├── 🟢 Coleta
│   ├── 🟢 Armazenamento
│   ├── 🟢 Alteração
│   ├── 🟢 Consulta
│   ├── 🟢 Recuperação
│   ├── 🟢 Divulgação
│   ├── 🟢 Disponibilização
│   ├── 🟢 Exclusão
│   ├── 🟢 Anonimização
│   └── 🟢 Pseudonimização
│
├── 7. RELATOR 3 — CONSENTIMENTO
│   ├── 🟢 manifestado por Titular
│   ├── 🟢 dirigido a Controlador
│   ├── 🟢 tem TDP em seu escopo
│   └── 🟢 refere-se a Finalidade
│
├── 8. FINALIDADE
│   ├── 🟢 Finalidade <<mode>>
│   ├── 🟢 caracteriza TDP
│   ├── 🟢 definida por Controlador
│   ├── 🟢 referida pelo Consentimento
│   ├── 🟢 informada ao Titular
│   └── 🟢 descrição obrigatória
│
└── 9. DOCUMENTAÇÃO
    ├── 🟢 43 conceitos com definição
    ├── 🟢 21 associações com definição
    ├── 🟢 ASTA e PNG sincronizados
    └── 🟢 Catálogo da OntoPrivacy
```

## 15.1 Mapa dos três centros

```text
DADO <<kind>>
    │
    └── desempenha o papel de
            DADO PESSOAL <<role>>
                    │
                    ▼
          IDENTIFICABILIDADE <<relator>>
             ├── baseia-se no Dado
             └── identifica o Titular
                    │
                    ▼
             TITULAR DE DP <<role>>


DADO PESSOAL + PARTES INTERESSADAS
                    │
                    ▼
        TRATAMENTO DE DADOS PESSOAIS
                    <<relator>>
             ├── abrange dados
             ├── envolve participantes
             ├── possui Controlador
             ├── pode possuir Operador
             ├── é Operação ou Conjunto
             └── é orientado por Finalidade


Quando houver manifestação:
                    │
                    ▼
            CONSENTIMENTO <<relator>>
             ├── manifestado pelo Titular
             ├── dirigido ao Controlador
             ├── tem o TDP em seu escopo
             └── refere-se às Finalidades
```

---
