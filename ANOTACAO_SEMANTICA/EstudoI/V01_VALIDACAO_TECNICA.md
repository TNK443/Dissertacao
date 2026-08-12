# V01 — Validação técnica do Estudo I

## 1. Objetivo

Este registro documenta as verificações executadas sobre a especificação original da API Pix e a versão final anotada incluídas neste pacote. O objetivo é confirmar a preservação estrutural do contrato OpenAPI e reproduzir as contagens apresentadas no Estudo I.

**Arquivos verificados:**

- `C01_API_PIX_Release_2.6.1.yaml`;
- `R01_API_PIX_Anotado.yaml`.

## 2. Resultado geral

**Situação: APROVADO.** As verificações estruturais e quantitativas definidas para o pacote foram satisfeitas.

## 3. Verificações realizadas

| Verificação | Original | Anotado | Resultado |
|---|---:|---:|---|
| OpenAPI | 3.0.0 | 3.0.0 | conforme |
| Versão da API | 2.6.1 | 2.6.1 | conforme |
| Paths | 16 | 16 | preservado |
| Operações HTTP | 27 | 27 | preservado |
| Schemas | 67 | 67 | preservado |
| Referências internas `$ref` | 373 | 373 | preservado |
| Referências internas quebradas | 0 | 0 | nenhuma |

## 4. Anotações semânticas

| Indicador | Resultado |
|---|---:|
| `x-operationType` | 19 |
| `x-refersTo` | 10 |
| Total de propriedades semânticas | 29 |
| Associações conceituais | 65 |
| Operações anotadas | 19 |
| Operações sem anotação por ausência de evidência suficiente | 6 |
| Operações em ponto de validação | 2 |

## 5. Equivalência estrutural

Após a retirada lógica de `x-refersTo` e `x-operationType`, a estrutura carregada da versão anotada foi comparada com a especificação oficial preservada. Para evitar que diferenças exclusivamente de espaçamento em textos descritivos fossem confundidas com alteração funcional, o conteúdo textual foi normalizado apenas para fins da comparação.

**Resultado:** equivalente.

Isso confirma, no escopo da verificação realizada, que as anotações foram acrescentadas sem modificar paths, operações, schemas ou referências internas da especificação-base.

## 6. Frequência dos conceitos registrados

| Conceito registrado no YAML | Quantidade |
|---|---:|
| `Operação de TDP` | 19 |
| `Consulta` | 10 |
| `Disponibilização` | 10 |
| `Dado Pessoal (DP)` | 8 |
| `Coleta` | 5 |
| `Armazenamento` | 5 |
| `Alteração` | 5 |
| `Exclusão` | 1 |
| `Pessoa Natural` | 1 |
| `Pessoa Jurídica` | 1 |


## 7. Como reproduzir

Instale as dependências descritas em `../PrivacyFinder/requirements.txt` ou, no mínimo, uma versão compatível de Python e PyYAML. A partir deste diretório, execute:

```bash
python V02_validar_estudo_i.py
```

O script encerra com código `0` quando todas as verificações esperadas são satisfeitas.

## 8. Delimitação

Esta validação confirma propriedades **técnicas e estruturais** do artefato e reproduz as contagens do Estudo I. Ela não valida juridicamente as associações, não certifica conformidade com a LGPD e não substitui revisão conceitual humana.
