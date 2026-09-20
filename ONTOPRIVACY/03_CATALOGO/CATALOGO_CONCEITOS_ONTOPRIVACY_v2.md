# Catálogo de Conceitos - OntoPrivacy v2

Este documento cataloga os 43 conceitos da OntoPrivacy v2. Os códigos C01–C43 são identificadores documentais do catálogo e não alteram a estrutura ou o versionamento do modelo. O mapeamento para QC-P1–QC-P7 é provisório e será validado.

## Template canônico

| Campo | Uso |
| --- | --- |
| ID documental | Identificação interna do catálogo. |
| Conceito | Rótulo canônico do ASTA/PNG. |
| Estereótipo | Classificação OntoUML registrada no ASTA. |
| Abstrato ou concreto | Condição de instanciação registrada no modelo. |
| Definição ontológica | Definição autoral que explicita a decisão conceitual. |
| Definição normativa | Texto-fonte registrado ou indicação transparente de ausência/herança. |
| Fonte | Origem da definição e da classificação. |
| Superconceito/Subconceitos | Hierarquia direta do modelo. |
| Relações | Associações incidentes no conceito. |
| Restrições | Conjuntos de generalização ou restrições próprias. |
| Sinônimos | Rótulos alternativos controlados. |
| Exemplo/Não exemplo | Instâncias ilustrativas autorais. |
| Uso em OpenAPI/GERPD | Orientação de uso alinhada à v2, não evidência histórica. |

## C01 - Agente Legal

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Agentes, pessoas e papéis |
| Estereótipo | «category» |
| Abstrato ou concreto | Abstrato |
| Definição ontológica | Categoria abstrata que reúne Pessoas Naturais e Pessoas Jurídicas enquanto sujeitos capazes de participar de relações e desempenhar papéis relevantes no domínio da privacidade de dados. |
| Definição normativa | Não há definição normativa direta. |
| Fonte | OntoPrivacy v2 |
| Superconceito | - |
| Subconceitos | Parte Interessada na Privacidade; Pessoa Jurídica; Pessoa Natural |
| Relações | - |
| Restrições | GS01 {disjoint, complete} sobre Pessoa Natural; Pessoa Jurídica |
| Sinônimos | Pessoa de Direito; Sujeito de Direito. |
| Exemplo | Maria (Pessoa Natural) ou uma universidade constituída como Pessoa Jurídica, consideradas como participantes possíveis do domínio. |
| Não exemplo | Um endpoint REST ou um banco de dados, que não é sujeito jurídico. |
| QCs relacionadas | QC-P3 |
| Uso previsto em OpenAPI | Condicional: anotar somente quando a especificação fornecer evidência suficiente do participante e de seu papel relacional; não inferir por autenticação, método HTTP ou nome do sistema. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto nas Etapas 1 e 3 para participantes e papéis; apoio às Etapas 4 a 8 para responsabilidade, requisitos e rastreabilidade. |

## C02 - Pessoa Natural

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Agentes, pessoas e papéis |
| Estereótipo | «kind» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Tipo fundamental que representa um ser humano dotado de identidade própria, capaz de desempenhar o papel de Titular de DP e, conforme o contexto, outros papéis do domínio. |
| Definição normativa | Não há definição normativa direta. |
| Fonte | OntoPrivacy v2 |
| Superconceito | Agente Legal |
| Subconceitos | Titular de DP |
| Relações | - |
| Restrições | GS01 membro de {disjoint, complete} |
| Sinônimos | - |
| Exemplo | João, estudante identificado em um processo de matrícula. |
| Não Exemplo | Uma empresa ou um sistema computacional. |
| QCs relacionadas | QC-P2; QC-P3 |
| Uso previsto em OpenAPI | Direto/condicional em Schema Objects, propriedades, parâmetros ou respostas, quando o elemento técnico representar explicitamente o conceito; não inferir papéis apenas pelo nome. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto nas Etapas 1 e 3 para participantes e papéis; apoio às Etapas 4 a 8 para responsabilidade, requisitos e rastreabilidade. |

## C03 - Pessoa Jurídica

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Agentes, pessoas e papéis |
| Estereótipo | «kind» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Tipo fundamental que representa uma organização dotada de personalidade jurídica própria, distinta de seus membros e capaz de desempenhar papéis no domínio da privacidade de dados. |
| Definição normativa | Não há definição normativa direta. |
| Fonte | OntoPrivacy v2 |
| Superconceito | Agente Legal |
| Subconceitos | Entidade Organizacional |
| Relações | - |
| Restrições | GS01 membro de {disjoint, complete} |
| Sinônimos | - |
| Exemplo | Universidade X, com personalidade jurídica própria. |
| Não Exemplo | Um departamento interno sem personalidade jurídica própria. |
| QCs relacionadas | QC-P3 |
| Uso previsto em OpenAPI | Direto/condicional em Schema Objects, propriedades, parâmetros ou respostas, quando o elemento técnico representar explicitamente o conceito; não inferir papéis apenas pelo nome. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto nas Etapas 1 e 3 para participantes e papéis; apoio às Etapas 4 a 8 para responsabilidade, requisitos e rastreabilidade. |

## C04 - Entidade Organizacional

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Agentes, pessoas e papéis |
| Estereótipo | «subkind» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Especialização rígida de Pessoa Jurídica que representa uma organização estruturada para desempenhar funções institucionais, administrativas, econômicas, regulatórias ou sociais. |
| Definição normativa | Não há definição normativa direta. |
| Fonte | OntoPrivacy v2 |
| Superconceito | Pessoa Jurídica |
| Subconceitos | Agência; Autoridade Pública |
| Relações | - |
| Restrições | - |
| Sinônimos | - |
| Exemplo | Uma instituição de ensino constituída como Pessoa Jurídica. |
| Não Exemplo | Uma pessoa humana. |
| QCs relacionadas | QC-P3 |
| Uso previsto em OpenAPI | Direto/condicional em Schema Objects, propriedades, parâmetros ou respostas, quando o elemento técnico representar explicitamente o conceito; não inferir papéis apenas pelo nome. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto nas Etapas 1 e 3 para participantes e papéis; apoio às Etapas 4 a 8 para responsabilidade, requisitos e rastreabilidade. |

## C05 - Agência

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Agentes, pessoas e papéis |
| Estereótipo | «subkind» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Especialização rígida de Entidade Organizacional que representa uma organização pública instituída por norma para desempenhar funções administrativas, regulatórias, executivas ou de prestação de serviços. |
| Definição normativa | Não há definição normativa direta. |
| Fonte | OntoPrivacy v2 |
| Superconceito | Entidade Organizacional |
| Subconceitos | - |
| Relações | - |
| Restrições | - |
| Sinônimos | - |
| Exemplo | Uma agência reguladora pública formalmente instituída. |
| Não Exemplo | Uma equipe temporária criada informalmente dentro de uma empresa. |
| QCs relacionadas | QC-P3 |
| Uso previsto em OpenAPI | Direto/condicional em Schema Objects, propriedades, parâmetros ou respostas, quando o elemento técnico representar explicitamente o conceito; não inferir papéis apenas pelo nome. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto nas Etapas 1 e 3 para participantes e papéis; apoio às Etapas 4 a 8 para responsabilidade, requisitos e rastreabilidade. |

## C06 - Autoridade Pública

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Agentes, pessoas e papéis |
| Estereótipo | «subkind» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Especialização rígida de Entidade Organizacional que representa uma organização pública dotada de competência institucional para exercer poder, supervisão ou função administrativa em determinado domínio. |
| Definição normativa | Não há definição normativa direta. |
| Fonte | OntoPrivacy v2 |
| Superconceito | Entidade Organizacional |
| Subconceitos | - |
| Relações | - |
| Restrições | - |
| Sinônimos | - |
| Exemplo | Uma entidade pública competente para supervisionar determinado domínio. |
| Não Exemplo | Uma empresa privada sem competência pública. |
| QCs relacionadas | QC-P3 |
| Uso previsto em OpenAPI | Direto/condicional em Schema Objects, propriedades, parâmetros ou respostas, quando o elemento técnico representar explicitamente o conceito; não inferir papéis apenas pelo nome. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto nas Etapas 1 e 3 para participantes e papéis; apoio às Etapas 4 a 8 para responsabilidade, requisitos e rastreabilidade. |

## C07 - Parte Interessada na Privacidade

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Agentes, pessoas e papéis |
| Estereótipo | «rolemixin» |
| Abstrato ou concreto | Abstrato |
| Definição ontológica | Papel relacional abstrato desempenhado por um Agente Legal quando ele pode afetar, ser afetado ou perceber-se afetado por uma decisão ou atividade relacionada ao Tratamento de Dados Pessoais. |
| Definição normativa | ABNT NBR ISO/IEC 29100:2020:<br>2.20 PARTE INTERESSADA NA PRIVACIDADE: pessoa natural ou jurídica, autoridade pública, agência ou qualquer outra entidade, que possa afetar, ser afetada ou perceber que é afetada por uma decisão ou atividade relacionada ao tratamento de dados pessoais (DP). |
| Fonte | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020 |
| Superconceito | Agente Legal |
| Subconceitos | Agente de Tratamento; Terceiro; Titular de DP |
| Relações | R08 envolve - Tratamento de Dados Pessoais (TDP) [1..*] |
| Restrições | - |
| Sinônimos | - |
| Exemplo | O Titular, o Controlador ou um Terceiro envolvidos em um TDP específico. |
| Não Exemplo | Uma pessoa sem qualquer vínculo com o TDP analisado. |
| QCs relacionadas | QC-P3; QC-P4 |
| Uso previsto em OpenAPI | Condicional: anotar somente quando a especificação fornecer evidência suficiente do participante e de seu papel relacional; não inferir por autenticação, método HTTP ou nome do sistema. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto nas Etapas 1 e 3 para participantes e papéis; apoio às Etapas 4 a 8 para responsabilidade, requisitos e rastreabilidade. |

