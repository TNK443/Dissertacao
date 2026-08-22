# Elementos Complementares do Catálogo — OntoPrivacy v2

## Conjuntos de generalização

| ID | Superconceito | Subconceitos | Condição | Interpretação | Fonte | QCs |
| --- | --- | --- | --- | --- | --- | --- |
| GS01 | Agente Legal | Pessoa Natural; Pessoa Jurídica | {disjoint, complete} | Todo Agente Legal é Pessoa Natural ou Pessoa Jurídica, e nenhuma instância pertence simultaneamente aos dois tipos. | OntoPrivacy v2; UFO/OntoUML; decisão de modelagem | QC-P3 |
| GS02 | Dado | Dado Pessoal (DP); Dado Anonimizado | {disjoint} | No contexto considerado, um Dado não desempenha simultaneamente os papéis de Dado Pessoal e Dado Anonimizado; outros Dados são admitidos. | OntoPrivacy v2; LGPD; ISO/IEC 29100; decisão de modelagem | QC-P1; QC-P2; QC-P7 |
| GS03 | Identificabilidade | Identificabilidade Direta; Identificabilidade Indireta | {disjoint, complete} | Toda Identificabilidade é classificada como direta ou indireta, mas não como ambas na mesma instância. | OntoPrivacy v2; ABNT NBR ISO/IEC 29100:2020, item 2.5 | QC-P2 |
| GS04 | Tratamento de Dados Pessoais (TDP) | Operação de TDP; Conjunto de Operações de TDP | {disjoint, complete} | Todo TDP é representado como uma operação individual ou como um conjunto articulado de operações. | OntoPrivacy v2; LGPD, art. 5º, X; ISO/IEC 29100, item 2.21 | QC-P4 |
| GS05 | Operação de TDP | Alteração; Anonimização; Armazenamento; Coleta; Consulta; Disponibilização; Divulgação; Exclusão; Pseudonimização; Recuperação | {overlapping, incomplete} | Os tipos de operação podem coexistir no contexto de uma interação/tratamento e não esgotam todas as operações possíveis. | OntoPrivacy v2; LGPD, art. 5º, X; ISO/IEC 29100, item 2.21 | QC-P4; QC-P7 |
| GS06 | Agente de Tratamento | Controlador; Operador | {complete} | Todo Agente de Tratamento desempenha o papel de Controlador, Operador ou ambos em contextos admitidos pelo modelo. | OntoPrivacy v2; LGPD, art. 5º, IX; ISO/IEC 29100 | QC-P3; QC-P4 |
| GS07 | DP Sensível | DP Biométrico; DP Etnia; DP Político; DP Religião; DP Saúde | {overlapping, incomplete} | Um Dado Pessoal Sensível pode enquadrar-se em mais de uma categoria, e a taxonomia representada é deliberadamente parcial. | OntoPrivacy v2; LGPD, art. 5º, II; ISO/IEC 29100, item 2.24 | QC-P1 |

## Restrição própria

| ID | Elemento | Tipo | Regra | Fonte | QCs | Status |
| --- | --- | --- | --- | --- | --- | --- |
| REST01 | Dado Pseudonimizado | Restrição de classe | Todo Dado Pseudonimizado participa de pelo menos uma Identificabilidade Indireta. | OntoPrivacy v2; decisão de modelagem; apoio em LGPD, art. 13, §4º; ISO/IEC 29100, item 2.22 | QC-P2; QC-P7 | Registrada no ASTA; não exibida no PNG por decisão de apresentação. |

## Atributo

| ID | Proprietário | Atributo | Tipo | Multiplicidade | Definição | Fonte | QCs | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ATT01 | Finalidade | descrição | string | 1 | Expressão textual obrigatória e suficientemente individualizada do propósito para o qual o TDP é realizado. | OntoPrivacy v2; LGPD, art. 6º, I | QC-P5; QC-P6 | Registrado no ASTA; não exibido no PNG por decisão de apresentação. |

## Questões provisórias utilizadas apenas para indexação

| Código | Tema |
| --- | --- |
| QC-P1 | Dados e coleções |
| QC-P2 | Titular e identificabilidade |
| QC-P3 | Participantes e papéis |
| QC-P4 | Estrutura e operações do tratamento |
| QC-P5 | Finalidade |
| QC-P6 | Consentimento |
| QC-P7 | Anonimização, pseudonimização e resultados |

## Revisão terminológica

| Item | Status | Decisão |
| --- | --- | --- |
| Dado Pessoal (DP) | Canônico no ASTA | Manter o rótulo; “Dado Pessoal” e “DP” são sinônimos/abreviações de uso textual. |
| Tratamento de Dados Pessoais (TDP) | Canônico no ASTA | Manter o rótulo; “TDP” é abreviação. |
| Exclusão | Canônico no ASTA | Manter “Exclusão”; registrar “Eliminação” como sinônimo normativo. |
| DP Sensível e subclasses | Canônico no ASTA | Manter rótulos do modelo; nomes extensos aparecem como sinônimos no catálogo. |
| rolemixin | Nome técnico no ASTA | Registrar exatamente <<rolemixin>> no catálogo; na redação acadêmica, explicar como roleMixin. |
| Finalidade.descrição | Atributo no ASTA | Documentar no catálogo, embora não apareça no PNG. |
| Restrição de Dado Pseudonimizado | Restrição no ASTA | Documentar no catálogo, embora não apareça no PNG. |
| IDs C01–C43 e R01–R21 | IDs documentais | Usados apenas para organização do Catálogo; não constituem identificadores semânticos estáveis nem alteram LIM-v2-06. |