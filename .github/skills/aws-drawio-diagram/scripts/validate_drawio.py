#!/usr/bin/env python3
"""Validate a .drawio file against the AWS diagram skill rules. Usage: validate_drawio.py FILE [--template]"""
import re, sys, pathlib, xml.etree.ElementTree as ET

CATALOG = pathlib.Path(__file__).resolve().parent.parent / "references" / "aws-shape-catalog.md"
ALLOWED = set(re.findall(r"mxgraph\.aws4\.([a-z0-9_]+)", CATALOG.read_text()))

def main(path, template=False):
    errs, warns = [], []
    root = ET.parse(path).getroot()
    if root.find(".//diagram/mxGraphModel") is None:
        errs.append("No uncompressed <diagram><mxGraphModel> found (save uncompressed: File > Properties > uncheck Compressed)")
    for d in root.iter("diagram"):
        cells = {c.get("id"): c for c in d.iter("mxCell")}
        ids = [c.get("id") for c in d.iter("mxCell")]
        for dup in {i for i in ids if ids.count(i) > 1}:
            errs.append(f"[{d.get('name')}] duplicate id '{dup}'")
        if "0" not in cells or "1" not in cells:
            errs.append(f"[{d.get('name')}] missing root cells 0/1")
        if "title-block" not in cells:
            warns.append(f"[{d.get('name')}] no title-block")
        for cid, c in cells.items():
            if cid in ("0", "1"): continue
            if c.get("parent") not in cells:
                errs.append(f"{cid}: parent '{c.get('parent')}' not found")
            style = c.get("style") or ""
            for name in re.findall(r"mxgraph\.aws4\.([a-z0-9_]+)", style):
                if name not in ALLOWED:
                    errs.append(f"{cid}: shape 'mxgraph.aws4.{name}' not in catalog")
            if c.get("edge") == "1":
                for k in ("source", "target"):
                    if c.get(k) not in cells:
                        errs.append(f"{cid}: {k} '{c.get(k)}' missing")
            if c.get("vertex") == "1" and "container=1" not in style and not (c.get("value") or "").strip():
                warns.append(f"{cid}: unlabeled shape")
            if not template and "{{" in (c.get("value") or ""):
                errs.append(f"{cid}: unfilled placeholder in '{c.get('value')}'")
            if re.search(r"\b\d{12}\b|arn:aws:", c.get("value") or ""):
                errs.append(f"{cid}: looks like an account id / ARN in label")
    for w in warns: print("WARN ", w)
    for e in errs: print("ERROR", e)
    print(f"{path}: {len(errs)} error(s), {len(warns)} warning(s)")
    return 1 if errs else 0

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args: sys.exit(__doc__)
    sys.exit(max(main(a, "--template" in sys.argv) for a in args))
