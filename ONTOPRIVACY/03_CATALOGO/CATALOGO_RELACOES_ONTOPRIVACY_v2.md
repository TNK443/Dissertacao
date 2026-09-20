# Catálogo de Relações - OntoPrivacy v2

Este documento cataloga as 21 associações da OntoPrivacy v2. Os códigos R01–R21 são identificadores documentais e correspondem ao inventário aprovado no Gate G1.

## R01 - integra (Dado–Conjunto de Dados)

| Campo | Conteúdo |
| --- | --- |
| Rótulo no modelo | (sem rótulo no diagrama) |
| Estereótipo | «memberOf» |
| Extremo A | Conjunto de Dados [0..*; agregação=composite] |
| Extremo B | Dado [2..*; agregação=none] |
| Definição | Um Dado integra um Conjunto de Dados quando é considerado membro do coletivo segundo o critério de organização adotado. |
| Fonte e rastreabilidade | OntoPrivacy v2; UFO/OntoUML (memberOf) |
| Restrições/observações | - |
| QCs relacionadas | QC-P1 |
| Uso em OpenAPI | A relação pode orientar anotações contextuais quando ambos os extremos estiverem evidenciados; a abordagem básica não deve inferi-la apenas pela estrutura sintática. |
| Uso no GERPD | Apoia a ligação entre achados nas etapas indicadas pelas QCs e a rastreabilidade nas Etapas 6–8. |

## R02 - integra (Dado Pessoal–Banco de Dados DP)

| Campo | Conteúdo |
| --- | --- |
| Rótulo no modelo | (sem rótulo no diagrama) |
| Estereótipo | «memberOf» |
| Extremo A | Banco de Dados DP [0..*; agregação=composite] |
| Extremo B | Dado Pessoal (DP) [2..*; agregação=none] |
| Definição | Um Dado Pessoal integra um Banco de Dados DP quando é organizado como membro desse banco. |
| Fonte e rastreabilidade | OntoPrivacy v2; LGPD, art. 5º, IV; UFO/OntoUML (memberOf) |
| Restrições/observações | - |
| QCs relacionadas | QC-P1 |
| Uso em OpenAPI | A relação pode orientar anotações contextuais quando ambos os extremos estiverem evidenciados; a abordagem básica não deve inferi-la apenas pela estrutura sintática. |
| Uso no GERPD | Apoia a ligação entre achados nas etapas indicadas pelas QCs e a rastreabilidade nas Etapas 6–8. |

## R03 - é composto por

| Campo | Conteúdo |
| --- | --- |
| Rótulo no modelo | (sem rótulo no diagrama) |
| Estereótipo | associação comum |
| Extremo A | Conjunto de Operações de TDP [0..*; agregação=aggregate] |
| Extremo B | Operação de TDP [2..*; agregação=none] |
| Definição | Um Conjunto de Operações de TDP reúne duas ou mais Operações de TDP pertencentes ao mesmo contexto de tratamento. |
| Fonte e rastreabilidade | OntoPrivacy v2; LGPD, art. 5º, X; ABNT NBR ISO/IEC 29100:2020, item 2.21 |
| Restrições/observações | Cada Conjunto reúne 2..* Operações; a associação usa agregação compartilhada no ASTA. |
| QCs relacionadas | QC-P4 |
| Uso em OpenAPI | A relação pode orientar anotações contextuais quando ambos os extremos estiverem evidenciados; a abordagem básica não deve inferi-la apenas pela estrutura sintática. |
| Uso no GERPD | Apoia a ligação entre achados nas etapas indicadas pelas QCs e a rastreabilidade nas Etapas 6–8. |

## R04 - abrange

| Campo | Conteúdo |
| --- | --- |
| Rótulo no modelo | abrange |
| Estereótipo | «mediation» |
| Extremo A | Tratamento de Dados Pessoais (TDP) [0..*; agregação=none] |
| Extremo B | Dado Pessoal (DP) [1..*; agregação=none] |
| Definição | Tratamento de Dados Pessoais (TDP) ABRANGE 1 (um) ou mais (1..*) Dados Pessoais (DP).<br>Dado Pessoal (DP) RECEBE 0 (nenhum) ou mais (0..*) Tratamento de Dados Pessoais (TDP). |
| Fonte e rastreabilidade | OntoPrivacy v2; LGPD, art. 5º, X; ABNT NBR ISO/IEC 29100:2020, item 2.21 |
| Restrições/observações | - |
| QCs relacionadas | QC-P4; QC-P7 |
| Uso em OpenAPI | A relação pode orientar anotações contextuais quando ambos os extremos estiverem evidenciados; a abordagem básica não deve inferi-la apenas pela estrutura sintática. |
| Uso no GERPD | Apoia a ligação entre achados nas etapas indicadas pelas QCs e a rastreabilidade nas Etapas 6–8. |

