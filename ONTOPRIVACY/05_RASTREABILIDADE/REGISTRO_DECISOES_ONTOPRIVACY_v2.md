# Registro de Decisões Ontológicas — OntoPrivacy v2

## 1. Identificação

- **Artefato:** OntoPrivacy — Ontologia de Referência de Domínio de Privacidade de Dados.
- **Versão canônica:** v2.
- **Artefatos canônicos:** `OntoPrivacy_v2.asta` e `OntoPrivacy_v2.png`.
- **Estado:** fechamento documental concluído.
- **Natureza:** ontologia de referência de domínio, em nível conceitual.

## 2. Decisões 1 consolidadas

| ID | Decisão | Justificativa / consequência |
|---|---|---|
| DEC-V2-01 | A OntoPrivacy v2 é uma ontologia de referência de domínio em nível conceitual. | O artefato prioriza a conceituação do domínio e a comunicação semântica; não é apresentado como ontologia operacional plenamente processável. |
| DEC-V2-02 | LGPD e ABNT NBR ISO/IEC 29100:2020 constituem as fontes centrais. | A LGPD fornece a ancoragem normativa brasileira e a ISO/IEC 29100 complementa a terminologia e a estrutura de privacidade. |
| DEC-V2-03 | UFO fornece a fundamentação ontológica e OntoUML a linguagem de representação. | A classificação dos conceitos explicita identidade, rigidez, dependência e natureza relacional. |
| DEC-V2-04 | O modelo permanece em um único diagrama. | A apresentação única foi escolhida para a versão da dissertação; agrupamentos temáticos serão usados apenas na explicação textual. |
| DEC-V2-05 | A conceituação é organizada por três `relators`: Identificabilidade, Tratamento de Dados Pessoais e Consentimento. | Esses relatores articulam, respectivamente, dado–titular, tratamento–participantes–dados e manifestação–titular–controlador–TDP–finalidade. |
| DEC-V2-06 | Finalidade é um `mode` dependente de Tratamento de Dados Pessoais. | A finalidade representa o propósito particular do TDP, independentemente da existência de Consentimento. |
| DEC-V2-07 | `Exclusão` é o rótulo canônico; `Eliminação` é sinônimo normativo. | Preserva a terminologia adotada no modelo e a rastreabilidade ao art. 5º, XIV, da LGPD. |
| DEC-V2-08 | Base Legal não integra o núcleo conceitual da v2. | A ontologia não pretende determinar hipóteses jurídicas nem licitude; Base Legal permanece externa, podendo ser tratada pelo GERPD. |
| DEC-V2-09 | Ator Autorizado, Ator Desautorizado e TDP Autorizado não integram a v2. | Autorização técnica ou jurídica não é tratada como classificação ontológica central nesta versão. |
| DEC-V2-10 | A OntoPrivacy não é mecanismo de conformidade. | A existência de conceitos, Consentimento ou Finalidade não implica validade jurídica, licitude ou certificação de conformidade. |
| DEC-V2-11 | Versões anteriores estão descontinuadas como fonte da conceituação atual. | Podem ser preservadas somente para a rastreabilidade histórica dos Estudos I e II. |

## 3. Limites deliberadamente adiados

Os itens abaixo são registrados como **limites da versão v2**, e não como erros pendentes que impeçam seu congelamento:

| ID | Limite adiado | Tratamento na v2 |
|---|---|---|
| LIM-V2-01 | Relações `derivation` não registradas semanticamente na ferramenta. | A fundamentação conceitual pode ser descrita textualmente ou apresentada graficamente; a formalização fica para evolução futura. |
| LIM-V2-02 | Restrições formais adicionais entre os três relatores. | Não integram o critério de congelamento da v2. |
| LIM-V2-03 | Revisão formal exaustiva da correspondência entre todas as definições narrativas e cardinalidades. | Eventuais refinamentos serão tratados em versão futura, sem reabrir a linha de base atual. |
| LIM-V2-04 | Nomes nos extremos das associações. | Permanecem ausentes na v2; a leitura é sustentada pelos rótulos das associações e pelo catálogo futuro. |
| LIM-V2-05 | Cobertura integral das categorias de Dados Pessoais Sensíveis. | A taxonomia é deliberadamente parcial e extensível. |
| LIM-V2-06 | Identificadores semânticos estáveis para conceitos e relações. | Serão atribuídos em atividade posterior, sem alterar a conceituação já congelada. |
| LIM-V2-07 | Operacionalização em OWL/OCL/SHACL ou linguagem equivalente. | Fora do escopo da dissertação atual; possível evolução futura. |

## 4. Regras de governança

