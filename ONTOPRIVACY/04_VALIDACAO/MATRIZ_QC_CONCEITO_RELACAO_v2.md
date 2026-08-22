# Matriz QC–Conceito–Relação — OntoPrivacy v2

## Visão sintética

| QC | Conceitos | Relações | Cenários | Resposta exemplificativa | Resultado |
| --- | --- | --- | --- | --- | --- |
| QC1 | C13 Dado; C14 Dado Pessoal (DP); C15 DP Sensível; C16 DP Etnia; C17 DP Religião; C18 DP Político; C19 DP Saúde; C20 DP Biométrico; C21 Dado Pseudonimizado; C22 Dado Anonimizado; C23 Anonimidade; C24 Conjunto de Dados; C25 Banco de Dados DP | R01 integra (Dado–Conjunto de Dados); R02 integra (Dado Pessoal–Banco de Dados DP); R06 caracteriza | SC-QC1-P; SC-QC1-L | No cenário, D-CPF e D-E-mail são Dados Pessoais; D-Saúde é DP Sensível/DP Saúde; D-Código é Dado Pseudonimizado; D-Estatística é Dado Anonimizado caracterizado por Anonimidade. D-CPF, D-E-mail, D-Saúde e D-Código integram BDP-Matrículas; D-Estatística integra CD-Indicadores, mas não o Banco de Dados DP. | Respondível integralmente; classificação e pertencimento são expressos pelos conceitos e por R01, R02 e R06. |
| QC2 | C02 Pessoa Natural; C12 Titular de DP; C14 Dado Pessoal (DP); C21 Dado Pseudonimizado; C26 Identificabilidade; C27 Identificabilidade Direta; C28 Identificabilidade Indireta | R05 baseia-se; R09 identifica; R13 refere-se a (Dado Pessoal–Titular) | SC-QC2-P; SC-QC2-L | D-CPF refere-se a Ana por IDIR-01, uma Identificabilidade Direta. D-Código refere-se à mesma Titular por IIND-01, uma Identificabilidade Indireta baseada no código e na tabela de correspondência separada. | Respondível integralmente; o relator Identificabilidade sustenta o vínculo dado–Titular e distingue as modalidades direta e indireta. |
| QC3 | C01 Agente Legal; C02 Pessoa Natural; C03 Pessoa Jurídica; C04 Entidade Organizacional; C05 Agência; C06 Autoridade Pública; C07 Parte Interessada na Privacidade; C08 Agente de Tratamento; C09 Controlador; C10 Operador; C11 Terceiro; C12 Titular de DP; C29 Tratamento de Dados Pessoais (TDP) | R08 envolve; R10 instrui; R11 realiza; R21 é responsável pelo | SC-QC3-P; SC-QC3-L | Em TDP-Matrícula, Ana é Pessoa Natural e Titular; Instituto Alfa é Pessoa Jurídica/Entidade Organizacional e Controlador; Nuvem Beta é Pessoa Jurídica/Entidade Organizacional e Operador; todos são Partes Interessadas. Em TDP-Bolsas, Agência Alfa atua como Controlador e Autoridade Delta participa como Terceiro. O Controlador é responsável pelos TDPs e, quando representado, instrui o Operador, que realiza o tratamento. | Respondível integralmente; os papéis são contextuais e não são inferidos de perfis ou componentes técnicos. |
| QC4 | C14 Dado Pessoal (DP); C29 Tratamento de Dados Pessoais (TDP); C30 Operação de TDP; C31 Conjunto de Operações de TDP; C32 Coleta; C33 Armazenamento; C34 Alteração; C35 Recuperação; C36 Consulta; C37 Divulgação; C38 Disponibilização; C39 Exclusão; C40 Anonimização; C41 Pseudonimização | R03 é composto por; R04 abrange; R08 envolve; R11 realiza; R21 é responsável pelo | SC-QC4-P; SC-QC4-L | TDP-Matrícula abrange D-CPF, D-E-mail e D-Saúde e é um Conjunto de Operações de TDP composto por OP-Coleta, OP-Armazenamento e OP-Consulta. Instituto Alfa é responsável pelo tratamento e Nuvem Beta realiza as operações que lhe foram atribuídas. | Respondível integralmente; a ontologia distingue TDP unitário e composto e permite indicar as operações específicas. |
| QC5 | C09 Controlador; C12 Titular de DP; C29 Tratamento de Dados Pessoais (TDP); C43 Finalidade | R07 define; R18 é informada ao; R20 é orientado por | SC-QC5-P; SC-QC5-L | TDP-Matrícula é orientado por F-Matrícula (“processar a inscrição e emitir o certificado”), definida pelo Instituto Alfa e informada a Ana. TDP-Marketing é orientado por F-Marketing (“enviar comunicações promocionais sobre novos cursos”), também definida pelo Instituto e informada à Titular. | Respondível integralmente; Finalidade está explicitamente representada como modo do TDP e coberta também pela QC6. |
| QC6 | C09 Controlador; C12 Titular de DP; C29 Tratamento de Dados Pessoais (TDP); C42 Consentimento; C43 Finalidade | R12 refere-se a (Consentimento–Finalidade); R16 tem escopo; R17 é dirigido a; R19 é manifestado por | SC-QC6-P; SC-QC6-L | C-01 é manifestado por Ana, dirigido ao Instituto Alfa, tem TDP-Marketing em seu escopo e refere-se à F-Marketing. A resposta descreve a estrutura representada, sem concluir que o consentimento é juridicamente válido ou que o tratamento é lícito. | Respondível integralmente; nenhuma relação exige Base Legal, Ator Autorizado, Ator Desautorizado ou TDP Autorizado. |
| QC7 | C14 Dado Pessoal (DP); C21 Dado Pseudonimizado; C22 Dado Anonimizado; C23 Anonimidade; C28 Identificabilidade Indireta; C29 Tratamento de Dados Pessoais (TDP); C30 Operação de TDP; C40 Anonimização; C41 Pseudonimização | R04 abrange; R05 baseia-se; R06 caracteriza; R14 resulta em (Anonimização); R15 resulta em (Pseudonimização) | SC-QC7-P; SC-QC7-L | OP-Pseudonimização abrange D-CPF e resulta em D-Código, que permanece Dado Pessoal e participa de Identificabilidade Indireta. OP-Anonimização abrange dados do estudo e resulta em D-Estatística, um Dado Anonimizado caracterizado por Anonimidade. | Respondível integralmente; a ontologia separa as operações, os resultados e as condições remanescentes. |