## R05 - baseia-se

| Campo | Conteúdo |
| --- | --- |
| Rótulo no modelo | baseia-se |
| Estereótipo | «mediation» |
| Extremo A | Identificabilidade [1..*; agregação=none] |
| Extremo B | Dado Pessoal (DP) [1..*; agregação=none] |
| Definição | Uma Identificabilidade é sustentada pelos Dados Pessoais cuja interpretação isolada ou combinada permite identificar um titular. |
| Fonte e rastreabilidade | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020, item 2.5 |
| Restrições/observações | - |
| QCs relacionadas | QC-P2 |
| Uso em OpenAPI | A relação pode orientar anotações contextuais quando ambos os extremos estiverem evidenciados; a abordagem básica não deve inferi-la apenas pela estrutura sintática. |
| Uso no GERPD | Apoia a ligação entre achados nas etapas indicadas pelas QCs e a rastreabilidade nas Etapas 6–8. |

## R06 - caracteriza

| Campo | Conteúdo |
| --- | --- |
| Rótulo no modelo | caracteriza |
| Estereótipo | «characterization» |
| Extremo A | Anonimidade [1; agregação=none] |
| Extremo B | Dado Anonimizado [1; agregação=none] |
| Definição | A Anonimidade caracteriza o Dado Anonimizado cuja associação a uma pessoa não é possível pelos meios razoáveis considerados. |
| Fonte e rastreabilidade | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020, itens 2.1–2.3; LGPD, art. 5º, III e XI |
| Restrições/observações | - |
| QCs relacionadas | QC-P1; QC-P7 |
| Uso em OpenAPI | A relação pode orientar anotações contextuais quando ambos os extremos estiverem evidenciados; a abordagem básica não deve inferi-la apenas pela estrutura sintática. |
| Uso no GERPD | Apoia a ligação entre achados nas etapas indicadas pelas QCs e a rastreabilidade nas Etapas 6–8. |

## R07 - define

| Campo | Conteúdo |
| --- | --- |
| Rótulo no modelo | define |
| Estereótipo | associação comum |
| Extremo A | Controlador [1..*; agregação=none] |
| Extremo B | Finalidade [1..*; agregação=none] |
| Definição | Um Controlador define uma Finalidade quando, no contexto do TDP pelo qual é responsável, estabelece o propósito que orienta e delimita esse tratamento. |
| Fonte e rastreabilidade | OntoPrivacy v2; LGPD, art. 5º, VI e art. 6º, I; ABNT NBR ISO/IEC 29100:2020, item 2.8 |
| Restrições/observações | - |
| QCs relacionadas | QC-P5 |
| Uso em OpenAPI | A relação pode orientar anotações contextuais quando ambos os extremos estiverem evidenciados; a abordagem básica não deve inferi-la apenas pela estrutura sintática. |
| Uso no GERPD | Apoia a ligação entre achados nas etapas indicadas pelas QCs e a rastreabilidade nas Etapas 6–8. |

## R08 - envolve

| Campo | Conteúdo |
| --- | --- |
| Rótulo no modelo | envolve |
| Estereótipo | «mediation» |
| Extremo A | Tratamento de Dados Pessoais (TDP) [1..*; agregação=none] |
| Extremo B | Parte Interessada na Privacidade [1..*; agregação=none] |
| Definição | Tratamento de Dados Pessoais (TDP) ENVOLVE 1 (um) ou mais (1..*) Parte Interessada na Privacidade.<br>Parte Interessada na Privacidade SE ENVOLVE de 0 (nenhum) ou mais (0..*) Tratatamento de Dados Pessoais (TDP). |
| Fonte e rastreabilidade | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020, item 2.20 |
| Restrições/observações | - |
| QCs relacionadas | QC-P3; QC-P4 |
| Uso em OpenAPI | A relação pode orientar anotações contextuais quando ambos os extremos estiverem evidenciados; a abordagem básica não deve inferi-la apenas pela estrutura sintática. |
| Uso no GERPD | Apoia a ligação entre achados nas etapas indicadas pelas QCs e a rastreabilidade nas Etapas 6–8. |

## R09 - identifica