## C08 - Agente de Tratamento

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Agentes, pessoas e papéis |
| Estereótipo | «rolemixin» |
| Abstrato ou concreto | Abstrato |
| Definição ontológica | Papel relacional abstrato que reúne Controladores e Operadores envolvidos em Tratamentos de Dados Pessoais. |
| Definição normativa | LGPD - Lei nº 13.709/2018:<br>(Redação dada pela Lei nº 13.853, de 2019) <br><br>(Art. 5º) IX - AGENTES DE TRATAMENTO: o controlador e o operador; |
| Fonte | OntoPrivacy v2; LGPD - Lei nº 13.709/2018 |
| Superconceito | Parte Interessada na Privacidade |
| Subconceitos | Controlador; Operador |
| Relações | - |
| Restrições | GS06 {complete} sobre Controlador; Operador |
| Sinônimos | - |
| Exemplo | Um Controlador ou Operador participante de um TDP. |
| Não Exemplo | O Titular considerado apenas como pessoa a quem os dados se referem. |
| QCs relacionadas | QC-P3; QC-P4 |
| Uso previsto em OpenAPI | Condicional: anotar somente quando a especificação fornecer evidência suficiente do participante e de seu papel relacional; não inferir por autenticação, método HTTP ou nome do sistema. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto nas Etapas 1 e 3 para participantes e papéis; apoio às Etapas 4 a 8 para responsabilidade, requisitos e rastreabilidade. |

## C09 - Controlador

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Agentes, pessoas e papéis |
| Estereótipo | «rolemixin» |
| Abstrato ou concreto | Abstrato |
| Definição ontológica | Papel desempenhado por um Agente Legal que, em relação a determinado TDP, possui competência decisória sobre o tratamento, incluindo a definição de suas Finalidades e de seus meios. |
| Definição normativa | ABNT NBR ISO/IEC 29100:2020:<br>2.8 CONTROLADOR DE DP: PARTE(S) INTERESSADA(S) NA PRIVACIDADE que determina(m) os objetivos e os meios para o tratamento dos DADOS PESSOAIS (DP) e que não é(são) pessoa(s) natural(is) que usa(m) os dados para objetivos pessoais.<br><br>NOTA: Um CONTROLADOR DE DP algumas vezes INSTRUI outros (por exemplo, OPERADORES DE DP) a tratar DP em seu nome, enquanto a responsabilidade pelo tratamento permanece com o CONTROLADOR DE DP.<br><br>LGPD - Lei nº 13.709/2018:<br>(Redação dada pela Lei nº 13.853, de 2019) <br><br>(Art. 5º) VI - CONTROLADOR: pessoa natural ou jurídica, de direito público ou privado, a quem competem as decisões referentes ao tratamento de dados pessoais; |
| Fonte | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020; LGPD - Lei nº 13.709/2018 |
| Superconceito | Agente de Tratamento |
| Subconceitos | - |
| Relações | R07 define - Finalidade [1..*]<br>R10 instrui - Operador [0..*]<br>R17 é dirigido a - Consentimento [0..*]<br>R21 é responsável pelo - Tratamento de Dados Pessoais (TDP) [1..*] |
| Restrições | GS06 membro de {complete} |
| Sinônimos | - |
| Exemplo | A universidade que define a finalidade e os meios do tratamento de dados de matrícula. |
| Não Exemplo | Um fornecedor que apenas executa instruções, sem decidir a finalidade ou os meios. |
| QCs relacionadas | QC-P3; QC-P4; QC-P5; QC-P6 |
| Uso previsto em OpenAPI | Condicional: anotar somente quando a especificação fornecer evidência suficiente do participante e de seu papel relacional; não inferir por autenticação, método HTTP ou nome do sistema. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto nas Etapas 1 e 3 para participantes e papéis; apoio às Etapas 4 a 8 para responsabilidade, requisitos e rastreabilidade. |

## C10 - Operador

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Agentes, pessoas e papéis |
| Estereótipo | «rolemixin» |
| Abstrato ou concreto | Abstrato |
| Definição ontológica | Papel desempenhado por um Agente Legal que realiza determinado TDP em nome do Controlador, observando as instruções recebidas e os limites das Finalidades que orientam o tratamento. |
| Definição normativa | ABNT NBR ISO/IEC 29100:2020:<br>2.10 OPERADOR DE DP: parte interessada na privacidade, que faz o tratamento dos dados pessoais (DP) em benefício e de acordo com as instruções de um controlador de DP.<br><br>NOTA BRASILEIRA: O motivo para a tradução do termo “PII processor” por “operador de DP” é o uso corrente da expressão “operador de DP” no Brasil e sua adoção pela lei brasileira que trata de privacidade e proteção de dados pessoais (Lei 13.709/2018 – Lei Geral de Proteção de Dados Pessoais – LGPD).<br><br>LGPD - Lei nº 13.709/2018:<br>(Redação dada pela Lei nº 13.853, de 2019) <br><br>(Art. 5º) VII - OPERADOR: pessoa natural ou jurídica, de direito público ou privado, que realiza o tratamento de dados pessoais em nome do controlador; |
| Fonte | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020; LGPD - Lei nº 13.709/2018 |
| Superconceito | Agente de Tratamento |
| Subconceitos | - |
| Relações | R10 instrui - Controlador [1..*]<br>R11 realiza - Tratamento de Dados Pessoais (TDP) [1..*] |
| Restrições | GS06 membro de {complete} |
| Sinônimos | - |
| Exemplo | O provedor contratado que processa inscrições em nome da universidade. |
| Não Exemplo | O Titular que apenas fornece seus próprios dados. |
| QCs relacionadas | QC-P3; QC-P4 |
| Uso previsto em OpenAPI | Condicional: anotar somente quando a especificação fornecer evidência suficiente do participante e de seu papel relacional; não inferir por autenticação, método HTTP ou nome do sistema. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto nas Etapas 1 e 3 para participantes e papéis; apoio às Etapas 4 a 8 para responsabilidade, requisitos e rastreabilidade. |

## C11 - Terceiro

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Agentes, pessoas e papéis |
| Estereótipo | «rolemixin» |
| Abstrato ou concreto | Abstrato |
| Definição ontológica | Papel desempenhado por uma Parte Interessada que, no contexto considerado, não atua como Titular, Controlador ou Operador do TDP e não realiza o tratamento em nome do Controlador. |
| Definição normativa | ABNT NBR ISO/IEC 29100:2020:<br>2.25 TERCEIRO: Parte interessada na privacidade que não o titular de dados pessoais (DP), o controlador de DP e o operador de DP, e as pessoas naturais que são autorizadas a tratar os dados sob direta autoridade do controlador de DP ou do operador de DP.<br><br>4.2.4 TERCEIROs: Um terceiro pode receber DP de um controlador de DP ou de um operador de DP. O terceiro não trata DP em nome do controlador de DP. Geralmente, o terceiro se tornará um controlador de DP por si próprio, quando receber os DP em questão. |
| Fonte | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020 |
| Superconceito | Parte Interessada na Privacidade |
| Subconceitos | - |
| Relações | - |
| Restrições | - |
| Sinônimos | - |
| Exemplo | Uma organização que recebe dados e passa a tratá-los por conta própria, sem atuar em nome do Controlador original. |
| Não Exemplo | O próprio Controlador, considerado no mesmo papel e no mesmo TDP. |
| QCs relacionadas | QC-P3 |
| Uso previsto em OpenAPI | Condicional: anotar somente quando a especificação fornecer evidência suficiente do participante e de seu papel relacional; não inferir por autenticação, método HTTP ou nome do sistema. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto nas Etapas 1 e 3 para participantes e papéis; apoio às Etapas 4 a 8 para responsabilidade, requisitos e rastreabilidade. |