## Mapeamento normalizado QC–Conceito

| QC | ID | Conceito | Papel na resposta |
| --- | --- | --- | --- |
| QC1 | C13 | Dado | tipo fundamental de dado |
| QC1 | C14 | Dado Pessoal (DP) | papel de dado pessoal |
| QC1 | C15 | DP Sensível | categoria sensível abstrata |
| QC1 | C16 | DP Etnia | categoria sensível étnica |
| QC1 | C17 | DP Religião | categoria sensível religiosa |
| QC1 | C18 | DP Político | categoria sensível política |
| QC1 | C19 | DP Saúde | categoria sensível de saúde |
| QC1 | C20 | DP Biométrico | categoria sensível biométrica |
| QC1 | C21 | Dado Pseudonimizado | dado pseudonimizado |
| QC1 | C22 | Dado Anonimizado | dado anonimizado |
| QC1 | C23 | Anonimidade | modo de anonimidade |
| QC1 | C24 | Conjunto de Dados | coletivo de dados |
| QC1 | C25 | Banco de Dados DP | banco estruturado de dados pessoais |
| QC2 | C02 | Pessoa Natural | provedor de identidade do Titular |
| QC2 | C12 | Titular de DP | papel do titular identificado |
| QC2 | C14 | Dado Pessoal (DP) | dado que sustenta a identificação |
| QC2 | C21 | Dado Pseudonimizado | caso de identificabilidade indireta |
| QC2 | C26 | Identificabilidade | relator central |
| QC2 | C27 | Identificabilidade Direta | modalidade direta |
| QC2 | C28 | Identificabilidade Indireta | modalidade indireta |
| QC3 | C01 | Agente Legal | categoria de participantes jurídicos |
| QC3 | C02 | Pessoa Natural | pessoa natural |
| QC3 | C03 | Pessoa Jurídica | pessoa jurídica |
| QC3 | C04 | Entidade Organizacional | organização jurídica |
| QC3 | C05 | Agência | tipo organizacional Agência |
| QC3 | C06 | Autoridade Pública | tipo organizacional Autoridade Pública |
| QC3 | C07 | Parte Interessada na Privacidade | papel geral de participante |
| QC3 | C08 | Agente de Tratamento | papel geral dos agentes de tratamento |
| QC3 | C09 | Controlador | papel decisório |
| QC3 | C10 | Operador | papel executor |
| QC3 | C11 | Terceiro | papel de terceiro |
| QC3 | C12 | Titular de DP | papel do titular |
| QC3 | C29 | Tratamento de Dados Pessoais (TDP) | contexto relacional do tratamento |
| QC4 | C14 | Dado Pessoal (DP) | objeto pessoal abrangido |
| QC4 | C29 | Tratamento de Dados Pessoais (TDP) | relator do tratamento |
| QC4 | C30 | Operação de TDP | tratamento unitário |
| QC4 | C31 | Conjunto de Operações de TDP | tratamento composto |
| QC4 | C32 | Coleta | operação Coleta |
| QC4 | C33 | Armazenamento | operação Armazenamento |
| QC4 | C34 | Alteração | operação Alteração |
| QC4 | C35 | Recuperação | operação Recuperação |
| QC4 | C36 | Consulta | operação Consulta |
| QC4 | C37 | Divulgação | operação Divulgação |
| QC4 | C38 | Disponibilização | operação Disponibilização |
| QC4 | C39 | Exclusão | operação Exclusão |
| QC4 | C40 | Anonimização | operação Anonimização |
| QC4 | C41 | Pseudonimização | operação Pseudonimização |
| QC5 | C09 | Controlador | Controlador que define |
| QC5 | C12 | Titular de DP | Titular informado |
| QC5 | C29 | Tratamento de Dados Pessoais (TDP) | portador relacional da finalidade |
| QC5 | C43 | Finalidade | propósito do tratamento |
| QC6 | C09 | Controlador | destinatário do Consentimento |
| QC6 | C12 | Titular de DP | Titular manifestante |
| QC6 | C29 | Tratamento de Dados Pessoais (TDP) | TDP no escopo |
| QC6 | C42 | Consentimento | relator Consentimento |
| QC6 | C43 | Finalidade | Finalidade referida |
| QC7 | C14 | Dado Pessoal (DP) | dado pessoal de entrada |
| QC7 | C21 | Dado Pseudonimizado | resultado pseudonimizado |
| QC7 | C22 | Dado Anonimizado | resultado anonimizado |
| QC7 | C23 | Anonimidade | condição de anonimidade |
| QC7 | C28 | Identificabilidade Indireta | condição de identificabilidade indireta |
| QC7 | C29 | Tratamento de Dados Pessoais (TDP) | tratamento relacional |
| QC7 | C30 | Operação de TDP | operação de tratamento |
| QC7 | C40 | Anonimização | operação de anonimização |
| QC7 | C41 | Pseudonimização | operação de pseudonimização |

