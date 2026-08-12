# Adendos de Retorno AR-01 a AR-07

Os textos abaixo foram extraídos das respostas brutas e preservam a formulação original da execução.

## 3. Adendo de Retorno — Etapa 1

**AR-01 — atualização contextual de AN-01, sem substituição da saída original.**

A Etapa 2 revelou que C01/C02 registram **nome do pai e nome da mãe do aluno** (DP-11 e DP-12). Assim, o campo **“Usuários, perfis e partes interessadas”** de AN-01 fica complementado com: **pai do aluno e mãe do aluno, exclusivamente como pessoas naturais cujos nomes são representados nos dados cadastrais do aluno; não há evidência de que interajam com o Tibico, possuam perfil de usuário ou desempenhem qualquer papel adicional no sistema**. Essa atualização não altera o escopo integral definido na Etapa 1 e não impede o prosseguimento da aplicação.

## 3. Adendos de Retorno

**AR-02 — Retorno à Etapa 4 — OP-20.**

A análise de finalidade/necessidade evidenciou que, no caso de uso **Controlar Turma — Alocar Professor**, C02 afirma que o sistema exibe “os professores disponíveis de horário e que a área da disciplina seja igual à área de atuação do professor”, mas **não explicita que o nome DP-01 seja um campo efetivamente exibido**. 

Assim, preservando a saída original da Etapa 4, o estado acumulado passa a considerar **OP-20 corrigido por adendo** da seguinte forma: **DP-26 — Área de atuação do professor; DP-28 — horário/disponibilidade associada à alocação / Disponibilização / AG-08 → AG-03 / finalidade: apoiar a alocação de professor à turma**. **DP-01 deixa de ser considerado vínculo confirmado de OP-20 e passa a A verificar nesse contexto específico.**

Não são necessários outros Adendos de Retorno para as Etapas 1 a 4.

## 3. Adendos de Retorno gerados nesta etapa

### AR-03 — Retorno à Etapa 5 — refinamento de FA-17

**Saída original preservada:** FA-17 havia registrado **“Dado necessário? Sim, no nível funcional documentado”** para DP-29, DP-30 e DP-32.

A revisão evidencia que C01 sustenta a necessidade funcional de **credenciais de login e senha**, mas não demonstra a necessidade específica de utilizar **a matrícula como nome de usuário do aluno** e **o CPF como nome de usuário do professor**. C01/RN10 apenas determina essa composição. 

O estado acumulado de **FA-17 — Dado necessário?** passa a ser:

**Parcial — a existência de identificador de acesso e senha é requerida funcionalmente por RNF01; a necessidade específica de utilizar matrícula e CPF como valores dos nomes de usuário permanece A verificar.**

Os demais campos de FA-17 permanecem inalterados.

### AR-04 — Retorno à Etapa 6 — inclusão de RP-44

É acrescentado, sem renumeração dos requisitos anteriores:

| ID        | Elemento derivado                                                                                                                                                                                                                                  | Tipo de elemento derivado | Origem da derivação                                               | Conceitos da OntoPrivacy        | Ponto de validação                                                                                                                               |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ----------------------------------------------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **RP-44** | **A instituição de ensino deve definir e documentar a necessidade de utilizar a matrícula como nome de usuário do aluno e o CPF como nome de usuário do professor, distinguindo a necessidade de autenticação da escolha desses identificadores.** | **Negócio**               | DP-04, DP-10, DP-29, DP-30; OP-17; FA-17 conforme AR-03; C01/RN10 | **Dado Pessoal; Armazenamento** | A autenticação é funcionalmente requerida, mas a escolha específica de matrícula/CPF como identificadores de acesso não é justificada no corpus. |

### AR-05 — Retorno à Etapa 7 — inclusão da rastreabilidade de RP-44

| ID do requisito | Conceito da OntoPrivacy     | Fonte normativa / conceitual                          | Dado pessoal               | Operação | Agente / ator       | Artefato / evidência                                                                                                                                                                               | Status        |
| --------------- | --------------------------- | ----------------------------------------------------- | -------------------------- | -------- | ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| **RP-44**       | Dado Pessoal; Armazenamento | GERPD; OntoPrivacy; LGPD/ISO/IEC 29100 em nível geral | DP-04; DP-10; DP-29; DP-30 | OP-17    | AG-01; AG-02; AG-08 | C01/RN10 determina matrícula como login do aluno e CPF como login do professor; FA-17, refinado por AR-03, distingue necessidade da autenticação da necessidade desses identificadores específicos | **A validar** |

### AR-06 — Retorno à Etapa 6 — inclusão de RP-45

A revisão da cadeia FA-35–FA-41 mostrou que a necessidade individual dos campos dos relatórios havia sido registrada como **A verificar**, mas não havia sido convertida em requisito candidato específico.

É acrescentado:

| ID        | Elemento derivado                                                                                                                                                                                                 | Tipo de elemento derivado | Origem da derivação                                             | Conceitos da OntoPrivacy                     | Ponto de validação                                                                                                                                 |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | --------------------------------------------------------------- | -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **RP-45** | **A instituição de ensino deve definir e documentar a necessidade de cada dado pessoal incluído no Relatório de Resultados, Boletim, Histórico e respectivas exportações em relação à finalidade de cada saída.** | **Negócio**               | FA-35–FA-41; OP-35–OP-41; DP-34–DP-36 e respectivos componentes | **Dado Pessoal; Consulta; Disponibilização** | Validar individualmente os campos das saídas, preservando PA-18 quanto à divergência de frequência e PA-19 quanto à abrangência da exportação PDF. |

### AR-07 — Retorno à Etapa 7 — inclusão da rastreabilidade de RP-45

| ID do requisito | Conceito da OntoPrivacy                  | Fonte normativa / conceitual                          | Dado pessoal                                                                  | Operação    | Agente / ator                                | Artefato / evidência                                                                                                                                   | Status        |
| --------------- | ---------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------------------------------- | ----------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------- |
| **RP-45**       | Dado Pessoal; Consulta; Disponibilização | GERPD; OntoPrivacy; LGPD/ISO/IEC 29100 em nível geral | DP-01; DP-10; DP-13; DP-16; DP-19–DP-24; DP-34–DP-36, conforme cada relatório | OP-35–OP-41 | AG-01; AG-02; AG-03; AG-08, conforme a saída | C01, descrição de relatório de resultados, boletim e histórico; C02/Tabela 5; FA-35–FA-41 registram necessidade individual dos campos como A verificar | **A validar** |

Com **AR-03 a AR-07**, o estado acumulado da aplicação passa a conter **RP-01 a RP-45**, preservando integralmente os registros anteriores e os Adendos **AR-01** e **AR-02**.