## C12 - Titular de DP

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Agentes, pessoas e papéis |
| Estereótipo | «role» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Papel desempenhado por uma Pessoa Natural à qual se referem um ou mais Dados Pessoais, podendo receber informação sobre as Finalidades e manifestar Consentimento quando aplicável. |
| Definição normativa | ABNT NBR ISO/IEC 29100:2020:<br>2.9 TITULAR DE DP: pessoa natural a quem se referem os dados pessoais (DP).<br><br>LGPD - Lei nº 13.709/2018:<br>(Redação dada pela Lei nº 13.853, de 2019) <br><br>(Art. 5º) V - TITULAR: pessoa natural a quem se referem os dados pessoais que são objeto de tratamento; |
| Fonte | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020; LGPD - Lei nº 13.709/2018 |
| Superconceito | Parte Interessada na Privacidade; Pessoa Natural |
| Subconceitos | - |
| Relações | R09 identifica - Identificabilidade [1..*]<br>R13 refere-se a (Dado Pessoal–Titular) - Dado Pessoal (DP) [1..*]<br>R18 é informada ao - Finalidade [0..*]<br>R19 é manifestado por - Consentimento [0..*] |
| Restrições | - |
| Sinônimos | Titular; Titular de Dados Pessoais |
| Exemplo | O aluno a quem se referem nome, CPF e e-mail tratados na matrícula. |
| Não Exemplo | Uma Pessoa Jurídica à qual pertence um CNPJ. |
| QCs relacionadas | QC-P2; QC-P3; QC-P5; QC-P6 |
| Uso previsto em OpenAPI | Condicional: anotar somente quando a especificação fornecer evidência suficiente do participante e de seu papel relacional; não inferir por autenticação, método HTTP ou nome do sistema. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto nas Etapas 2 e 3 para relacionar dados e titulares; repercute nas Etapas 4 a 8. |

## C13 - Dado

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Dados, categorias e coleções |
| Estereótipo | «kind» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Tipo fundamental que representa uma unidade informacional individualizada em determinado contexto, passível de organização, associação, armazenamento ou tratamento. |
| Definição normativa | Não há definição normativa direta. |
| Fonte | OntoPrivacy v2 |
| Superconceito | - |
| Subconceitos | Dado Anonimizado; Dado Pessoal (DP) |
| Relações | R01 integra (Dado–Conjunto de Dados) - Conjunto de Dados [0..*] |
| Restrições | GS02 {disjoint} sobre Dado Pessoal (DP); Dado Anonimizado |
| Sinônimos | - |
| Exemplo | A ocorrência do valor de CPF em um campo de uma requisição JSON. |
| Não Exemplo | A própria Pessoa Natural representada pelo dado. |
| QCs relacionadas | QC-P1 |
| Uso previsto em OpenAPI | Direto/condicional em Schema Objects, propriedades, parâmetros ou respostas, quando o elemento técnico representar explicitamente o conceito; não inferir papéis apenas pelo nome. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto principalmente na Etapa 2; pode fundamentar operações, requisitos e rastreabilidade nas Etapas 4, 6, 7 e 8. |

## C14 - Dado Pessoal (DP)

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Dados, categorias e coleções |
| Estereótipo | «role» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Papel desempenhado por um Dado quando ele participa de uma Identificabilidade que o vincula direta ou indiretamente a um Titular de DP. |
| Definição normativa | ABNT NBR ISO/IEC 29100:2020:<br>2.7 DADOS PESSOAIS (DP): qualquer informação que (a) possa ser usada para identificar a pessoa natural à qual tal informação se relaciona ou (b) pode estar direta ou indiretamente vinculada a uma pessoa natural.<br><br>NOTA: Para determinar se um TITULAR DE DP É IDENTIFICÁVEL, convém que sejam levados em conta todos os meios que possam ser razoavelmente usados pela parte interessada na privacidade, detentora dos dados, ou por qualquer outra parte, para identificar a pessoa natural.<br><br>LGPD - Lei nº 13.709/2018:<br>(Redação dada pela Lei nº 13.853, de 2019) <br><br>(Art. 5º) I - DADO PESSOAL: informação relacionada a pessoa natural identificada ou identificável; |
| Fonte | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020; LGPD - Lei nº 13.709/2018 |
| Superconceito | Dado |
| Subconceitos | DP Sensível; Dado Pseudonimizado |
| Relações | R02 integra (Dado Pessoal–Banco de Dados DP) - Banco de Dados DP [0..*]<br>R04 abrange - Tratamento de Dados Pessoais (TDP) [0..*]<br>R05 baseia-se - Identificabilidade [1..*]<br>R13 refere-se a (Dado Pessoal–Titular) - Titular de DP [1..*] |
| Restrições | GS02 membro de {disjoint} |
| Sinônimos | Dado Pessoal; DP |
| Exemplo | Um CPF que identifica diretamente João. |
| Não Exemplo | Um identificador aleatório sem vínculo razoável com pessoa natural no contexto. |
| QCs relacionadas | QC-P1; QC-P2; QC-P4 |
| Uso previsto em OpenAPI | Direto/condicional em Schema Objects, propriedades, parâmetros ou respostas, quando o elemento técnico representar explicitamente o conceito; não inferir papéis apenas pelo nome. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto principalmente na Etapa 2; pode fundamentar operações, requisitos e rastreabilidade nas Etapas 4, 6, 7 e 8. |

## C15 - DP Sensível

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Dados, categorias e coleções |
| Estereótipo | «role» |
| Abstrato ou concreto | Abstrato |
| Definição ontológica | Papel abstrato especializado de Dado Pessoal cujo conteúdo se enquadra em uma ou mais categorias sensíveis adotadas pela OntoPrivacy. |
| Definição normativa | ABNT NBR ISO/IEC 29100:2020:<br>2.24 DP SENSÍVEIS: categoria de dados pessoais (DP) cuja natureza é sensível, como aqueles que se relacionam à esfera mais íntima do titular de DP ou que podem ter um impacto significativo sobre o titular de DP.<br><br>NOTA: Em algumas jurisdições ou em contextos específicos, DP SENSÍVEIS são definidos com referência à natureza dos DP e podem consistir em DP que revelem a origem racial, opiniões políticas, crenças religiosas ou outras, dados pessoais sobre saúde, vida sexual ou condenações criminais, bem como outros DP que possam ser definidos como sensíveis.<br><br>LGPD - Lei nº 13.709/2018:<br>(Redação dada pela Lei nº 13.853, de 2019) <br><br>(Art. 5º) II - DADO PESSOAL SENSÍVEL: dado pessoal sobre origem racial ou étnica, convicção religiosa, opinião política, filiação a sindicato ou a organização de caráter religioso, filosófico ou político, dado referente à saúde ou à vida sexual, dado genético ou biométrico, quando vinculado a uma pessoa natural; |
| Fonte | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020; LGPD - Lei nº 13.709/2018 |
| Superconceito | Dado Pessoal (DP) |
| Subconceitos | DP Biométrico; DP Etnia; DP Político; DP Religião; DP Saúde |
| Relações | - |
| Restrições | GS07 {overlapping, incomplete} sobre DP Biométrico; DP Etnia; DP Político; DP Religião; DP Saúde |
| Sinônimos | Dado Pessoal Sensível |
| Exemplo | Um diagnóstico médico relacionado a uma pessoa natural. |
| Não Exemplo | Um número interno de produto sem relação com pessoa natural. |
| QCs relacionadas | QC-P1 |
| Uso previsto em OpenAPI | Direto/condicional em Schema Objects, propriedades, parâmetros ou respostas, quando o elemento técnico representar explicitamente o conceito; não inferir papéis apenas pelo nome. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto principalmente na Etapa 2; pode fundamentar operações, requisitos e rastreabilidade nas Etapas 4, 6, 7 e 8. |

## C16 - DP Etnia

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Dados, categorias e coleções |
| Estereótipo | «role» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Papel especializado de DP Sensível desempenhado por um dado referente à origem racial ou étnica de uma Pessoa Natural. |
| Definição normativa | ABNT NBR ISO/IEC 29100:2020:<br>2.24 DP SENSÍVEIS: categoria de dados pessoais (DP) cuja natureza é sensível, como aqueles que se relacionam à esfera mais íntima do titular de DP ou que podem ter um impacto significativo sobre o titular de DP.<br><br>NOTA: Em algumas jurisdições ou em contextos específicos, DP SENSÍVEIS são definidos com referência à natureza dos DP e podem consistir em DP QUE REVELEM A ORIGEM RACIAL, opiniões políticas, crenças religiosas ou outras, dados pessoais sobre saúde, vida sexual ou condenações criminais, bem como outros DP que possam ser definidos como sensíveis.<br><br>LGPD - Lei nº 13.709/2018:<br>(Redação dada pela Lei nº 13.853, de 2019) <br><br>(Art. 5º) II - DADO PESSOAL SENSÍVEL: DADO PESSOAL SOBRE ORIGEM RACIAL OU ÉTNICA, convicção religiosa, opinião política, filiação a sindicato ou a organização de caráter religioso, filosófico ou político, dado referente à saúde ou à vida sexual, dado genético ou biométrico, quando vinculado a uma pessoa natural; |
| Fonte | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020; LGPD - Lei nº 13.709/2018 |
| Superconceito | DP Sensível |
| Subconceitos | - |
| Relações | - |
| Restrições | GS07 membro de {overlapping, incomplete} |
| Sinônimos | Dado sobre Origem Racial ou Étnica |
| Exemplo | A informação declarada de origem racial ou étnica de uma pessoa. |
| Não Exemplo | Um CEP que não revela origem racial ou étnica. |
| QCs relacionadas | QC-P1 |
| Uso previsto em OpenAPI | Direto/condicional em Schema Objects, propriedades, parâmetros ou respostas, quando o elemento técnico representar explicitamente o conceito; não inferir papéis apenas pelo nome. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto principalmente na Etapa 2; pode fundamentar operações, requisitos e rastreabilidade nas Etapas 4, 6, 7 e 8. |

