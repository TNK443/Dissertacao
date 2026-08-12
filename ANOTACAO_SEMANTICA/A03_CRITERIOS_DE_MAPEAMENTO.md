# A03 — Critérios de mapeamento entre OpenAPI e OntoPrivacy

## 1. Finalidade

Este documento consolida regras de decisão empregadas para tornar a anotação mais controlada, rastreável e conservadora. Os critérios foram sistematizados a partir da abordagem da Seção 3.2 e das decisões observadas no Estudo I.

## 2. Regra geral

> **Anotar somente quando houver evidência suficiente no artefato analisado.**

Quando a informação for condicional, ambígua ou depender de contexto externo, a decisão adequada é não inserir uma classificação categórica e registrar a questão como ponto de validação, quando relevante.

## 3. Critérios

### C01 — O método HTTP não determina sozinho a operação de tratamento

`GET`, `POST`, `PUT`, `PATCH` e `DELETE` fornecem apenas uma orientação inicial. A classificação deve considerar:

- descrição funcional;
- `requestBody`;
- respostas;
- schemas;
- referências `$ref`;
- efeito exposto pela interface.

### C02 — Percorrer cadeias `$ref`

Quando os dados não estiverem visíveis diretamente na operação, as referências internas devem ser percorridas até os componentes efetivamente utilizados.

### C03 — Distinguir dado, entidade e papel

Um valor de CPF pode ser associado a `Dado Pessoal (DP)`, mas não deve ser classificado como `Pessoa Natural`, `Titular de Dados Pessoais` ou `Titular Identificável` apenas por conter um identificador.

Um schema agregado que represente uma pessoa física pode, havendo evidência, ser associado a `Pessoa Natural`.

### C04 — Papéis dependem de contexto relacional

Conceitos como `Titular`, `Controlador`, `Operador` e outros papéis não devem ser atribuídos sem evidência suficiente da relação que fundamenta o papel.

### C05 — Leitura pode envolver duas perspectivas

Uma operação de leitura pode representar:

- `Consulta`, do ponto de vista do consumidor que solicita o recurso;
- `Disponibilização`, do ponto de vista do provedor que entrega os dados na resposta.

A utilização conjunta depende da evidência disponível na operação.

### C06 — Criação e envio podem envolver Coleta; persistência explícita pode justificar Armazenamento

A presença de `POST` ou `PUT` não implica automaticamente `Coleta` e `Armazenamento`. O significado funcional e o recurso criado devem sustentar a associação.

### C07 — Revisão de recurso deve ser interpretada pelo efeito

Operações de revisão como `PATCH` podem ser associadas a `Alteração` quando modificam informações existentes. O rótulo resulta do efeito descrito, não do verbo HTTP isolado.

### C08 — Remoção pode representar Exclusão quando o objeto removido é pertinente ao escopo

Uma operação `DELETE` somente deve ser anotada como `Exclusão` quando a remoção descrita envolver elemento que sustente a relação com o tratamento de dados considerado.

### C09 — Autenticação e autorização técnicas não comprovam TDP Autorizado

OAuth, certificados, escopos ou regras de acesso controlam o uso técnico da API, mas não demonstram isoladamente:

- consentimento;
- base legal;
- outra condição jurídica de legitimidade;
- `Tratamento de Dados Pessoais Autorizado`.

### C10 — Elementos condicionais devem permanecer condicionais

A Chave Pix é um exemplo central: pode assumir CPF, telefone, e-mail, CNPJ ou chave aleatória. Por isso, a categoria `Dado Pessoal` não pode ser aplicada universalmente ao campo sem informação adicional sobre a instância e seu titular.

### C11 — Preferir o ponto semântico responsável pela definição do dado

Quando um parâmetro reutiliza um Schema Object, a anotação deve preferencialmente ficar no elemento responsável pela definição do tipo, evitando duplicação desnecessária em diferentes níveis do documento.

### C12 — Ausência de anotação não significa ausência de tratamento

Uma operação não anotada significa apenas que, no escopo e nas evidências analisadas, não houve fundamento suficiente para inserir a anotação.

## 4. Matriz rápida de decisão

| Situação | Decisão recomendada |
|---|---|
| CPF explicitamente representado | associar a `Dado Pessoal (DP)` |
| schema `PessoaFisica` | associar a `Pessoa Natural`, se o schema representar a entidade |
| `GET` que retorna dados pessoais | avaliar `Consulta` + `Disponibilização` |
| `PATCH` que revisa cobrança | avaliar `Alteração` |
| OAuth presente | não inferir `TDP Autorizado` |
| Chave Pix sem tipo/titular definido | ponto de validação / sem classificação universal |
| identificador transacional sem vínculo explícito à pessoa natural | não anotar como dado pessoal sem evidência adicional |
| dado/efeito somente visível via `$ref` | percorrer referências antes da decisão |

## 5. Estados possíveis da decisão

Para registro reprodutível, recomenda-se utilizar três estados:

- **Anotado:** evidência suficiente e extensão inserida;
- **Não anotado — evidência insuficiente:** nenhuma associação categórica sustentada;
- **Ponto de validação:** relação plausível, mas dependente de contexto ou evidência adicional.

Esses estados são empregados no arquivo `EstudoI/R02_REGISTRO_MAPEAMENTO_ANOTACOES.csv`.
