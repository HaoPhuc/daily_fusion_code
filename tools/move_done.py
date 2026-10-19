#!/usr/bin/env python3
"""Move checked exercises from exercises/ to done/ and fix every link to them.

Usage: python3 tools/move_done.py <folder-name-or-path> [...]

For each folder:
  1. git mv exercises/<f> done/<f>
  2. replace "exercises/<f>" with "done/<f>" in LOG.md, theory/*.md and every
     README/FEEDBACK/HINT in exercises/ and done/
  3. rebuild the PDFs of every exercise whose README or theory note mentions <f>,
     so links inside PDFs point to the new place
"""
import pathlib
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent


def text_files():
    files = [REPO / "LOG.md"] + sorted((REPO / "theory").glob("*.md"))
    for base in ("exercises", "done"):
        for name in ("README.md", "FEEDBACK.md", "HINT.md"):
            files += sorted((REPO / base).glob(f"*/{name}"))
    return [f for f in files if f.exists()]


def main(names):
    (REPO / "done").mkdir(exist_ok=True)
    moved = []
    for name in names:
        name = pathlib.Path(name).name
        src, dst = REPO / "exercises" / name, REPO / "done" / name
        if not src.is_dir():
            print(f"skip {name}: not in exercises/")
            continue
        subprocess.run(["git", "-C", str(REPO), "mv", str(src), str(dst)], check=True)
        moved.append(name)
        print(f"moved {name} -> done/")
    if not moved:
        return
    rebuild = set()
    for f in text_files():
        text = f.read_text(encoding="utf-8")
        new = text
        for name in moved:
            new = new.replace(f"exercises/{name}", f"done/{name}")
        if new != text:
            f.write_text(new, encoding="utf-8")
        for name in moved:
            if name in new and f.parent.name not in ("theory",) and f.name != "LOG.md":
                rebuild.add(f.parent)
            if f.parent.name == "theory" and name in new:
                stem = f.stem
                for base in ("exercises", "done"):
                    if (REPO / base / stem).is_dir():
                        rebuild.add(REPO / base / stem)
    rebuild = sorted(p for p in rebuild if p.name not in moved)
    if rebuild:
        subprocess.run([sys.executable, str(REPO / "tools" / "make_pdf.py"), *map(str, rebuild)], check=True)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])
