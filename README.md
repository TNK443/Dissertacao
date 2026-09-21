<div align="center">

# **ONTOPRIVACY**

## UMA ONTOLOGIA DE DOMÍNIO PARA O ENRIQUECIMENTO SEMÂNTICO DE ARTEFATOS DE ENGENHARIA DE SOFTWARE  

</div>

![OE1](https://img.shields.io/badge/%20OE1%20%20-OntoPrivacy-0f766e?style=flat-square) **→**
![OntoPrivacy](https://img.shields.io/badge/OntoPrivacy-v2-3f7f5f?style=flat-square)
![Modelo](https://img.shields.io/badge/Modelagem-UFO%20%7C%20OntoUML-6f42c1?style=flat-square)
![Método](https://img.shields.io/badge/M%C3%A9todo-SABiO-d97706?style=flat-square)

![OE2(a)](https://img.shields.io/badge/OE2(a)-Anotacao%20Semantica-0b5d7a?style=flat-square) **→**
![EstudoI](https://img.shields.io/badge/Estudo%20I-v1.0-0b5d7a?style=flat-square)
![PrivacyFinder](https://img.shields.io/badge/PrivacyFinder-v1.0-6f82c1?style=flat-square)
![OpenAPI](https://img.shields.io/badge/OpenAPI-3.x-6ba539?style=flat-square)
![API Pix](https://img.shields.io/badge/API%20Pix-2.6.1-59636e?style=flat-square)

![OE2(b)](https://img.shields.io/badge/OE2(b)-GERPD-d97706?style=flat-square) **→**
![EstudoII](https://img.shields.io/badge/Estudo%20II-v1.0-2ea043?style=flat-square)
![GERPD](https://img.shields.io/badge/GERPD-v1.0-1f6feb?style=flat-square)

> **Título do Trabalho:** OntoPrivacy: uma Ontologia de Domínio para o enriquecimento semântico de artefatos de Engenharia de Software.  
> **Autor:** Dornelio Mori Junior  
> **Orientador:** Prof. Dr. Fabiano Borges Ruy  
> **Instituição:** Instituto Federal do Espírito Santo (IFES) - CAMPUS SERRA  
> **Programa:** Programa de Pós-Graduação em Computação Aplicada (PPCOMP) - Mestrado Profissional em Computação Aplicada  
> **Linha de Pesquisa:** Inteligência Artificial  
> **Ano:** 2026

---

## 📌 Sobre este repositório

Este repositório reúne todo o material suplementar, artefatos técnicos, dados, códigos e documentação complementar desenvolvidos e utilizados na elaboração da dissertação de mestrado descrita acima

Repositório de apoio aos artefatos, materiais de aplicação e evidências produzidos no desenvolvimento da dissertação de mestrado no IFES, situada na interseção entre **Ontologias**, **Privacidade de Dados**, **LGPD** e **Engenharia de Software**.

O objetivo deste repositório é promover a **transparência, reprodutibilidade e continuidade** da pesquisa acadêmica realizada.

> [!IMPORTANT]
> Este repositório documenta artefatos acadêmicos e aplicações demonstrativas. Nenhum material aqui deve ser interpretado como certificação de conformidade com a LGPD ou como substituto de avaliação jurídica, técnica, organizacional ou de segurança.

---

## 🧭 Visão geral da pesquisa e política de versões

```mermaid
---
config:
    theme: redux-color
    look: neo
---
flowchart LR
    %% Definição de estilos (ClassDef)
    %% Ontologia: Tons de Verde
    classDef ontologia fill:#C8E6C9,stroke:#2E7D32,stroke-width:2px,color:#1A1A1A;
    classDef ontologiav1 fill:#E8F5E9,stroke:#4CAF50,stroke-width:2px,stroke-dasharray: 5 5,color:#1A1A1A;
    classDef ontologiav2 fill:#C8E6C9,stroke:#2E7D32,stroke-width:2px,color:#1A1A1A;
    
    %% Propostas: Tons de Azul (Tecnologia/Engenharia)
    classDef proposta fill:#BBDEFB,stroke:#1565C0,stroke-width:2px,color:#1A1A1A;
    
    %% Estudos de Caso: Tons de Roxo (Validação/Aplicação)
    classDef estudo fill:#D1C4E9,stroke:#4527A0,stroke-width:2px,color:#1A1A1A;
    
    %% Documentação: Cor solicitada #cfd8dc (Cinza/Azulado)
    classDef doc fill:#cfd8dc,stroke:#546E7A,stroke-width:2px,color:#1A1A1A;

    %% Nós de Ontologia
    OP0("fa:fa-sitemap <b>ONTOPRIVACY</b>"):::ontologia

    %% Agrupamento das Ontologias
    subgraph F1["<b>FASE 1: Ontologia de Domínio</b>"]
        OP1("fa:fa-code-branch OntoPrivacy v1\n(Versão Inicial)"):::ontologiav1
        OP2("fa:fa-cube <b>OntoPrivacy v2</b>\n(Versão Final)"):::ontologiav2
    end
    %% Documentação
    DOC[/"fa:fa-book Catálogo, QCs, Rastreabilidade\ne Validação Conceitual"/]:::doc

    %% Agrupamento das Propostas Desenvolvidas
    subgraph F2["<b>FASE 2: Propostas</b>"]
        AS("fa:fa-network-wired Anotação Semântica\n(OpenAPI / Web Services)"):::proposta
        G("fa:fa-clipboard-list GERPD v1.0\n(Engenharia de Requisitos)"):::proposta
    end

    %% Agrupamento dos Estudos de Caso
    subgraph F3["<b>FASE 3: Estudos / Aplicações</b>"]
        E1{{"fa:fa-qrcode Estudo I: API Pix"}}:::estudo
        E2{{"fa:fa-robot Estudo II: Tibico + ChatGPT"}}:::estudo
    end

    %% CONEXÕES COM RÓTULOS
    OP0 -->|Utilizada na| AS
    OP0 -->|Integrada ao| G
    

    AS -->|Validada no| E1
    G -->|Validado no| E2
    
    OP1 -->|Evolução\nConceitual| OP2
    OP2 -->|Resulta em| DOC
    OP0 <--> F1

    %% Estilização visual dos Agrupamentos (Subgraphs)
    %% rx:10,ry:10 arredondam os cantos da caixa principal
    %% F1 - Fundo verde super claro, borda arredondada verde média
    style F1 fill:#F1F8E9,stroke:#81C784,stroke-width:3px,color:#1A1A1A,stroke-dasharray: 5 5,rx:10,ry:10
    %% F2 - Fundo azul super claro, borda arredondada azul média
    style F2 fill:#E3F2FD,stroke:#64B5F6,stroke-width:3px,color:#1A1A1A,stroke-dasharray: 5 5,rx:10,ry:10
    %% F3 - Fundo roxo super claro, borda arredondada roxa média
    style F3 fill:#F3E5F5,stroke:#BA68C8,stroke-width:3px,color:#1A1A1A,stroke-dasharray: 5 5,rx:10,ry:10
```

| 🧩 Artefato | Papel na Dissertação | Base Ontológica | Aplicação | 📂 Diretório |
| :---: | :--- | :---: | :--- | :--- |
| <small>**OntoPrivacy**</small> | <small>Seção 3.1 / Ontologia de Referência de Domínio (OE01)</small> | <small>Versão Conceitual</small> | <small>- Anotação Semântica<br>- GERPD</small> | [`/ONTOPRIVACY`](./ONTOPRIVACY/) |
| <small>**Anotação Semântica**</small> | <small>Seção 3.2 / OE02(a)</small> | <small>OntoPrivacy</small> | <small>Estudo I: API Pix (OE03)</small> | [<small>`/ANOTACAO_SEMANTICA`</small>](./ANOTACAO_SEMANTICA/) |
| <small>**GERPD v1.0**</small> | <small>Seção 3.3 / OE02(b)</small> | <small>OntoPrivacy</small> | <small>Estudo II: Tibico + ChatGPT (OE04)</small> | [`/GERPD`](./GERPD/) |

> [!NOTE]
> Na dissertação, a versão final congelada é denominada **OntoPrivacy v2**.
> O trabalho tem como objetivo geral desenvolver uma **Ontologia de Referência de Domínio** de privacidade de dados e utilizá-la como fundamentação no **enriquecimento semântico de artefatos de Engenharia de Software**. A pesquisa investiga duas formas complementares de aplicação:
>
> 1. anotação semântica de descrições **Web Services / REST / OpenAPI**;
> 2. apoio à **Engenharia de Requisitos de Privacidade de Dados** por meio do GERPD.

---

## 📂 Estrutura do repositório

```text
/Dissertacao/
├── README.md
├── .gitignore
├── ONTOPRIVACY/
│   ├── README.md
│   ├── ONTOPRIVACY.md
│   ├── VERSIONAMENTO.md
│   ├── CHANGELOG.md
│   ├── 01_MODELO/
│   ├── 02_METODOLOGIA/
│   ├── 03_CATALOGO/
│   ├── 04_VALIDACAO/
│   ├── 05_RASTREABILIDADE/
│   ├── 06_HISTORICO/
│   └── 07_REFERENCIAS/
├── ANOTACAO_SEMANTICA/
│   ├── README.md
│   ├── PrivacyFinder/
│   └── EstudoI/
└── GERPD/
    ├── README.md
    ├── 01_Documento_Oficial/
    ├── 02_Templates/
    ├── 03_Figuras/
    └── EstudoII/
```

### [`ONTOPRIVACY/`](./ONTOPRIVACY/)

Reúne a **versão conceitual final da Ontologia de Domínio**, o diagrama, a documentação metodológica, o Catálogo OntoPrivacy, as Questões de Competência, os cenários de validação e as matrizes de rastreabilidade.

### [`ANOTACAO_SEMANTICA/`](./ANOTACAO_SEMANTICA/)

Reúne a abordagem de anotação semântica apresentada na Seção 3.2, a OntoPrivacy v1 utilizada nesse eixo, as extensões OpenAPI, o Privacy Finder e o pacote reprodutível do Estudo I sobre a API Pix.

### [`GERPD/`](./GERPD/)

Reúne o GERPD v1.0, seus templates e figuras, bem como o pacote completo do Estudo II. O guia e o estudo preservam o vocabulário da OntoPrivacy v1 utilizado durante sua execução.

---

## 🧠 OntoPrivacy em síntese

A **OntoPrivacy** é uma ontologia de referência de domínio, em nível conceitual, fundamentada principalmente na **LGPD** e na **ABNT NBR ISO/IEC 29100:2020**, desenvolvida com apoio do **SABiO**, fundamentada em **UFO** e representada em **OntoUML**.

Sua arquitetura é organizada por três entidades relacionais centrais:

- **Identificabilidade:** relaciona `Dados Pessoais` ao `Titular de DP` e distingue identificação direta e indireta;
- **Tratamento de Dados Pessoais:** relaciona dados, participantes, operações e `Finalidade`'s;
- **Consentimento:** relaciona `Titular de DP`, `Controlador`, `TDP` e `Finalidade`'s determinadas.

A documentação pública inclui **43 conceitos**, **21 relações**, **7 conjuntos de generalização**, **7 Questões de Competência** e **14 cenários de validação conceitual**.

➡️ Comece em [`ONTOPRIVACY/README.md`](./ONTOPRIVACY/README.md).

---

## 🧩 Princípios de organização

1. **Separação entre artefato conceitual e aplicações:** a OntoPrivacy final possui diretório próprio; os estudos permanecem em seus eixos históricos.
2. **Preservação de versões:** OntoPrivacy v1 e v2 não são tratadas como intercambiáveis.
3. **Rastreabilidade:** conceitos, relações, fontes, QCs e cenários são documentados em arquivos próprios.
4. **Não extrapolação:** ausência de evidência em um artefato não é interpretada automaticamente como ausência de tratamento, papel, Consentimento ou Finalidade.
5. **Preservação do corpus:** entradas originais, resultados anotados, respostas brutas e revisões humanas permanecem separados.
6. **Reprodutibilidade:** os pacotes incluem os artefatos necessários para inspeção e repetição das verificações documentadas.
7. **Limites explícitos:** a OntoPrivacy não determina Base Legal, licitude ou conformidade jurídica.

---

## 🔎 Como navegar

1. Para compreender a ontologia final, consulte [`ONTOPRIVACY/README.md`](./ONTOPRIVACY/README.md).
2. Para uma descrição acadêmica detalhada, leia [`ONTOPRIVACY/ONTOPRIVACY.md`](./ONTOPRIVACY/ONTOPRIVACY.md).
3. Para examinar o modelo, acesse [`ONTOPRIVACY/01_MODELO/`](./ONTOPRIVACY/01_MODELO/).
4. Para estudar SABiO, UFO e OntoUML, acesse [`ONTOPRIVACY/02_METODOLOGIA/`](./ONTOPRIVACY/02_METODOLOGIA/).
5. Para reproduzir o Estudo I, acesse [`ANOTACAO_SEMANTICA/EstudoI/`](./ANOTACAO_SEMANTICA/EstudoI/).
6. Para examinar o Estudo II, acesse [`GERPD/EstudoII/`](./GERPD/EstudoII/).

---

## 📚 Publicação relacionada à OntoPrivacy v1

MORI JUNIOR, D.; NARDI, J. C.; RUY, F. B.; TEIXEIRA, G. F. **Apoio na adoção da Lei Geral de Proteção de Dados Pessoais por meio de anotações semânticas em descrições de serviços Web**. *Em Questão*, v. 31, e-139608, 2025. DOI: `10.1590/1808-5245.31.139608`.

---

## 🔗 Repositórios e fontes de referência

- Repositório principal: [TNK443/Dissertacao](https://github.com/TNK443/Dissertacao)
- Repositório histórico do Privacy Finder: [TNK443/Streamit](https://github.com/TNK443/Streamit)
- Especificação de referência da API Pix: [bacen/pix-api](https://github.com/bacen/pix-api)
- Documentação da linguagem OntoUML: [OntoUML Specification](https://ontouml.readthedocs.io/)

---

<div align="center">

**OntoPrivacy: uma Ontologia de Domínio para enriquecimento semântico de artefatos de Engenharia de Software**  
OntoPrivacy · Anotação Semântica · GERP

*`Material complementar de pesquisa acadêmica | versão 1.0, agosto de 2026.`*  

<small>*Dissertação apresentada ao Programa de Pós-Graduação em Computação Aplicada (PPCOMP)*</small>  
<small>*Instituto Federal do Espírito Santo (IFES), Campus Serra*</small>

</div>
