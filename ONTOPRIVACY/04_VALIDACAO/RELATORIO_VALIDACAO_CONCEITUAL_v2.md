# Relatório de Validação Conceitual — OntoPrivacy v2

## 1. Método

A validação foi executada por rastreamento das QCs aos conceitos, relações, conjuntos e limites documentados nos Gates G1 e G2, seguido de instanciação conceitual em cenários positivos e negativos/limítrofes. Não foi utilizado raciocinador automático, e nenhuma alteração estrutural foi introduzida.

## 2. Respostas exemplificativas

| QC | Versão objetiva | Resposta por instâncias | Resultado |
| --- | --- | --- | --- |
| QC1 | Quais dados são pessoais, sensíveis, pseudonimizados ou anonimizados, e em quais coleções estão organizados? | No cenário, D-CPF e D-E-mail são Dados Pessoais; D-Saúde é DP Sensível/DP Saúde; D-Código é Dado Pseudonimizado; D-Estatística é Dado Anonimizado caracterizado por Anonimidade. D-CPF, D-E-mail, D-Saúde e D-Código integram BDP-Matrículas; D-Estatística integra CD-Indicadores, mas não o Banco de Dados DP. | Respondível integralmente; classificação e pertencimento são expressos pelos conceitos e por R01, R02 e R06. |
| QC2 | A quem cada dado pessoal se refere e como ocorre a identificação: direta ou indireta? | D-CPF refere-se a Ana por IDIR-01, uma Identificabilidade Direta. D-Código refere-se à mesma Titular por IIND-01, uma Identificabilidade Indireta baseada no código e na tabela de correspondência separada. | Respondível integralmente; o relator Identificabilidade sustenta o vínculo dado–Titular e distingue as modalidades direta e indireta. |
| QC3 | Quem participa do tratamento e qual papel desempenha? | Em TDP-Matrícula, Ana é Pessoa Natural e Titular; Instituto Alfa é Pessoa Jurídica/Entidade Organizacional e Controlador; Nuvem Beta é Pessoa Jurídica/Entidade Organizacional e Operador; todos são Partes Interessadas. Em TDP-Bolsas, Agência Alfa atua como Controlador e Autoridade Delta participa como Terceiro. O Controlador é responsável pelos TDPs e, quando representado, instrui o Operador, que realiza o tratamento. | Respondível integralmente; os papéis são contextuais e não são inferidos de perfis ou componentes técnicos. |
| QC4 | Quais operações de tratamento são realizadas sobre os dados pessoais? | TDP-Matrícula abrange D-CPF, D-E-mail e D-Saúde e é um Conjunto de Operações de TDP composto por OP-Coleta, OP-Armazenamento e OP-Consulta. Instituto Alfa é responsável pelo tratamento e Nuvem Beta realiza as operações que lhe foram atribuídas. | Respondível integralmente; a ontologia distingue TDP unitário e composto e permite indicar as operações específicas. |
| QC5 | Para qual finalidade o tratamento é realizado, quem a define e a quem é informada? | TDP-Matrícula é orientado por F-Matrícula (“processar a inscrição e emitir o certificado”), definida pelo Instituto Alfa e informada a Ana. TDP-Marketing é orientado por F-Marketing (“enviar comunicações promocionais sobre novos cursos”), também definida pelo Instituto e informada à Titular. | Respondível integralmente; Finalidade está explicitamente representada como modo do TDP e coberta também pela QC6. |
| QC6 | Quem consente com qual tratamento, perante qual controlador e para quais finalidades? | C-01 é manifestado por Ana, dirigido ao Instituto Alfa, tem TDP-Marketing em seu escopo e refere-se à F-Marketing. A resposta descreve a estrutura representada, sem concluir que o consentimento é juridicamente válido ou que o tratamento é lícito. | Respondível integralmente; nenhuma relação exige Base Legal, Ator Autorizado, Ator Desautorizado ou TDP Autorizado. |
| QC7 | Que dados resultam da anonimização ou pseudonimização e qual condição de identificação permanece? | OP-Pseudonimização abrange D-CPF e resulta em D-Código, que permanece Dado Pessoal e participa de Identificabilidade Indireta. OP-Anonimização abrange dados do estudo e resulta em D-Estatística, um Dado Anonimizado caracterizado por Anonimidade. | Respondível integralmente; a ontologia separa as operações, os resultados e as condições remanescentes. |

