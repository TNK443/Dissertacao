# Limites de Escopo identificados

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