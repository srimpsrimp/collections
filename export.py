from __future__ import annotations

import json
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    list_dir = root / "list"
    out_path = root / "output.jsonl"

    paths = sorted(list_dir.glob("*.json"), key=lambda p: p.name.lower())
    if not paths:
        raise SystemExit(f"No .json files under {list_dir}")

    with out_path.open("w", encoding="utf-8") as out:
        for path in paths:
            data = json.loads(path.read_text(encoding="utf-8"))
            out.write(json.dumps(data, ensure_ascii=False, separators=(",", ":")))
            out.write("\n")

    print(f"Wrote {len(paths)} lines to {out_path}")


if __name__ == "__main__":
    main()