## 3. Resultados dos cenários

| QC | Cenário positivo | Cenário negativo/limítrofe | Conclusão |
| --- | --- | --- | --- |
| QC1 | SC-QC1-P | SC-QC1-L | A capacidade de resposta e o limite de inferência foram demonstrados. |
| QC2 | SC-QC2-P | SC-QC2-L | A capacidade de resposta e o limite de inferência foram demonstrados. |
| QC3 | SC-QC3-P | SC-QC3-L | A capacidade de resposta e o limite de inferência foram demonstrados. |
| QC4 | SC-QC4-P | SC-QC4-L | A capacidade de resposta e o limite de inferência foram demonstrados. |
| QC5 | SC-QC5-P | SC-QC5-L | A capacidade de resposta e o limite de inferência foram demonstrados. |
| QC6 | SC-QC6-P | SC-QC6-L | A capacidade de resposta e o limite de inferência foram demonstrados. |
| QC7 | SC-QC7-P | SC-QC7-L | A capacidade de resposta e o limite de inferência foram demonstrados. |

## 4. Limites de escopo registrados

| ID | QCs | Limite | Classificação | Impacto | Bloqueia o Gate? |
| --- | --- | --- | --- | --- | --- |
| LIM-QC-01 | QC1–QC7 | A OntoPrivacy v2 é uma ontologia de referência conceitual, sem linguagem operacional de consulta ou raciocinador incorporado. | Limite metodológico | As respostas são demonstradas por instanciação e inspeção conceitual, não por execução automática. | Não |
| LIM-QC-02 | QC2; QC7 | O contexto, os meios razoáveis e a parte capaz de identificar não são representados explicitamente. | Limite de escopo adiado | A Identificabilidade e a Anonimidade são avaliadas em contexto previamente delimitado. | Não |
| LIM-QC-03 | QC1 | A cobertura das categorias de DP Sensível é deliberadamente parcial. | Limite de cobertura adiado | A QC identifica as categorias presentes no modelo, sem afirmar exaustividade legal. | Não |
| LIM-QC-04 | QC5; QC6 | Base Legal, licitude, conformidade e validade jurídica não integram o modelo. | Exclusão deliberada de escopo | As QCs representam Finalidade e Consentimento, mas não concluem autorização jurídica. | Não |
| LIM-QC-05 | QC3; QC6 | Ator Autorizado, Ator Desautorizado e TDP Autorizado permanecem excluídos. | Decisão fixa | Autorização técnica ou jurídica não é confundida com papel ontológico ou Consentimento. | Não |
| LIM-QC-06 | QC6 | Ciclo de vida, revogação, prova e validade temporal do Consentimento não são modelados. | Evolução futura | A QC responde apenas à estrutura relacional estática representada. | Não |
| LIM-QC-07 | QC5 | A ontologia não avalia automaticamente se a Finalidade é legítima, específica ou suficientemente explícita. | Limite normativo | A QC identifica a Finalidade e seus vínculos; a avaliação jurídica permanece externa. | Não |
| LIM-QC-08 | QC3; QC4 | Métodos HTTP, perfis, componentes e nomes técnicos não determinam sozinhos papéis ou operações. | Regra de evidência | A validação exige contexto funcional e participante jurídico explicitado. | Não |
| LIM-QC-09 | QC7 | A ontologia distingue operação, resultado e condição, mas não modela métricas ou graus de anonimização. | Limite de escopo | A resposta é categorial, não quantitativa. | Não |

## 5. Cobertura do núcleo

- Conceitos mobilizados: **43/43**.
- Relações mobilizadas: **21/21**.
- Conceitos não mobilizados: **nenhum**.
- Relações não mobilizadas: **nenhuma**.
- Finalidade é coberta diretamente pela QC5 e referenciada novamente na QC6.

## 6. Parecer

Todas as sete QCs são conceitualmente respondíveis. Nenhuma exige Base Legal, Ator Autorizado, Ator Desautorizado ou TDP Autorizado. Os cenários podem ser representados sem modificação silenciosa da OntoPrivacy v2. Os limites identificados são não bloqueadores e foram classificados como decisões de escopo, limitações metodológicas ou evoluções futuras.