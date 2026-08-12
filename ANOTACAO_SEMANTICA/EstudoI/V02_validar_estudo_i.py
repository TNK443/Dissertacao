#!/usr/bin/env python3
"""Validação reprodutível do Estudo I.

Verifica parse YAML, estrutura OpenAPI, referências internas e contagens das
extensões semânticas. Não altera os arquivos analisados.
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

METHODS = {"get", "post", "put", "patch", "delete", "head", "options", "trace"}
TARGET_EXTS = {"x-refersTo", "x-operationType"}


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def operations(data):
    result=[]
    for path,item in (data.get("paths") or {}).items():
        if isinstance(item,dict):
            for method,obj in item.items():
                if method.lower() in METHODS and isinstance(obj,dict):
                    result.append((path,method.lower(),obj))
    return result


def walk(obj: Any):
    if isinstance(obj,dict):
        for k,v in obj.items():
            yield k,v
            yield from walk(v)
    elif isinstance(obj,list):
        for v in obj:
            yield from walk(v)


def collect_refs(data):
    return [v for k,v in walk(data) if k == "$ref"]


def resolve_internal(data, ref):
    if not (isinstance(ref,str) and ref.startswith("#/")):
        return True
    cur=data
    try:
        for part in ref[2:].split("/"):
            part=part.replace("~1","/").replace("~0","~")
            cur=cur[part]
        return True
    except Exception:
        return False


def strip_semantic(obj):
    if isinstance(obj,dict):
        return {k:strip_semantic(v) for k,v in obj.items() if k not in TARGET_EXTS}
    if isinstance(obj,list):
        return [strip_semantic(v) for v in obj]
    return obj


def normalize(obj):
    if isinstance(obj,dict): return {k:normalize(v) for k,v in obj.items()}
    if isinstance(obj,list): return [normalize(v) for v in obj]
    if isinstance(obj,str): return re.sub(r"\s+", " ", obj).strip()
    return obj


def extension_stats(data):
    counts=Counter()
    concepts=Counter()
    for k,v in walk(data):
        if k in TARGET_EXTS:
            counts[k]+=1
            values=v if isinstance(v,list) else [v]
            concepts.update(str(x) for x in values)
    return counts,concepts


def check(label, value, expected=None):
    ok = bool(value) if expected is None else value == expected
    expected_text = "" if expected is None else f" | esperado: {expected}"
    print(f"[{'OK' if ok else 'FALHA'}] {label}: {value}{expected_text}")
    return ok


def main():
    parser=argparse.ArgumentParser()
    here=Path(__file__).resolve().parent
    parser.add_argument("--original",type=Path,default=here/"C01_API_PIX_Release_2.6.1.yaml")
    parser.add_argument("--anotado",type=Path,default=here/"R01_API_PIX_Anotado.yaml")
    args=parser.parse_args()

    original=load_yaml(args.original)
    annotated=load_yaml(args.anotado)
    ok=[]

    print("VALIDAÇÃO TÉCNICA — ESTUDO I / API PIX")
    print("="*52)
    ok.append(check("OpenAPI original", original.get("openapi"), "3.0.0"))
    ok.append(check("Versão API original", original.get("info",{}).get("version"), "2.6.1"))
    ok.append(check("OpenAPI anotado", annotated.get("openapi"), "3.0.0"))
    ok.append(check("Versão API anotada", annotated.get("info",{}).get("version"), "2.6.1"))

    orig_ops=operations(original); ann_ops=operations(annotated)
    ok.append(check("Paths original", len(original.get("paths") or {}), 16))
    ok.append(check("Paths anotado", len(annotated.get("paths") or {}), 16))
    ok.append(check("Operações original", len(orig_ops), 27))
    ok.append(check("Operações anotado", len(ann_ops), 27))
    ok.append(check("Schemas original", len((original.get("components") or {}).get("schemas") or {}), 67))
    ok.append(check("Schemas anotado", len((annotated.get("components") or {}).get("schemas") or {}), 67))

    refs_o=collect_refs(original); refs_a=collect_refs(annotated)
    broken_o=[r for r in refs_o if not resolve_internal(original,r)]
    broken_a=[r for r in refs_a if not resolve_internal(annotated,r)]
    ok.append(check("Referências $ref original", len(refs_o), 373))
    ok.append(check("Referências $ref anotado", len(refs_a), 373))
    ok.append(check("Referências internas quebradas no original", len(broken_o), 0))
    ok.append(check("Referências internas quebradas no anotado", len(broken_a), 0))

    ext,concepts=extension_stats(annotated)
    ok.append(check("x-operationType", ext["x-operationType"], 19))
    ok.append(check("x-refersTo", ext["x-refersTo"], 10))
    ok.append(check("Total de propriedades semânticas", sum(ext.values()), 29))
    ok.append(check("Associações conceituais", sum(concepts.values()), 65))
    ok.append(check("Equivalência estrutural após retirada das anotações", normalize(strip_semantic(annotated)) == normalize(original), True))

    print("="*52)
    if all(ok):
        print("RESULTADO: APROVADO — todas as verificações esperadas foram satisfeitas.")
        return 0
    print("RESULTADO: REPROVADO — uma ou mais verificações não corresponderam ao esperado.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
