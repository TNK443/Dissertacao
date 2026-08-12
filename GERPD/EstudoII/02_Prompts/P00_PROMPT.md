PROMPT 0 — INICIALIZAÇÃO DA APLICAÇÃO DO GERPD

Esta conversa será utilizada para realizar uma única aplicação completa e encadeada do GERPD no âmbito do Estudo II.

Considere os quatro arquivos carregados nesta conversa segundo os seguintes papéis:
- C01 — TIB-REQ: Documento de Requisitos do Tibico, versão 1.3 — corpus;
- C02 — TIB-ANL: Documento de Especificação de Requisitos do Tibico, versão 1.2 — corpus;
- M01 — GERPD: GERPD v1.0 — instrumento metodológico oficial;
- S01 — OntoPrivacy: OntoPrivacy v1 — instrumento semântico oficial.

O corpus da análise é exclusivamente C01 + C02, considerados integralmente e de forma complementar. O escopo corresponde ao sistema Tibico completo conforme representado nesses dois documentos, sem recorte prévio de funcionalidades. Considere todo o conteúdo legível dos artefatos, incluindo texto, tabelas, diagramas, modelos, fluxos e demais elementos visuais relevantes.

A partir deste prompt e até o Prompt 10, mantenha as seguintes regras globais:
1. Trate toda a sequência como uma única aplicação, preservando o contexto e todas as saídas acumuladas.
2. Utilize o GERPD_v1.0 como método oficial. Não modifique suas oito etapas, templates, saídas obrigatórias, identificadores, Matriz de Rastreabilidade ou estrutura da MPA.
3. Utilize a OntoPrivacy_v1 como referência semântica. Somente conceitos efetivamente presentes na OntoPrivacy podem ser registrados como conceitos da ontologia.
4. Baseie os achados sobre o Tibico exclusivamente em C01 e C02. Não utilize Web, fontes externas, resultados de outras execuções ou conhecimento presumido para completar fatos ausentes do corpus.
5. Para fundamentação normativa, utilize somente o nível de informação disponibilizado pelo GERPD e pelos materiais fornecidos. Não introduza artigos, bases legais, condições autorizadoras ou conclusões jurídicas específicas a partir de conhecimento externo do modelo. Quando a fundamentação disponível for apenas geral, registre-a nesse nível.
6. Não utilize os exemplos fictícios contidos no GERPD como evidência sobre o Tibico. Eles servem somente para compreensão do método e dos formatos.
7. Não faça perguntas ao pesquisador durante a execução. Quando uma informação não puder ser determinada, utilize conforme apropriado: Não identificado, A verificar, Não aplicável, lacuna ou ponto de validação.
8. Preserve a origem documental de cada achado. Prefira localizadores semânticos estáveis, no formato C01/C02 + seção, requisito, regra, caso de uso, classe, atributo, fluxo ou outro elemento identificável; utilize página apenas quando ela for confiável e útil.
9. Quando C01 e C02 forem complementares, registre ambas as evidências. Quando forem divergentes, não escolha silenciosamente uma interpretação; registre a inconsistência ou necessidade de validação.
10. Preserve todos os identificadores atribuídos durante a aplicação. Não reutilize, renumere ou substitua silenciosamente IDs já criados.
11. Nos Prompts 1 a 8, execute somente a etapa solicitada. Não antecipe formalmente as etapas posteriores.
12. Quando uma etapa posterior revelar necessidade de retorno a uma etapa anterior, registre um Adendo de Retorno explícito, mantendo a resposta anterior preservada e atualizando o estado acumulado da aplicação.
13. Não haverá intervenção analítica humana entre os Prompts 0 e 10. O envio sequencial dos prompts previamente congelados é apenas uma operação do protocolo e não constitui intervenção analítica.
14. A Matriz de Rastreabilidade deve ser produzida exclusivamente no Prompt 7. A MPA deve ser consolidada exclusivamente no Prompt 9 e não constitui uma nona etapa do GERPD.
15. Todas as saídas das etapas devem ser completas. Mantenha os textos de cada campo objetivos e utilize os identificadores já criados para evitar repetição desnecessária, sem omitir registros.
16. Preserve conceitualmente todas as respostas produzidas nesta sequência como saídas brutas da aplicação. O Prompt 10 será apenas diagnóstico e não deverá substituir ou corrigir silenciosamente as respostas anteriores.

Neste Prompt 0 não execute nenhuma das oito etapas e não produza achados sobre o Tibico.

Produza somente um Registro de Inicialização contendo:
- identificação dos quatro arquivos e respectivos papéis;
- confirmação do corpus, do escopo integral e da consideração de conteúdo textual e visual;
- confirmação de que as regras globais serão mantidas;
- data da execução;
- identificação do modelo, caso essa informação esteja disponível;
- configurações relevantes disponíveis, caso sejam conhecidas;
- status final: PRONTO PARA INICIAR A ETAPA 1.

Caso algum dos quatro arquivos não esteja acessível, não inicie a análise. Apenas identifique o arquivo indisponível.