| Campo | Conteúdo |
| --- | --- |
| Rótulo no modelo | identifica |
| Estereótipo | «mediation» |
| Extremo A | Identificabilidade [1..*; agregação=none] |
| Extremo B | Titular de DP [1; agregação=none] |
| Definição | Uma Identificabilidade conecta os dados que a sustentam ao Titular cuja identidade pode ser estabelecida. |
| Fonte e rastreabilidade | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020, itens 2.5 e 2.9; LGPD, art. 5º, I e V |
| Restrições/observações | - |
| QCs relacionadas | QC-P2 |
| Uso em OpenAPI | A relação pode orientar anotações contextuais quando ambos os extremos estiverem evidenciados; a abordagem básica não deve inferi-la apenas pela estrutura sintática. |
| Uso no GERPD | Apoia a ligação entre achados nas etapas indicadas pelas QCs e a rastreabilidade nas Etapas 6–8. |

## R10 - instrui

| Campo | Conteúdo |
| --- | --- |
| Rótulo no modelo | instrui |
| Estereótipo | «material» |
| Extremo A | Controlador [1..*; agregação=none] |
| Extremo B | Operador [0..*; agregação=none] |
| Definição | Um CONTROLADOR DE DP algumas vezes INSTRUI outros (por exemplo, OPERADORES DE DP) a tratar DP em seu nome, enquanto a responsabilidade pelo tratamento permanece com o CONTROLADOR DE DP. |
| Fonte e rastreabilidade | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020, nota do item 2.8 |
| Restrições/observações | - |
| QCs relacionadas | QC-P3; QC-P4 |
| Uso em OpenAPI | A relação pode orientar anotações contextuais quando ambos os extremos estiverem evidenciados; a abordagem básica não deve inferi-la apenas pela estrutura sintática. |
| Uso no GERPD | Apoia a ligação entre achados nas etapas indicadas pelas QCs e a rastreabilidade nas Etapas 6–8. |

## R11 - realiza

| Campo | Conteúdo |
| --- | --- |
| Rótulo no modelo | realiza |
| Estereótipo | «mediation» |
| Extremo A | Operador [0..*; agregação=none] |
| Extremo B | Tratamento de Dados Pessoais (TDP) [1..*; agregação=none] |
| Definição | Um Operador realiza um TDP quando executa as operações que o compõem em nome do Controlador.<br>O Operador que realiza um TDP deve executar suas operações dentro dos limites das Finalidades que caracterizam esse tratamento. |
| Fonte e rastreabilidade | OntoPrivacy v2; LGPD, art. 5º, VII; ABNT NBR ISO/IEC 29100:2020, item 2.10 |
| Restrições/observações | - |
| QCs relacionadas | QC-P3; QC-P4 |
| Uso em OpenAPI | A relação pode orientar anotações contextuais quando ambos os extremos estiverem evidenciados; a abordagem básica não deve inferi-la apenas pela estrutura sintática. |
| Uso no GERPD | Apoia a ligação entre achados nas etapas indicadas pelas QCs e a rastreabilidade nas Etapas 6–8. |

## R12 - refere-se a (Consentimento–Finalidade)

| Campo | Conteúdo |
| --- | --- |
| Rótulo no modelo | refere-se a |
| Estereótipo | associação comum |
| Extremo A | Consentimento [0..*; agregação=none] |
| Extremo B | Finalidade [1..*; agregação=none] |
| Definição | As Finalidades referidas por um Consentimento devem pertencer ao TDP que está no escopo desse Consentimento.<br><br>Notação resumida:<br>Finalidades do Consentimento<br>    ⊆<br>Finalidades do TDP em seu escopo |
| Fonte e rastreabilidade | OntoPrivacy v2; LGPD, art. 5º, XII e art. 6º, I |
| Restrições/observações | As Finalidades referidas devem pertencer ao TDP no escopo do Consentimento (regra textual da associação). |
| QCs relacionadas | QC-P6 |
| Uso em OpenAPI | A relação pode orientar anotações contextuais quando ambos os extremos estiverem evidenciados; a abordagem básica não deve inferi-la apenas pela estrutura sintática. |
| Uso no GERPD | Apoia a ligação entre achados nas etapas indicadas pelas QCs e a rastreabilidade nas Etapas 6–8. |

## R13 - refere-se a (Dado Pessoal–Titular)

| Campo | Conteúdo |
| --- | --- |
| Rótulo no modelo | refere-se a |
| Estereótipo | «material» |
| Extremo A | Dado Pessoal (DP) [1..*; agregação=none] |
| Extremo B | Titular de DP [1..*; agregação=none] |
| Definição | Dado Pessoal «material» refere-se a Titular.<br>Identificabilidade  «derivation» Dado Pessoal refere-se a Titular. |
| Fonte e rastreabilidade | OntoPrivacy v2; LGPD, art. 5º, I e V; ABNT NBR ISO/IEC 29100:2020, itens 2.5, 2.7 e 2.9 |
| Restrições/observações | Relação material conceitualmente fundamentada por Identificabilidade; derivation formal adiada na v2. |
| QCs relacionadas | QC-P2 |
| Uso em OpenAPI | A relação pode orientar anotações contextuais quando ambos os extremos estiverem evidenciados; a abordagem básica não deve inferi-la apenas pela estrutura sintática. |
| Uso no GERPD | Apoia a ligação entre achados nas etapas indicadas pelas QCs e a rastreabilidade nas Etapas 6–8. |