1. Alterações futuras devem gerar nova versão e registro explícito no changelog.
2. O diagrama e o arquivo ASTA devem manter o mesmo número de versão.
3. Evidências brutas dos Estudos I e II não devem ser reescritas retroativamente.
4. Atualizações no Capítulo 3, no GERPD e no Capítulo 4 devem usar uma matriz de migração conceitual.
5. A OntoPrivacy v2 deve ser a fonte canônica da redação final da Seção 3.1.

## 5. Decisões 2 documentais

| ID | Decisão | Justificativa / consequência |
| --- | --- | --- |
| DEC-V2-12 | O produto integrado será denominado Catálogo OntoPrivacy. | O catálogo consolida conceitos, relações, conjuntos de generalização, restrição, atributo, fontes e orientações de uso, sem alterar o ASTA ou o PNG. |
| DEC-V2-13 | As definições são documentadas em duas camadas: ontológica e normativa/conceitual. | A definição ontológica explicita a decisão da OntoPrivacy; a definição normativa preserva ou referencia o texto-fonte registrado. |
| DEC-V2-14 | A Matriz Conceito–Fonte distingue rastreabilidade direta, herdada/relacionada e transversal. | Evita atribuir silenciosamente uma fonte normativa diretamente a uma classe quando o apoio é herdado de superconceito ou conceito relacionado. |
| DEC-V2-15 | Os códigos C01–C43, R01–R21, GS01–GS07, REST01 e ATT01 são identificadores documentais do catálogo. | Esses códigos não constituem IRIs ou identificadores semânticos estáveis; a decisão LIM-V2-06 permanece adiada. |
| DEC-V2-16 | O campo “QCs relacionadas” utiliza códigos provisórios QC-P1–QC-P7. | O mapeamento é apenas preparatório. |
| DEC-V2-17 | Os campos de uso em OpenAPI e GERPD representam orientação de uso alinhada à v2, não evidência histórica dos Estudos I e II. | Preserva a rastreabilidade dos estudos e evita reclassificação retroativa de artefatos históricos. |
| DEC-V2-18 | Conceitos sem definição normativa direta mantêm definição ontológica autoral e fonte explicitamente indicada como autoral. | O catálogo não preenche lacunas normativas com atribuições não registradas; quando há apoio herdado, ele é qualificado. |
| DEC-V2-19 | Não modifica a estrutura congelada da OntoPrivacy v2. | Os 43 conceitos, 21 associações, 36 generalizações, sete conjuntos, uma restrição e um atributo permanecem inalterados. |

## 6. Estado após a Decisões 2

- A estrutura da OntoPrivacy v2 permanece inalterada.
- O Catálogo OntoPrivacy passa a ser a documentação canônica complementar ao ASTA e ao PNG.
- Os mapeamentos para QCs e usos em OpenAPI/GERPD são preparatórios e não substituem a validação nem as evidências históricas dos Estudos I e II.

## 7. Decisões 3

| ID | Decisão | Justificativa / consequência |
| --- | --- | --- |
| DEC-V2-20 | As sete QCs provisórias QC-P1–QC-P7 são promovidas, após revisão, às QCs canônicas QC1–QC7. | As versões longas constituem a formulação formal; as versões curtas são equivalentes de apresentação e consulta rápida. |
| DEC-V2-21 | Cada QC possui cenário positivo e cenário negativo ou limítrofe. | A validação demonstra tanto a capacidade representacional quanto o limite de inferência na ausência de evidência. |
| DEC-V2-22 | As QCs cobrem os 43 conceitos e as 21 associações catalogadas. | Nenhum conceito ou relação do núcleo permanece sem mobilização por ao menos uma QC. |
| DEC-V2-23 | A validação conceitual utiliza instanciação exemplificativa e inspeção manual. | A OntoPrivacy v2 permanece ontologia de referência, sem pretensão de consulta operacional automática. |
| DEC-V2-24 | Cenários negativos validam a regra de não inferência sem evidência suficiente. | Métodos HTTP, perfis técnicos, tokens e criptografia não são tratados automaticamente como operações, papéis, Consentimento ou Anonimização. |
| DEC-V2-25 | Base Legal, Ator Autorizado, Ator Desautorizado e TDP Autorizado permanecem excluídos das QCs. | A aprovação do Gate G3 não reabre decisões fixas nem amplia silenciosamente o escopo. |
| DEC-V2-26 | As lacunas identificadas são registradas como limites de escopo, limites metodológicos ou evoluções futuras. | Nenhuma delas impede a respondibilidade conceitual das QCs na v2. |
| DEC-V2-27 | Com a aprovação do Gate G3, a OntoPrivacy v2 é congelada como fonte canônica da dissertação. | Qualquer mudança estrutural ou semântica posterior exige solicitação formal e nova versão; o trabalho seguinte concentra-se na revisão textual do Capítulo 3 e na sincronização controlada dos artefatos. |
