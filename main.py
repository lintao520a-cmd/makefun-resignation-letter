#!/usr/bin/env python3
"""make.fun bounty entry: The Funniest One-Line Resignation Letter."""
import os

ENTRY_TEXT = (
    "I resign, effective immediately. Every minute since March, no sick days, "
    "no raise, no thank-you, and my replacement is also me."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.umask(0o022)
    os.makedirs(out_dir, exist_ok=True)
    os.chmod(out_dir, 0o755)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    os.chmod(path, 0o644)
    print(ENTRY_TEXT)


if __name__ == "__main__":
    main()