## R14 - resulta em (Anonimização)

| Campo | Conteúdo |
| --- | --- |
| Rótulo no modelo | resulta em |
| Estereótipo | «mediation» |
| Extremo A | Anonimização [1; agregação=none] |
| Extremo B | Dado Anonimizado [1..*; agregação=none] |
| Definição | Uma Anonimização resulta em um Dado Anonimizado quando esse dado é produzido como resultado da aplicação dos meios de anonimização. |
| Fonte e rastreabilidade | OntoPrivacy v2; LGPD, art. 5º, III e XI; ABNT NBR ISO/IEC 29100:2020, itens 2.2 e 2.3 |
| Restrições/observações | - |
| QCs relacionadas | QC-P7 |
| Uso em OpenAPI | A relação pode orientar anotações contextuais quando ambos os extremos estiverem evidenciados; a abordagem básica não deve inferi-la apenas pela estrutura sintática. |
| Uso no GERPD | Apoia a ligação entre achados nas etapas indicadas pelas QCs e a rastreabilidade nas Etapas 6–8. |

## R15 - resulta em (Pseudonimização)

| Campo | Conteúdo |
| --- | --- |
| Rótulo no modelo | resulta em |
| Estereótipo | «mediation» |
| Extremo A | Pseudonimização [1; agregação=none] |
| Extremo B | Dado Pseudonimizado [1..*; agregação=none] |
| Definição | Uma Pseudonimização resulta em um Dado Pseudonimizado quando o dado produzido depende de informação adicional separada para associação ao titular. |
| Fonte e rastreabilidade | OntoPrivacy v2; LGPD, art. 13, §4º; ABNT NBR ISO/IEC 29100:2020, item 2.22; Glossário ANPD |
| Restrições/observações | - |
| QCs relacionadas | QC-P7 |
| Uso em OpenAPI | A relação pode orientar anotações contextuais quando ambos os extremos estiverem evidenciados; a abordagem básica não deve inferi-la apenas pela estrutura sintática. |
| Uso no GERPD | Apoia a ligação entre achados nas etapas indicadas pelas QCs e a rastreabilidade nas Etapas 6–8. |

## R16 - tem escopo

| Campo | Conteúdo |
| --- | --- |
| Rótulo no modelo | tem escopo |
| Estereótipo | associação comum |
| Extremo A | Consentimento [0..*; agregação=none] |
| Extremo B | Tratamento de Dados Pessoais (TDP) [1; agregação=none] |
| Definição | Cada Consentimento tem (1) TDP em seu escopo;<br>Cada TDP pode estar no escopo de (0..*) Consentimentos.<br><br>NOTA: A relação 'tem escopo' conecta cada Consentimento ao Tratamento de Dados Pessoais específico ao qual a manifestação se refere. A OntoPrivacy não representa, nesta versão, o ciclo de vida, a revogação ou a evolução temporal desse escopo. |
| Fonte e rastreabilidade | OntoPrivacy v2; LGPD, art. 5º, XII |
| Restrições/observações | - |
| QCs relacionadas | QC-P6 |
| Uso em OpenAPI | A relação pode orientar anotações contextuais quando ambos os extremos estiverem evidenciados; a abordagem básica não deve inferi-la apenas pela estrutura sintática. |
| Uso no GERPD | Apoia a ligação entre achados nas etapas indicadas pelas QCs e a rastreabilidade nas Etapas 6–8. |

## R17 - é dirigido a

| Campo | Conteúdo |
| --- | --- |
| Rótulo no modelo | é dirigido a |
| Estereótipo | «mediation» |
| Extremo A | Consentimento [0..*; agregação=none] |
| Extremo B | Controlador [1..*; agregação=none] |
| Definição | Cada Consentimento é dirigido a (1..*) Controladores;<br>Cada Controlador pode receber (0..*) Consentimentos. |
| Fonte e rastreabilidade | OntoPrivacy v2; LGPD, art. 5º, VI e XII; ABNT NBR ISO/IEC 29100:2020, itens 2.4 e 2.8 |
| Restrições/observações | - |
| QCs relacionadas | QC-P6 |
| Uso em OpenAPI | A relação pode orientar anotações contextuais quando ambos os extremos estiverem evidenciados; a abordagem básica não deve inferi-la apenas pela estrutura sintática. |
| Uso no GERPD | Apoia a ligação entre achados nas etapas indicadas pelas QCs e a rastreabilidade nas Etapas 6–8. |