## C17 - DP Religião

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Dados, categorias e coleções |
| Estereótipo | «role» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Papel especializado de DP Sensível desempenhado por um dado referente à convicção religiosa de uma Pessoa Natural. |
| Definição normativa | ABNT NBR ISO/IEC 29100:2020:<br>2.24 DP SENSÍVEIS: categoria de dados pessoais (DP) cuja natureza é sensível, como aqueles que se relacionam à esfera mais íntima do titular de DP ou que podem ter um impacto significativo sobre o titular de DP.<br><br>NOTA: Em algumas jurisdições ou em contextos específicos, DP SENSÍVEIS são definidos com referência à natureza dos DP e podem consistir em DP que revelem a origem racial, opiniões políticas, CRENÇAS RELIGIOSAS ou outras, dados pessoais sobre saúde, vida sexual ou condenações criminais, bem como outros DP que possam ser definidos como sensíveis.<br><br>LGPD - Lei nº 13.709/2018:<br>(Redação dada pela Lei nº 13.853, de 2019) <br><br>(Art. 5º) II - DADO PESSOAL SENSÍVEL: dado pessoal sobre origem racial ou étnica, CONVICÇÃO RELIGIOSA, opinião política, filiação a sindicato ou a organização de caráter religioso, filosófico ou político, dado referente à saúde ou à vida sexual, dado genético ou biométrico, quando vinculado a uma pessoa natural; |
| Fonte | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020; LGPD - Lei nº 13.709/2018 |
| Superconceito | DP Sensível |
| Subconceitos | - |
| Relações | - |
| Restrições | GS07 membro de {overlapping, incomplete} |
| Sinônimos | Dado sobre Convicção Religiosa |
| Exemplo | A informação sobre a convicção religiosa declarada por uma pessoa. |
| Não Exemplo | Um endereço de e-mail que não expressa convicção religiosa. |
| QCs relacionadas | QC-P1 |
| Uso previsto em OpenAPI | Direto/condicional em Schema Objects, propriedades, parâmetros ou respostas, quando o elemento técnico representar explicitamente o conceito; não inferir papéis apenas pelo nome. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto principalmente na Etapa 2; pode fundamentar operações, requisitos e rastreabilidade nas Etapas 4, 6, 7 e 8. |

## C18 - DP Político

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Dados, categorias e coleções |
| Estereótipo | «role» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Papel especializado de DP Sensível desempenhado por um dado referente à opinião política de uma Pessoa Natural. |
| Definição normativa | LGPD - Lei nº 13.709/2018:<br>(Redação dada pela Lei nº 13.853, de 2019) <br><br>(Art. 5º) II - DADO PESSOAL SENSÍVEL: dado pessoal sobre origem racial ou étnica, convicção religiosa, OPINIÃO POLÍTICA, filiação a sindicato ou a ORGANIZAÇÃO DE CARÁTER religioso, filosófico ou POLÍTICO, dado referente à saúde ou à vida sexual, dado genético ou biométrico, quando vinculado a uma pessoa natural; |
| Fonte | OntoPrivacy v2; LGPD - Lei nº 13.709/2018 |
| Superconceito | DP Sensível |
| Subconceitos | - |
| Relações | - |
| Restrições | GS07 membro de {overlapping, incomplete} |
| Sinônimos | Dado sobre Opinião Política |
| Exemplo | A informação sobre a opinião política de uma pessoa. |
| Não Exemplo | Um cargo profissional sem informação de opinião política. |
| QCs relacionadas | QC-P1 |
| Uso previsto em OpenAPI | Direto/condicional em Schema Objects, propriedades, parâmetros ou respostas, quando o elemento técnico representar explicitamente o conceito; não inferir papéis apenas pelo nome. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto principalmente na Etapa 2; pode fundamentar operações, requisitos e rastreabilidade nas Etapas 4, 6, 7 e 8. |

## C19 - DP Saúde

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Dados, categorias e coleções |
| Estereótipo | «role» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Papel especializado de DP Sensível desempenhado por um dado referente à saúde de uma Pessoa Natural. |
| Definição normativa | ABNT NBR ISO/IEC 29100:2020:<br>2.24 DP SENSÍVEIS: categoria de dados pessoais (DP) cuja natureza é sensível, como aqueles que se relacionam à esfera mais íntima do titular de DP ou que podem ter um impacto significativo sobre o titular de DP.<br><br>NOTA: Em algumas jurisdições ou em contextos específicos, DP SENSÍVEIS são definidos com referência à natureza dos DP e podem consistir em DP que revelem a origem racial, opiniões políticas, crenças religiosas ou outras, DADOS PESSOAIS SOBRE SAÚDE, VIDA SEXUAL ou condenações criminais, bem como outros DP que possam ser definidos como sensíveis.<br><br>LGPD - Lei nº 13.709/2018:<br>(Redação dada pela Lei nº 13.853, de 2019) <br><br>(Art. 5º) II - DADO PESSOAL SENSÍVEL: dado pessoal sobre origem racial ou étnica, convicção religiosa, opinião política, filiação a sindicato ou a organização de caráter religioso, filosófico ou político, DADO REFERENTE À SAÚDE OU À VIDA SEXUAL, dado genético ou biométrico, quando vinculado a uma pessoa natural; |
| Fonte | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020; LGPD - Lei nº 13.709/2018 |
| Superconceito | DP Sensível |
| Subconceitos | - |
| Relações | - |
| Restrições | GS07 membro de {overlapping, incomplete} |
| Sinônimos | Dado sobre Saúde |
| Exemplo | Um diagnóstico, resultado de exame ou informação clínica de uma pessoa. |
| Não Exemplo | Uma preferência de interface sem relação com saúde. |
| QCs relacionadas | QC-P1 |
| Uso previsto em OpenAPI | Direto/condicional em Schema Objects, propriedades, parâmetros ou respostas, quando o elemento técnico representar explicitamente o conceito; não inferir papéis apenas pelo nome. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto principalmente na Etapa 2; pode fundamentar operações, requisitos e rastreabilidade nas Etapas 4, 6, 7 e 8. |

## C20 - DP Biométrico

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Dados, categorias e coleções |
| Estereótipo | «role» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Papel especializado de DP Sensível desempenhado por um dado biométrico vinculado a uma Pessoa Natural. |
| Definição normativa | ABNT NBR ISO/IEC 29100:2020:<br>2.24 DP SENSÍVEIS: categoria de dados pessoais (DP) cuja natureza é sensível, como aqueles que se relacionam à esfera mais íntima do titular de DP ou que podem ter um impacto significativo sobre o titular de DP.<br><br>NOTA: Em algumas jurisdições ou em contextos específicos, DP SENSÍVEIS são definidos com referência à natureza dos DP e podem consistir em DP que revelem a origem racial, opiniões políticas, crenças religiosas ou outras, dados pessoais sobre saúde, vida sexual ou condenações criminais, bem como outros DP que possam ser definidos como sensíveis.<br><br>LGPD - Lei nº 13.709/2018:<br>(Redação dada pela Lei nº 13.853, de 2019) <br><br>(Art. 5º) II - DADO PESSOAL SENSÍVEL: dado pessoal sobre origem racial ou étnica, convicção religiosa, opinião política, filiação a sindicato ou a organização de caráter religioso, filosófico ou político, dado referente à saúde ou à vida sexual, DADO GENÉTICO OU BIOMÉTRICO, quando vinculado a uma pessoa natural; |
| Fonte | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020; LGPD - Lei nº 13.709/2018 |
| Superconceito | DP Sensível |
| Subconceitos | - |
| Relações | - |
| Restrições | GS07 membro de {overlapping, incomplete} |
| Sinônimos | Dado Biométrico |
| Exemplo | Um modelo biométrico de impressão digital vinculado a uma pessoa. |
| Não Exemplo | O número de série de um dispositivo. |
| QCs relacionadas | QC-P1 |
| Uso previsto em OpenAPI | Direto/condicional em Schema Objects, propriedades, parâmetros ou respostas, quando o elemento técnico representar explicitamente o conceito; não inferir papéis apenas pelo nome. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto principalmente na Etapa 2; pode fundamentar operações, requisitos e rastreabilidade nas Etapas 4, 6, 7 e 8. |

