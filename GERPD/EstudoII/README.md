# Estudo II - Aplicação demonstrativa do GERPD com apoio do ChatGPT no projeto Tibico

## Objetivo

Este diretório disponibiliza os materiais necessários para compreender, auditar e reproduzir metodologicamente o **Estudo II**, no qual o GERPD v1.0 foi aplicado integralmente, com apoio do ChatGPT, a artefatos de Engenharia de Software do projeto acadêmico Tibico.

O estudo percorreu as oito etapas do GERPD, registrou as saídas intermediárias, consolidou os resultados na Matriz Padrão de Aplicação - MPA, executou uma autoverificação diagnóstica e realizou posteriormente uma revisão humana controlada.

## Delineamento

- Uma aplicação formal completa.
- Uma única conversa e contexto acumulado.
- Prompts congelados P00 a P10.
- P01 a P08: oito etapas do GERPD.
- P09: consolidação posterior na MPA.
- P10: autoverificação diagnóstica.
- Revisão humana realizada somente após o encerramento de P10.
- Saídas brutas preservadas e separadas do estado revisado.

## Corpus e instrumentos

O corpus formal é composto exclusivamente por:

- C01 - Documento de Requisitos do Tibico v1.3.
- C02 - Documento de Especificação de Requisitos do Tibico v1.2.

Os instrumentos congelados são:

- M01 - GERPD v1.0.
- S01 - OntoPrivacy v1.

## Resultados centrais

| Elemento | Estado bruto | Estado revisado |
|---|---:|---:|
| Dados pessoais - DP | 37 | 37 |
| Participantes/papéis - AG | 9 | 9 |
| Operações - OP | 41 | 41, com refinamentos conceituais |
| Finalidades/condições - FA | 43 | 43, com ajustes |
| Requisitos candidatos - RP | 45 | 47 |
| Pontos de atenção - PA | 20 | 21 |
| Registros MPA | 68 | 71 |
| Adendos de Retorno - AR | 7 | preservados |
| Ajustes humanos consolidados - RH | - | 10 |

Na revisão dos 68 registros da MPA bruta: **28 foram Aceitos, 39 Aceitos com ajustes, 1 permaneceu Pendente de validação e 0 foram Rejeitados integralmente**. Essas proporções descrevem esta aplicação específica e **não representam taxa de acurácia, erro ou desempenho geral do ChatGPT**.

## Estrutura de diretórios

- `00_Documentacao/`: protocolo congelado, metadados, glossário e mapa dos artefatos.
- `01_Corpus_e_Instrumentos/`: quatro arquivos efetivamente utilizados na execução formal.
- `02_Prompts/`: textos P00-P10 extraídos do protocolo congelado.
- `03_Respostas_Brutas/`: respostas completas e não editadas P00-P10.
- `04_Saidas_Etapas/`: saídas completas das oito etapas e síntese do estado bruto acumulado.
- `05_Adendos_Retorno/`: AR-01 a AR-07.
- `06_Rastreabilidade/`: Matriz de Rastreabilidade bruta acumulada e revisada.
- `07_Revisao_Humana/`: RH-01 a RH-10 e estado humano revisado.
- `08_MPA/`: MPA bruta e MPA revisada.
- `09_Autoverificacao/`: relatório completo do Prompt 10.
- `10_Indicadores/`: indicadores em formatos XLSX, CSV, JSON e Markdown.
- `11_Figuras/`: figuras do Estudo II disponíveis como arquivos independentes.
- `12_Reprodutibilidade/`: instruções de reprodução, manifesto, versionamento e relação com a Seção 4.3.

## Limites de interpretação

O estudo não tem como finalidade comprovar conformidade integral do Tibico com a LGPD, medir a usabilidade do GERPD, avaliar desempenho geral do ChatGPT, comparar modelos/ferramentas de IA ou demonstrar causalidade estatística.

## Integridade

As respostas P00-P10 foram copiadas sem edição para `03_Respostas_Brutas/`. Não foram executados nem incluídos checksums SHA-256 neste pacote, conforme decisão expressa do usuário na preparação do repositório.