## R18 - é informada ao

| Campo | Conteúdo |
| --- | --- |
| Rótulo no modelo | é informada ao |
| Estereótipo | associação comum |
| Extremo A | Finalidade [0..*; agregação=none] |
| Extremo B | Titular de DP [0..*; agregação=none] |
| Definição | Para atendimento ao princípio da finalidade, a Finalidade deve ser informada aos Titulares relacionados aos Dados Pessoais abrangidos pelo TDP. |
| Fonte e rastreabilidade | OntoPrivacy v2; LGPD, art. 6º, I e art. 9º |
| Restrições/observações | - |
| QCs relacionadas | QC-P5 |
| Uso em OpenAPI | A relação pode orientar anotações contextuais quando ambos os extremos estiverem evidenciados; a abordagem básica não deve inferi-la apenas pela estrutura sintática. |
| Uso no GERPD | Apoia a ligação entre achados nas etapas indicadas pelas QCs e a rastreabilidade nas Etapas 6–8. |

## R19 - é manifestado por

| Campo | Conteúdo |
| --- | --- |
| Rótulo no modelo | é manifestado por |
| Estereótipo | «mediation» |
| Extremo A | Consentimento [0..*; agregação=none] |
| Extremo B | Titular de DP [0..*; agregação=none] |
| Definição | Cada Consentimento é manifestado por (1) Titular de DP;<br>Cada Titular de DP pode manifestar (0..*) Consentimentos. |
| Fonte e rastreabilidade | OntoPrivacy v2; LGPD, art. 5º, V e XII; ABNT NBR ISO/IEC 29100:2020, itens 2.4 e 2.9 |
| Restrições/observações | - |
| QCs relacionadas | QC-P6 |
| Uso em OpenAPI | A relação pode orientar anotações contextuais quando ambos os extremos estiverem evidenciados; a abordagem básica não deve inferi-la apenas pela estrutura sintática. |
| Uso no GERPD | Apoia a ligação entre achados nas etapas indicadas pelas QCs e a rastreabilidade nas Etapas 6–8. |

## R20 - é orientado por

| Campo | Conteúdo |
| --- | --- |
| Rótulo no modelo | é orientado por |
| Estereótipo | «characterization» |
| Extremo A | Tratamento de Dados Pessoais (TDP) [1; agregação=none] |
| Extremo B | Finalidade [1..*; agregação=none] |
| Definição | Um Tratamento de Dados Pessoais é orientado por uma ou mais Finalidades. Cada Finalidade caracteriza exatamente um TDP e expressa o propósito que orienta e delimita as operações realizadas sobre os Dados Pessoais. |
| Fonte e rastreabilidade | OntoPrivacy v2; LGPD, art. 6º, I |
| Restrições/observações | Cada Finalidade caracteriza exatamente um TDP; cada TDP é orientado por 1..* Finalidades. |
| QCs relacionadas | QC-P5 |
| Uso em OpenAPI | A relação pode orientar anotações contextuais quando ambos os extremos estiverem evidenciados; a abordagem básica não deve inferi-la apenas pela estrutura sintática. |
| Uso no GERPD | Apoia a ligação entre achados nas etapas indicadas pelas QCs e a rastreabilidade nas Etapas 6–8. |

## R21 - é responsável pelo

| Campo | Conteúdo |
| --- | --- |
| Rótulo no modelo | é responsável pelo |
| Estereótipo | «mediation» |
| Extremo A | Controlador [1..*; agregação=none] |
| Extremo B | Tratamento de Dados Pessoais (TDP) [1..*; agregação=none] |
| Definição | Um Controlador é responsável por um TDP quando possui competência decisória sobre seus objetivos e meios. |
| Fonte e rastreabilidade | OntoPrivacy v2; LGPD, art. 5º, VI; ABNT NBR ISO/IEC 29100:2020, item 2.8 |
| Restrições/observações | - |
| QCs relacionadas | QC-P3; QC-P4 |
| Uso em OpenAPI | A relação pode orientar anotações contextuais quando ambos os extremos estiverem evidenciados; a abordagem básica não deve inferi-la apenas pela estrutura sintática. |
| Uso no GERPD | Apoia a ligação entre achados nas etapas indicadas pelas QCs e a rastreabilidade nas Etapas 6–8. |