## C21 - Dado Pseudonimizado

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Dados, categorias e coleções |
| Estereótipo | «role» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Papel especializado de Dado Pessoal desempenhado por um dado resultante de Pseudonimização, cuja associação ao Titular depende de informação adicional mantida separadamente sob condições controladas. |
| Definição normativa | Não há definição normativa autônoma registrada na classe. A rastreabilidade normativa é herdada dos conceitos superiores ou relacionados: ABNT NBR ISO/IEC 29100:2020; LGPD - Lei nº 13.709/2018; Glossário ANPD - Resolução CD/ANPD nº 1/2021. |
| Fonte | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020 - rastreabilidade herdada; LGPD - Lei nº 13.709/2018 - rastreabilidade herdada; Glossário ANPD - Resolução CD/ANPD nº 1/2021 - rastreabilidade herdada |
| Superconceito | Dado Pessoal (DP) |
| Subconceitos | - |
| Relações | R15 resulta em (Pseudonimização) - Pseudonimização [1] |
| Restrições | REST01 participa de pelo menos uma Identificabilidade Indireta |
| Sinônimos | - |
| Exemplo | Um código de participante cuja tabela de correspondência com o nome é mantida separadamente. |
| Não Exemplo | Um conjunto efetivamente anonimizado sem informação adicional de reidentificação. |
| QCs relacionadas | QC-P1; QC-P2; QC-P7 |
| Uso previsto em OpenAPI | Direto/condicional em Schema Objects, propriedades, parâmetros ou respostas, quando o elemento técnico representar explicitamente o conceito; não inferir papéis apenas pelo nome. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto principalmente na Etapa 2; pode fundamentar operações, requisitos e rastreabilidade nas Etapas 4, 6, 7 e 8. |

## C22 - Dado Anonimizado

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Dados, categorias e coleções |
| Estereótipo | «role» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Papel desempenhado por um Dado produzido por Anonimização e caracterizado por Anonimidade no contexto e segundo os meios razoáveis considerados. |
| Definição normativa | ABNT NBR ISO/IEC 29100:2020:<br>2.3 DADO ANONIMIZADO: dado que tenha sido produzido como resultado de um processo de anonimização dos dados pessoais.<br><br>LGPD - Lei nº 13.709/2018:<br>(Redação dada pela Lei nº 13.853, de 2019) <br><br>(Art. 5º) III - DADO ANONIMIZADO: dado relativo a titular que não possa ser identificado, considerando a utilização de meios técnicos razoáveis e disponíveis na ocasião de seu tratamento; |
| Fonte | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020; LGPD - Lei nº 13.709/2018 |
| Superconceito | Dado |
| Subconceitos | - |
| Relações | R06 caracteriza - Anonimidade [1]<br>R14 resulta em (Anonimização) - Anonimização [1] |
| Restrições | GS02 membro de {disjoint} |
| Sinônimos | - |
| Exemplo | Um conjunto estatístico que, no contexto analisado, não permite identificar os indivíduos por meios razoáveis. |
| Não Exemplo | Um CPF apenas criptografado ou com chave reversível disponível. |
| QCs relacionadas | QC-P1; QC-P7 |
| Uso previsto em OpenAPI | Direto/condicional em Schema Objects, propriedades, parâmetros ou respostas, quando o elemento técnico representar explicitamente o conceito; não inferir papéis apenas pelo nome. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto principalmente na Etapa 2; pode fundamentar operações, requisitos e rastreabilidade nas Etapas 4, 6, 7 e 8. |

## C23 - Anonimidade

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Dados, categorias e coleções |
| Estereótipo | «mode» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Modo intrínseco que caracteriza um Dado Anonimizado quando ele não permite a identificação direta ou indireta da Pessoa Natural no contexto considerado. |
| Definição normativa | ABNT NBR ISO/IEC 29100:2020:<br>2.1 ANONIMIDADE: característica da informação que não permite que um titular de dados pessoais seja identificado direta ou indiretamente. |
| Fonte | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020 |
| Superconceito | - |
| Subconceitos | - |
| Relações | R06 caracteriza - Dado Anonimizado [1] |
| Restrições | - |
| Sinônimos | - |
| Exemplo | A condição que caracteriza o conjunto estatístico após anonimização. |
| Não Exemplo | Criptografia, que é uma medida técnica e não implica anonimidade. |
| QCs relacionadas | QC-P1; QC-P7 |
| Uso previsto em OpenAPI | Condicional e normalmente dependente de extensão específica ou metadado contextual; não inferir na anotação básica sem evidência explícita. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto principalmente na Etapa 2; pode fundamentar operações, requisitos e rastreabilidade nas Etapas 4, 6, 7 e 8. |

## C24 - Conjunto de Dados

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Dados, categorias e coleções |
| Estereótipo | «collective» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Coletivo constituído por dois ou mais Dados reunidos segundo um critério de organização ou uso comum. |
| Definição normativa | Não há definição normativa direta. |
| Fonte | OntoPrivacy v2 |
| Superconceito | - |
| Subconceitos | Banco de Dados DP |
| Relações | R01 integra (Dado–Conjunto de Dados) - Dado [2..*] |
| Restrições | - |
| Sinônimos | - |
| Exemplo | Um arquivo CSV formado por vários registros de inscrição. |
| Não Exemplo | Uma única ocorrência isolada de dado, considerando a cardinalidade mínima do modelo. |
| QCs relacionadas | QC-P1 |
| Uso previsto em OpenAPI | Direto/condicional em Schema Objects, propriedades, parâmetros ou respostas, quando o elemento técnico representar explicitamente o conceito; não inferir papéis apenas pelo nome. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto principalmente na Etapa 2; pode fundamentar operações, requisitos e rastreabilidade nas Etapas 4, 6, 7 e 8. |

## C25 - Banco de Dados DP

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Dados, categorias e coleções |
| Estereótipo | «subkind» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Especialização rígida de Conjunto de Dados que representa um conjunto estruturado composto por Dados Pessoais e organizado em suporte físico ou eletrônico. |
| Definição normativa | LGPD - Lei nº 13.709/2018:<br>(Redação dada pela Lei nº 13.853, de 2019) <br><br>Art. 5º, IV - BANCO DE DADOS: conjunto estruturado de dados pessoais organizado em um ou mais locais e mantido em suporte eletrônico ou físico. |
| Fonte | OntoPrivacy v2; LGPD - Lei nº 13.709/2018 |
| Superconceito | Conjunto de Dados |
| Subconceitos | - |
| Relações | R02 integra (Dado Pessoal–Banco de Dados DP) - Dado Pessoal (DP) [2..*] |
| Restrições | - |
| Sinônimos | - |
| Exemplo | Um banco estruturado contendo registros pessoais de alunos. |
| Não Exemplo | Um catálogo constituído apenas por dados de produtos não pessoais. |
| QCs relacionadas | QC-P1 |
| Uso previsto em OpenAPI | Direto/condicional em Schema Objects, propriedades, parâmetros ou respostas, quando o elemento técnico representar explicitamente o conceito; não inferir papéis apenas pelo nome. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto principalmente na Etapa 2; pode fundamentar operações, requisitos e rastreabilidade nas Etapas 4, 6, 7 e 8. |

## C26 - Identificabilidade

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Identificabilidade |
| Estereótipo | «relator» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Relator que conecta um ou mais Dados Pessoais ao Titular cuja identidade pode ser estabelecida direta ou indiretamente no contexto analisado. |
| Definição normativa | ABNT NBR ISO/IEC 29100:2020:<br>2.5 IDENTIFICABILIDADE*: condição que resulta na identificação de um titular de dados pessoais (DP), DIRETA ou indiretamente, com base em um dado conjunto de DP.<br><br>NOTA: Para determinar se um TITULAR DE DP É IDENTIFICÁVEL, convém que sejam levados em conta todos os meios que possam ser razoavelmente usados pela parte interessada na privacidade, detentora dos dados, ou por qualquer outra parte, para identificar a pessoa natural. |
| Fonte | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020 |
| Superconceito | - |
| Subconceitos | Identificabilidade Direta; Identificabilidade Indireta |
| Relações | R05 baseia-se - Dado Pessoal (DP) [1..*]<br>R09 identifica - Titular de DP [1] |
| Restrições | GS03 {disjoint, complete} sobre Identificabilidade Direta; Identificabilidade Indireta |
| Sinônimos | - |
| Exemplo | A relação pela qual CPF e nome permitem estabelecer que o Titular é João. |
| Não Exemplo | A simples existência de um dado sem relação que permita identificar pessoa natural. |
| QCs relacionadas | QC-P2 |
| Uso previsto em OpenAPI | Condicional e normalmente dependente de extensão específica ou metadado contextual; não inferir na anotação básica sem evidência explícita. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto nas Etapas 2 e 3 para relacionar dados e titulares; repercute nas Etapas 4 a 8. |

## C27 - Identificabilidade Direta

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Identificabilidade |
| Estereótipo | «subkind» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Especialização rígida de Identificabilidade na qual o Titular pode ser individualizado sem depender de combinação relevante com informação adicional separada. |
| Definição normativa | Não há definição normativa autônoma registrada na classe. A rastreabilidade normativa é herdada dos conceitos superiores ou relacionados: ABNT NBR ISO/IEC 29100:2020. |
| Fonte | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020 - rastreabilidade herdada |
| Superconceito | Identificabilidade |
| Subconceitos | - |
| Relações | - |
| Restrições | GS03 membro de {disjoint, complete} |
| Sinônimos | - |
| Exemplo | A identificação de João por seu CPF. |
| Não Exemplo | A identificação que depende da combinação de vários atributos auxiliares. |
| QCs relacionadas | QC-P2 |
| Uso previsto em OpenAPI | Condicional e normalmente dependente de extensão específica ou metadado contextual; não inferir na anotação básica sem evidência explícita. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto nas Etapas 2 e 3 para relacionar dados e titulares; repercute nas Etapas 4 a 8. |

