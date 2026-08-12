# A02 — Extensões OpenAPI consideradas pela abordagem

## 1. Objetivo

Este documento consolida as propriedades de extensão utilizadas como base técnica da abordagem de anotação semântica. As propriedades seguem o mecanismo de **Specification Extensions** da OpenAPI, no qual campos adicionais são identificados pelo prefixo `x-`.

## 2. Propriedades consideradas

| Propriedade | Elemento OpenAPI de referência | Significado operacional na abordagem |
|---|---|---|
| `x-refersTo` | Schema Object | relaciona um elemento da descrição a um conceito de um modelo semântico |
| `x-kindOf` | Schema Object | representa uma relação de especialização entre um elemento da descrição e um conceito mais geral |
| `x-mapsTo` | Schema Object | registra mapeamento entre elementos semanticamente equivalentes |
| `x-collectionOn` | Schema Object | relaciona uma coleção ao conceito que representa o tipo dos seus itens |
| `x-onResource` | Tag Object | indica o recurso descrito pelo elemento |
| `x-operationType` | Operation Object | indica o tipo semântico atribuído a uma operação HTTP |

Essas propriedades foram consideradas na Seção 3.2 como base para adaptar o mecanismo de anotação ao domínio da privacidade de dados e à OntoPrivacy.

## 3. Uso no domínio da privacidade

### `x-refersTo`

Uso principal neste projeto: associar schemas, propriedades ou schemas de parâmetros a conceitos como `Dado Pessoal (DP)`, `Pessoa Natural` e `Pessoa Jurídica`.

```yaml
cpf:
  type: string
  x-refersTo: ["Dado Pessoal (DP)"]
```

### `x-kindOf`

Pode ser empregada quando o elemento técnico representa uma especialização de um conceito ontológico mais geral, sem que seja apropriado tratá-lo como equivalência direta.

### `x-mapsTo`

Pode ser usada para indicar equivalência semântica entre elementos da descrição. Seu emprego requer cuidado para não confundir semelhança lexical com equivalência conceitual.

### `x-collectionOn`

Adequada a estruturas de coleção quando se pretende explicitar semanticamente o tipo de seus elementos.

### `x-onResource`

Voltada à associação de tags a recursos descritos pela API.

### `x-operationType`

Uso principal neste projeto: associar uma operação HTTP a uma ou mais operações de tratamento representadas pela OntoPrivacy.

```yaml
post:
  x-operationType:
    - "Operação de TDP"
    - "Coleta"
    - "Armazenamento"
```

## 4. Extensões efetivamente empregadas no Estudo I

> [!IMPORTANT]
> Embora a abordagem geral considere as seis propriedades, **a aplicação na API Pix empregou somente `x-refersTo` e `x-operationType`**.

| Propriedade | Ocorrências no Estudo I |
|---|---:|
| `x-operationType` | 19 |
| `x-refersTo` | 10 |
| `x-kindOf` | 0 |
| `x-mapsTo` | 0 |
| `x-collectionOn` | 0 |
| `x-onResource` | 0 |

## 5. Representação dos valores

No Estudo I, os valores são rótulos textuais da OntoPrivacy, normalmente registrados em arrays YAML. Essa estratégia favorece legibilidade e inspeção, porém possui limitações importantes:

- depende da grafia do rótulo;
- não expressa condição ou grau de certeza;
- não representa formalmente a perspectiva do participante;
- não substitui identificadores ontológicos processáveis;
- não habilita inferência automática.

## 6. Regra de utilização

Uma extensão não deve ser inserida apenas porque o elemento técnico *poderia* estar relacionado a um conceito. O vínculo precisa ser sustentado pelo conteúdo da especificação e pelos critérios definidos em `A03_CRITERIOS_DE_MAPEAMENTO.md`.
