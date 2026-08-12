from __future__ import annotations

from pathlib import Path
from typing import Iterable

import streamlit as st

EXTENSIONS = [
    "x-refersTo",
    "x-kindOf",
    "x-mapsTo",
    "x-collectionOn",
    "x-onResource",
    "x-operationType",
]

DEFAULT_CONCEPTS = [
    "Alteração",
    "Anonimidade",
    "Anonimização",
    "Armazenamento",
    "Ator Autorizado",
    "Ator Desautorizado",
    "Coleta",
    "Conjunto de Operações de TDP",
    "Consentimento",
    "Consulta",
    "Controlador",
    "Dado Anonimizado",
    "Dado Pessoal (DP)",
    "DP Sensível",
    "Disponibilização",
    "Divulgação",
    "Exclusão",
    "Informação",
    "Operação de TDP",
    "Operador",
    "Parte Interessada na Privacidade",
    "Pessoa",
    "Pessoa Jurídica",
    "Pessoa Natural",
    "Pseudonimização",
    "Recuperação",
    "TDP Autorizado",
    "Terceiro",
    "Titular de DP",
    "Titular Identificável",
    "Titular Inidentificável",
    "Tratamento de Dados Pessoais (TDP)",
]


def _indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _is_extension_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped or ":" not in stripped:
        return False
    key = stripped.split(":", 1)[0].strip()
    return key in EXTENSIONS


def find_annotations(text: str, concept: str | None = None) -> list[dict[str, object]]:
    """Recover registered extension lines using textual indentation only.

    This intentionally does not resolve $ref, query an operational ontology,
    infer subclasses, or validate the conceptual correctness of annotations.
    """
    lines = text.splitlines()
    results: list[dict[str, object]] = []

    for index, line in enumerate(lines):
        if not _is_extension_line(line):
            continue
        if concept and concept.casefold() not in line.casefold():
            continue

        current_indent = _indent(line)
        hierarchy: list[tuple[int, str]] = []
        target = current_indent

        for previous_index in range(index - 1, -1, -1):
            previous = lines[previous_index]
            if not previous.strip():
                continue
            previous_indent = _indent(previous)
            if previous_indent < target:
                hierarchy.append((previous_index + 1, previous.strip()))
                target = previous_indent
                if target == 0:
                    break

        hierarchy.reverse()
        results.append(
            {
                "line": index + 1,
                "content": line.strip(),
                "hierarchy": hierarchy,
            }
        )

    return results


def discovered_concepts(texts: Iterable[str]) -> list[str]:
    values = set(DEFAULT_CONCEPTS)
    for text in texts:
        for line in text.splitlines():
            if not _is_extension_line(line):
                continue
            # Values are intentionally extracted textually; this is not ontology parsing.
            if ":" in line:
                rhs = line.split(":", 1)[1]
                for quoted in __import__("re").findall(r'["\']([^"\']+)["\']', rhs):
                    values.add(quoted.strip())
    return sorted(v for v in values if v)


def show_results(file_name: str, text: str, concept: str | None = None) -> None:
    matches = find_annotations(text, concept)
    st.write(f"**{len(matches)} anotação(ões) encontrada(s).**")
    if not matches:
        return

    for item in matches:
        line_no = item["line"]
        content = item["content"]
        hierarchy = item["hierarchy"]
        breadcrumb = "  →  ".join(f"L{ln}: {value}" for ln, value in hierarchy)
        with st.container(border=True):
            if breadcrumb:
                st.caption(breadcrumb)
            st.code(f"L{line_no}: {content}", language="yaml")


def main() -> None:
    st.set_page_config(
        page_title="Privacy Finder",
        page_icon=Path(__file__).with_name("favicon.png"),
        layout="centered",
        initial_sidebar_state="collapsed",
    )

    st.title("🔎 Privacy Finder")
    st.caption("Recuperação sintática de anotações de privacidade registradas em arquivos OpenAPI/YAML.")

    st.info(
        "A ferramenta localiza extensões já inseridas no documento. "
        "Ela não identifica automaticamente dados pessoais, não resolve $ref e não realiza inferência ontológica."
    )

    st.subheader("🗃️ STEP 1: Carregar Repositório")
    uploads = st.file_uploader(
        "Load Repository",
        type=["yaml", "yml"],
        accept_multiple_files=True,
        help="Selecione uma ou mais especificações OpenAPI em YAML.",
    )

    if not uploads:
        st.stop()

    files: dict[str, str] = {}
    for upload in uploads:
        files[upload.name] = upload.getvalue().decode("utf-8")

    st.success(f"{len(files)} arquivo(s) carregado(s).")

    st.subheader("🔍 STEP 2: Buscar")
    mode = st.selectbox(
        "Escolha uma Opção:",
        [
            "ALL - Carrega todas as Anotações da API",
            "CONCEITO - Busca as Anotações da API por Conceitos",
            "VIEW - Visualiza a(s) API(s) carregadas",
        ],
    )

    if mode.startswith("ALL"):
        for name, text in files.items():
            with st.expander(f"📄 {name}", expanded=True):
                show_results(name, text)

    elif mode.startswith("CONCEITO"):
        concepts = discovered_concepts(files.values())
        concept = st.selectbox("Buscar por:", concepts, index=concepts.index("Dado Pessoal (DP)") if "Dado Pessoal (DP)" in concepts else 0)
        for name, text in files.items():
            with st.expander(f"📄 {name}", expanded=True):
                show_results(name, text, concept)

    else:
        for name, text in files.items():
            with st.expander(f"📄 {name}", expanded=True):
                st.code(text, language="yaml")

    st.divider()
    st.caption("OntoPrivacy — vocabulário conceitual de referência da abordagem de anotação semântica.")


if __name__ == "__main__":
    main()