## C28 - Identificabilidade Indireta

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Identificabilidade |
| Estereótipo | «subkind» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Especialização rígida de Identificabilidade na qual o Titular pode ser individualizado mediante combinação de dados, informação adicional ou meios razoavelmente disponíveis no contexto. |
| Definição normativa | Não há definição normativa autônoma registrada na classe. A rastreabilidade normativa é herdada dos conceitos superiores ou relacionados: ABNT NBR ISO/IEC 29100:2020; LGPD - Lei nº 13.709/2018. |
| Fonte | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020 - rastreabilidade herdada; LGPD - Lei nº 13.709/2018 - rastreabilidade herdada |
| Superconceito | Identificabilidade |
| Subconceitos | - |
| Relações | - |
| Restrições | GS03 membro de {disjoint, complete} |
| Sinônimos | - |
| Exemplo | A identificação de uma pessoa pela combinação de idade, profissão e CEP. |
| Não Exemplo | A identificação imediata por CPF. |
| QCs relacionadas | QC-P2; QC-P7 |
| Uso previsto em OpenAPI | Condicional e normalmente dependente de extensão específica ou metadado contextual; não inferir na anotação básica sem evidência explícita. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto nas Etapas 2 e 3 para relacionar dados e titulares; repercute nas Etapas 4 a 8. |

## C29 - Tratamento de Dados Pessoais (TDP)

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Tratamento e operações |
| Estereótipo | «relator» |
| Abstrato ou concreto | Abstrato |
| Definição ontológica | Relator que representa uma situação na qual Partes Interessadas submetem Dados Pessoais a uma Operação de TDP ou a um conjunto articulado de Operações, sob responsabilidade de Controladores e orientada por Finalidades. |
| Definição normativa | ABNT NBR ISO/IEC 29100:2020:<br>2.21 TRATAMENTO DE DP: OPERAÇÃO ou CONJUNTO DE OPERAÇÕES realizadas sobre dados pessoais (DP).<br><br>NOTA: Exemplos de OPERAÇÕES DE TRATAMENTO DE DP incluem, mas não estão limitados a, COLETA, ARMAZENAMENTO, ALTERAÇÃO, RECUPERAÇÃO, CONSULTA, DIVULGAÇÃO, ANONIMIZAÇÃO, PSEUDONIMIZAÇÃO, DISSEMINAÇÃO ou DISPONIBILIZAÇÃO, EXCLUSÃO ou DESTRUIÇÃO de DP.<br><br>LGPD - Lei nº 13.709/2018:<br>(Redação dada pela Lei nº 13.853, de 2019) <br><br>(Art. 5º) X - TRATAMENTO: toda OPERAÇÃO realizada com dados pessoais, como as que se referem a COLETA, produção, recepção, classificação, utilização, acesso, reprodução, transmissão, DISTRIBUIÇÃO, processamento, arquivamento, ARMAZENAMENTO, ELIMINAÇÃO, avaliação ou controle da informação, MODIFICAÇÃO, comunicação, transferência, difusão ou extração; |
| Fonte | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020; LGPD - Lei nº 13.709/2018 |
| Superconceito | - |
| Subconceitos | Conjunto de Operações de TDP; Operação de TDP |
| Relações | R04 abrange - Dado Pessoal (DP) [1..*]<br>R08 envolve - Parte Interessada na Privacidade [1..*]<br>R11 realiza - Operador [0..*]<br>R16 tem escopo - Consentimento [0..*]<br>R20 é orientado por - Finalidade [1..*]<br>R21 é responsável pelo - Controlador [1..*] |
| Restrições | GS04 {disjoint, complete} sobre Operação de TDP; Conjunto de Operações de TDP |
| Sinônimos | Tratamento de Dados Pessoais; TDP; Tratamento |
| Exemplo | A situação de tratamento referente à matrícula de alunos, envolvendo dados, participantes, operações e finalidade. |
| Não Exemplo | O texto abstrato de uma lei, sem uma situação de tratamento representada. |
| QCs relacionadas | QC-P3; QC-P4; QC-P5; QC-P6; QC-P7 |
| Uso previsto em OpenAPI | Direto em Operation Objects por anotação de tipo de tratamento, desde que a descrição funcional, os dados e o fluxo sustentem a classificação. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto principalmente na Etapa 4; apoia Finalidades/Consentimento na Etapa 5 e requisitos/rastreabilidade nas Etapas 6 a 8. |

## C30 - Operação de TDP

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Tratamento e operações |
| Estereótipo | «subkind» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Especialização rígida de TDP que representa uma modalidade específica de incidência relacional sobre um ou mais Dados Pessoais. |
| Definição normativa | ABNT NBR ISO/IEC 29100:2020:<br>Exemplos de operação de tratamento de DP incluem, mas não estão limitados a, coleta, armazenamento, alteração, recuperação, consulta, divulgação, anonimização, pseudonimização, disseminação ou disponibilização, exclusão ou destruição de DP.<br><br>LGPD - Lei nº 13.709/2018:<br>(Redação dada pela Lei nº 13.853, de 2019) <br><br>(Art. 5º) X - tratamento: toda operação realizada com dados pessoais, como as que se referem a coleta, produção, recepção, classificação, utilização, acesso, reprodução, transmissão, distribuição, processamento, arquivamento, armazenamento, eliminação, avaliação ou controle da informação, modificação, comunicação, transferência, difusão ou extração; |
| Fonte | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020; LGPD - Lei nº 13.709/2018 |
| Superconceito | Tratamento de Dados Pessoais (TDP) |
| Subconceitos | Alteração; Anonimização; Armazenamento; Coleta; Consulta; Disponibilização; Divulgação; Exclusão; Pseudonimização; Recuperação |
| Relações | R03 é composto por - Conjunto de Operações de TDP [0..*] |
| Restrições | GS04 membro de {disjoint, complete}<br>GS05 {overlapping, incomplete} sobre Alteração; Anonimização; Armazenamento; Coleta; Consulta; Disponibilização; Divulgação; Exclusão; Pseudonimização; Recuperação |
| Sinônimos | Operação de Tratamento de Dados Pessoais; Operação de Tratamento |
| Exemplo | Uma ocorrência relacional de Coleta de CPF no formulário de matrícula. |
| Não Exemplo | Um tratamento composto simultaneamente por várias operações. |
| QCs relacionadas | QC-P4 |
| Uso previsto em OpenAPI | Direto em Operation Objects por anotação de tipo de tratamento, desde que a descrição funcional, os dados e o fluxo sustentem a classificação. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto principalmente na Etapa 4; apoia Finalidades/Consentimento na Etapa 5 e requisitos/rastreabilidade nas Etapas 6 a 8. |

## C31 - Conjunto de Operações de TDP

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Tratamento e operações |
| Estereótipo | «subkind» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Especialização rígida de TDP que representa um tratamento relacional composto por pelo menos duas Operações de TDP pertencentes ao mesmo contexto. |
| Definição normativa | Não há definição normativa autônoma registrada na classe. A rastreabilidade normativa é herdada dos conceitos superiores ou relacionados: ABNT NBR ISO/IEC 29100:2020; LGPD - Lei nº 13.709/2018. |
| Fonte | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020 - rastreabilidade herdada; LGPD - Lei nº 13.709/2018 - rastreabilidade herdada |
| Superconceito | Tratamento de Dados Pessoais (TDP) |
| Subconceitos | - |
| Relações | R03 é composto por - Operação de TDP [2..*] |
| Restrições | GS04 membro de {disjoint, complete} |
| Sinônimos | Conjunto de Operações de Tratamento |
| Exemplo | O tratamento composto por Coleta, Armazenamento e Consulta dos dados de matrícula. |
| Não Exemplo | Uma única operação de Consulta. |
| QCs relacionadas | QC-P4 |
| Uso previsto em OpenAPI | Direto em Operation Objects por anotação de tipo de tratamento, desde que a descrição funcional, os dados e o fluxo sustentem a classificação. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto principalmente na Etapa 4; apoia Finalidades/Consentimento na Etapa 5 e requisitos/rastreabilidade nas Etapas 6 a 8. |

## C32 - Coleta

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Tratamento e operações |
| Estereótipo | «subkind» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Especialização de Operação de TDP na qual Dados Pessoais são obtidos de um Titular, de outra parte ou de uma fonte e incorporados ao contexto de tratamento. |
| Definição normativa | Não há definição normativa autônoma registrada na classe. A rastreabilidade normativa é herdada dos conceitos superiores ou relacionados: ABNT NBR ISO/IEC 29100:2020; LGPD - Lei nº 13.709/2018. |
| Fonte | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020 - rastreabilidade herdada; LGPD - Lei nº 13.709/2018 - rastreabilidade herdada |
| Superconceito | Operação de TDP |
| Subconceitos | - |
| Relações | - |
| Restrições | GS05 membro de {overlapping, incomplete} |
| Sinônimos | - |
| Exemplo | O recebimento de nome e CPF por meio de formulário eletrônico. |
| Não Exemplo | A leitura de dado já armazenado sem obtenção de nova informação. |
| QCs relacionadas | QC-P4 |
| Uso previsto em OpenAPI | Direto em Operation Objects por anotação de tipo de tratamento, desde que a descrição funcional, os dados e o fluxo sustentem a classificação. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto principalmente na Etapa 4; apoia Finalidades/Consentimento na Etapa 5 e requisitos/rastreabilidade nas Etapas 6 a 8. |