## Mapeamento normalizado QC–Relação

| QC | ID | Relação | Papel na resposta |
| --- | --- | --- | --- |
| QC1 | R01 | integra (Dado–Conjunto de Dados) | pertencimento de Dado a Conjunto |
| QC1 | R02 | integra (Dado Pessoal–Banco de Dados DP) | pertencimento de Dado Pessoal a Banco |
| QC1 | R06 | caracteriza | caracterização do dado anonimizado |
| QC2 | R05 | baseia-se | dados que sustentam a Identificabilidade |
| QC2 | R09 | identifica | Titular identificado pelo relator |
| QC2 | R13 | refere-se a (Dado Pessoal–Titular) | vínculo material Dado Pessoal–Titular |
| QC3 | R08 | envolve | participação no TDP |
| QC3 | R10 | instrui | instrução Controlador–Operador |
| QC3 | R11 | realiza | realização do TDP pelo Operador |
| QC3 | R21 | é responsável pelo | responsabilidade do Controlador |
| QC4 | R03 | é composto por | composição do tratamento composto |
| QC4 | R04 | abrange | dados abrangidos pelo TDP |
| QC4 | R08 | envolve | participantes envolvidos |
| QC4 | R11 | realiza | Operador que realiza |
| QC4 | R21 | é responsável pelo | Controlador responsável |
| QC5 | R07 | define | Controlador define Finalidade |
| QC5 | R18 | é informada ao | Finalidade informada ao Titular |
| QC5 | R20 | é orientado por | Finalidade orienta o TDP |
| QC6 | R12 | refere-se a (Consentimento–Finalidade) | Consentimento refere-se à Finalidade |
| QC6 | R16 | tem escopo | TDP no escopo |
| QC6 | R17 | é dirigido a | dirigido ao Controlador |
| QC6 | R19 | é manifestado por | manifestado pelo Titular |
| QC7 | R04 | abrange | Dados Pessoais abrangidos |
| QC7 | R05 | baseia-se | Identificabilidade sustentada pelo resultado pseudonimizado |
| QC7 | R06 | caracteriza | Anonimidade caracteriza o resultado anonimizado |
| QC7 | R14 | resulta em (Anonimização) | resultado da Anonimização |
| QC7 | R15 | resulta em (Pseudonimização) | resultado da Pseudonimização |