## C33 - Armazenamento

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Tratamento e operações |
| Estereótipo | «subkind» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Especialização de Operação de TDP na qual Dados Pessoais são mantidos persistentemente em suporte físico ou eletrônico para acesso ou uso posterior. |
| Definição normativa | Não há definição normativa autônoma registrada na classe. A rastreabilidade normativa é herdada dos conceitos superiores ou relacionados: ABNT NBR ISO/IEC 29100:2020; LGPD - Lei nº 13.709/2018. |
| Fonte | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020 - rastreabilidade herdada; LGPD - Lei nº 13.709/2018 - rastreabilidade herdada |
| Superconceito | Operação de TDP |
| Subconceitos | - |
| Relações | - |
| Restrições | GS05 membro de {overlapping, incomplete} |
| Sinônimos | - |
| Exemplo | A persistência dos dados de matrícula em banco de dados. |
| Não Exemplo | A exibição transitória de um dado sem persistência. |
| QCs relacionadas | QC-P4 |
| Uso previsto em OpenAPI | Direto em Operation Objects por anotação de tipo de tratamento, desde que a descrição funcional, os dados e o fluxo sustentem a classificação. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto principalmente na Etapa 4; apoia Finalidades/Consentimento na Etapa 5 e requisitos/rastreabilidade nas Etapas 6 a 8. |

## C34 - Alteração

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Tratamento e operações |
| Estereótipo | «subkind» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Especialização de Operação de TDP na qual o conteúdo, valor, estrutura, associação ou estado de Dados Pessoais existentes é modificado. |
| Definição normativa | Não há definição normativa autônoma registrada na classe. A rastreabilidade normativa é herdada dos conceitos superiores ou relacionados: ABNT NBR ISO/IEC 29100:2020; LGPD - Lei nº 13.709/2018. |
| Fonte | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020 - rastreabilidade herdada; LGPD - Lei nº 13.709/2018 - rastreabilidade herdada |
| Superconceito | Operação de TDP |
| Subconceitos | - |
| Relações | - |
| Restrições | GS05 membro de {overlapping, incomplete} |
| Sinônimos | Modificação |
| Exemplo | A atualização do endereço cadastrado do aluno. |
| Não Exemplo | Uma operação exclusivamente de leitura. |
| QCs relacionadas | QC-P4 |
| Uso previsto em OpenAPI | Direto em Operation Objects por anotação de tipo de tratamento, desde que a descrição funcional, os dados e o fluxo sustentem a classificação. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto principalmente na Etapa 4; apoia Finalidades/Consentimento na Etapa 5 e requisitos/rastreabilidade nas Etapas 6 a 8. |

## C35 - Recuperação

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Tratamento e operações |
| Estereótipo | «subkind» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Especialização de Operação de TDP na qual Dados Pessoais previamente armazenados são localizados e restituídos a uma condição acessível ou utilizável. |
| Definição normativa | Não há definição normativa autônoma registrada na classe. A rastreabilidade normativa é herdada dos conceitos superiores ou relacionados: ABNT NBR ISO/IEC 29100:2020. |
| Fonte | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020 - rastreabilidade herdada |
| Superconceito | Operação de TDP |
| Subconceitos | - |
| Relações | - |
| Restrições | GS05 membro de {overlapping, incomplete} |
| Sinônimos | - |
| Exemplo | A localização e restauração de um registro arquivado. |
| Não Exemplo | A obtenção inicial de um dado diretamente do Titular. |
| QCs relacionadas | QC-P4 |
| Uso previsto em OpenAPI | Direto em Operation Objects por anotação de tipo de tratamento, desde que a descrição funcional, os dados e o fluxo sustentem a classificação. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto principalmente na Etapa 4; apoia Finalidades/Consentimento na Etapa 5 e requisitos/rastreabilidade nas Etapas 6 a 8. |

## C36 - Consulta

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Tratamento e operações |
| Estereótipo | «subkind» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Especialização de Operação de TDP na qual um participante acessa Dados Pessoais para leitura ou exame, sem que isso implique, por si só, modificação ou comunicação a outra parte. |
| Definição normativa | Não há definição normativa autônoma registrada na classe. A rastreabilidade normativa é herdada dos conceitos superiores ou relacionados: ABNT NBR ISO/IEC 29100:2020; LGPD - Lei nº 13.709/2018. |
| Fonte | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020 - rastreabilidade herdada; LGPD - Lei nº 13.709/2018 - rastreabilidade herdada |
| Superconceito | Operação de TDP |
| Subconceitos | - |
| Relações | - |
| Restrições | GS05 membro de {overlapping, incomplete} |
| Sinônimos | - |
| Exemplo | A leitura de uma inscrição pela equipe administrativa. |
| Não Exemplo | A comunicação do dado a destinatário externo. |
| QCs relacionadas | QC-P4 |
| Uso previsto em OpenAPI | Direto em Operation Objects por anotação de tipo de tratamento, desde que a descrição funcional, os dados e o fluxo sustentem a classificação. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto principalmente na Etapa 4; apoia Finalidades/Consentimento na Etapa 5 e requisitos/rastreabilidade nas Etapas 6 a 8. |

## C37 - Divulgação

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Tratamento e operações |
| Estereótipo | «subkind» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Especialização de Operação de TDP na qual Dados Pessoais são comunicados ou revelados a destinatários além da parte que previamente os mantinha. |
| Definição normativa | Não há definição normativa autônoma registrada na classe. A rastreabilidade normativa é herdada dos conceitos superiores ou relacionados: ABNT NBR ISO/IEC 29100:2020; LGPD - Lei nº 13.709/2018. |
| Fonte | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020 - rastreabilidade herdada; LGPD - Lei nº 13.709/2018 - rastreabilidade herdada |
| Superconceito | Operação de TDP |
| Subconceitos | - |
| Relações | - |
| Restrições | GS05 membro de {overlapping, incomplete} |
| Sinônimos | Comunicação; Divulgação |
| Exemplo | O envio de dados pessoais a uma organização destinatária distinta. |
| Não Exemplo | A leitura interna por usuário autorizado, sem revelação a outro destinatário. |
| QCs relacionadas | QC-P4 |
| Uso previsto em OpenAPI | Direto em Operation Objects por anotação de tipo de tratamento, desde que a descrição funcional, os dados e o fluxo sustentem a classificação. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto principalmente na Etapa 4; apoia Finalidades/Consentimento na Etapa 5 e requisitos/rastreabilidade nas Etapas 6 a 8. |

## C38 - Disponibilização

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Tratamento e operações |
| Estereótipo | «subkind» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Especialização de Operação de TDP na qual Dados Pessoais são colocados ao alcance de uma pessoa, organização ou sistema sob condições de acesso. |
| Definição normativa | Não há definição normativa autônoma registrada na classe. A rastreabilidade normativa é herdada dos conceitos superiores ou relacionados: ABNT NBR ISO/IEC 29100:2020. |
| Fonte | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020 - rastreabilidade herdada |
| Superconceito | Operação de TDP |
| Subconceitos | - |
| Relações | - |
| Restrições | GS05 membro de {overlapping, incomplete} |
| Sinônimos | - |
| Exemplo | Uma API que torna dados acessíveis a um consumidor autenticado. |
| Não Exemplo | Um dado que permanece inacessível a qualquer destinatário. |
| QCs relacionadas | QC-P4 |
| Uso previsto em OpenAPI | Direto em Operation Objects por anotação de tipo de tratamento, desde que a descrição funcional, os dados e o fluxo sustentem a classificação. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto principalmente na Etapa 4; apoia Finalidades/Consentimento na Etapa 5 e requisitos/rastreabilidade nas Etapas 6 a 8. |

## C39 - Exclusão

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Tratamento e operações |
| Estereótipo | «subkind» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Especialização de Operação de TDP na qual um Dado ou Conjunto de Dados armazenado é excluído, independentemente do procedimento empregado. |
| Definição normativa | ABNT NBR ISO/IEC 29100:2020:<br>2.21 NOTA: Exemplos de operações de tratamento de DP incluem, mas não estão limitados a, EXCLUSÃO ou DESTRUIÇÃO de DP.<br><br>LGPD - Lei nº 13.709/2018:<br>(Redação dada pela Lei nº 13.853, de 2019) <br><br>(Art. 5º) XIV - ELIMINAÇÃO: exclusão de dado ou de conjunto de dados armazenados em banco de dados, independentemente do procedimento empregado; |
| Fonte | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020; LGPD - Lei nº 13.709/2018 |
| Superconceito | Operação de TDP |
| Subconceitos | - |
| Relações | - |
| Restrições | GS05 membro de {overlapping, incomplete} |
| Sinônimos | Eliminação |
| Exemplo | A remoção de um registro pessoal armazenado no banco. |
| Não Exemplo | A simples mudança de status para “arquivado” com manutenção integral do dado. |
| QCs relacionadas | QC-P4 |
| Uso previsto em OpenAPI | Direto em Operation Objects por anotação de tipo de tratamento, desde que a descrição funcional, os dados e o fluxo sustentem a classificação. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto principalmente na Etapa 4; apoia Finalidades/Consentimento na Etapa 5 e requisitos/rastreabilidade nas Etapas 6 a 8. |

## C40 - Anonimização

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Tratamento e operações |
| Estereótipo | «subkind» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Especialização de Operação de TDP que representa uma situação relacional na qual Dados Pessoais são submetidos a meios de anonimização, resultando em Dados Anonimizados caracterizados por Anonimidade. |
| Definição normativa | ABNT NBR ISO/IEC 29100:2020:<br>2.2 ANONIMIZAÇÃO: processo pelo qual dados pessoais (DP) são irreversivelmente alterados, de forma que um titular de DP não mais pode ser identificado, direta ou indiretamente, seja por um controlador de DP apenas ou em colaboração com qualquer outra parte.<br><br>LGPD - Lei nº 13.709/2018:<br>(Redação dada pela Lei nº 13.853, de 2019) <br><br>(Art. 5º) XI - ANONIMIZAÇÃO: utilização de meios técnicos razoáveis e disponíveis no momento do tratamento, por meio dos quais um dado perde a possibilidade de associação, direta ou indireta, a um indivíduo; |
| Fonte | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020; LGPD - Lei nº 13.709/2018 |
| Superconceito | Operação de TDP |
| Subconceitos | - |
| Relações | R14 resulta em (Anonimização) - Dado Anonimizado [1..*] |
| Restrições | GS05 membro de {overlapping, incomplete} |
| Sinônimos | - |
| Exemplo | A transformação de dados individuais em um conjunto que não permite identificação por meios razoáveis. |
| Não Exemplo | A mera criptografia reversível do dado. |
| QCs relacionadas | QC-P4; QC-P7 |
| Uso previsto em OpenAPI | Direto em Operation Objects por anotação de tipo de tratamento, desde que a descrição funcional, os dados e o fluxo sustentem a classificação. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto principalmente na Etapa 4; apoia Finalidades/Consentimento na Etapa 5 e requisitos/rastreabilidade nas Etapas 6 a 8. |

## C41 - Pseudonimização

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Tratamento e operações |
| Estereótipo | «subkind» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Especialização de Operação de TDP que representa uma situação relacional na qual Dados Pessoais têm elementos identificadores substituídos ou separados, resultando em Dados Pseudonimizados indiretamente identificáveis. |
| Definição normativa | ABNT NBR ISO/IEC 29100:2020:<br>2.22 Pseudonimização: Processo aplicado aos dados pessoais (DP) que substitui informação identificável por um pseudônimo.<br><br>NOTA 1: Pseudonimização pode ser realizada, tanto pelos titulares de DP, quanto pelos controladores de DP. A pseudonimização pode ser usada pelos titulares de DP para usar consistentemente um recurso ou serviço sem divulgar a sua identidade para este recurso ou serviço (ou entre serviços), ainda assim sendo responsabilizada por este uso.<br><br>NOTA 2: A pseudonimização não exclui a possibilidade de que possa haver (um conjunto restrito de) partes interessadas na privacidade, que não sejam o controlador de DP do dado pseudonimizado, que sejam capazes de determinar a identidade do titular de DP, com base no pseudônimo e nos dados conectados a ele.<br><br>LGPD - Lei nº 13.709/2018:<br>(Redação dada pela Lei nº 13.853, de 2019) <br><br>(Art. 13º) Art. 13. § 4º Para os efeitos deste artigo, a PSEUDONIMIZAÇÃO é o tratamento por meio do qual um dado perde a possibilidade de associação, direta ou indireta, a um indivíduo, senão pelo uso de informação adicional mantida separadamente pelo controlador em ambiente controlado e seguro.<br><br>Glossário ANPD - Resolução CD/ANPD nº 1/2021:<br>(Resolução CD/ANPD nº 1/2021.)<br><br>PSEUDONIMIZAÇÃO: Tratamento por meio do qual um dado perde a possibilidade de associação, direta ou indireta, a um indivíduo, senão pelo uso de informação adicional mantida separadamente pelo controlador em ambiente controlado e seguro. |
| Fonte | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020; LGPD - Lei nº 13.709/2018; Glossário ANPD - Resolução CD/ANPD nº 1/2021 |
| Superconceito | Operação de TDP |
| Subconceitos | - |
| Relações | R15 resulta em (Pseudonimização) - Dado Pseudonimizado [1..*] |
| Restrições | GS05 membro de {overlapping, incomplete} |
| Sinônimos | - |
| Exemplo | A substituição do nome por código, mantendo a chave de correspondência separada. |
| Não Exemplo | A destruição definitiva do vínculo com a pessoa. |
| QCs relacionadas | QC-P4; QC-P7 |
| Uso previsto em OpenAPI | Direto em Operation Objects por anotação de tipo de tratamento, desde que a descrição funcional, os dados e o fluxo sustentem a classificação. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto principalmente na Etapa 4; apoia Finalidades/Consentimento na Etapa 5 e requisitos/rastreabilidade nas Etapas 6 a 8. |

## C42 - Consentimento

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Consentimento e finalidade |
| Estereótipo | «relator» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Relator que representa a manifestação livre, informada e inequívoca de um Titular de DP, dirigida a Controladores, relativa a determinado TDP e a Finalidades determinadas, sem avaliar sua validade jurídica. |
| Definição normativa | ABNT NBR ISO/IEC 29100:2020:<br>2.4 CONSENTIMENTO: CONCORDÂNCIA, específica e informada, dada livremente pelo TITULAR DE DADOS PESSOAIS (DP) para o TRATAMENTO DE SEUS DP.<br><br>LGPD - Lei nº 13.709/2018:<br>(Redação dada pela Lei nº 13.853, de 2019) <br><br>(Art. 5º) XII - CONSENTIMENTO: manifestação livre, informada e inequívoca pela qual o TITULAR CONCORDA COM O TRATAMENTO DE SEUS DADOS PESSOAIS para uma finalidade determinada; |
| Fonte | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020; LGPD - Lei nº 13.709/2018 |
| Superconceito | - |
| Subconceitos | - |
| Relações | R12 refere-se a (Consentimento–Finalidade) - Finalidade [1..*]<br>R16 tem escopo - Tratamento de Dados Pessoais (TDP) [1]<br>R17 é dirigido a - Controlador [1..*]<br>R19 é manifestado por - Titular de DP [0..*] |
| Restrições | - |
| Sinônimos | - |
| Exemplo | A manifestação registrada do Titular para receber comunicações promocionais relativas a finalidade determinada. |
| Não Exemplo | Um token OAuth ou uma regra técnica de acesso, isoladamente. |
| QCs relacionadas | QC-P6 |
| Uso previsto em OpenAPI | Condicional e normalmente dependente de extensão específica ou metadado contextual; não inferir na anotação básica sem evidência explícita. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto principalmente na Etapa 5; fundamenta requisitos, rastreabilidade e pontos de validação nas Etapas 6 a 8. |

## C43 - Finalidade

| Campo | Conteúdo |
| --- | --- |
| Agrupamento de apresentação | Consentimento e finalidade |
| Estereótipo | «mode» |
| Abstrato ou concreto | Concreto |
| Definição ontológica | Modo existencialmente dependente de um TDP que expressa o propósito determinado para o qual o tratamento é realizado, orientando e delimitando suas operações e as decisões dos agentes. |
| Definição normativa | LGPD, art. 6º, I - princípio da finalidade: realização do tratamento para propósitos legítimos, específicos, explícitos e informados ao Titular, sem possibilidade de tratamento posterior incompatível com essas finalidades. |
| Fonte | OntoPrivacy v2; LGPD - Lei nº 13.709/2018 - rastreabilidade herdada |
| Superconceito | - |
| Subconceitos | - |
| Relações | R07 define - Controlador [1..*]<br>R12 refere-se a (Consentimento–Finalidade) - Consentimento [0..*]<br>R18 é informada ao - Titular de DP [0..*]<br>R20 é orientado por - Tratamento de Dados Pessoais (TDP) [1] |
| Restrições | - |
| Sinônimos | Finalidade do Tratamento; Propósito do Tratamento |
| Exemplo | “Emitir o certificado do curso” como propósito do TDP correspondente. |
| Não Exemplo | “Consentimento” ou “legítimo interesse”, que são condição/hipótese e não propósito; ou “coletar dados”, que é operação. |
| QCs relacionadas | QC-P5; QC-P6 |
| Uso previsto em OpenAPI | Condicional e normalmente dependente de extensão específica ou metadado contextual; não inferir na anotação básica sem evidência explícita. |
| Uso previsto no GERPD alinhado à v2 | Uso previsto principalmente na Etapa 5; fundamenta requisitos, rastreabilidade e pontos de validação nas Etapas 6 a 8. |
