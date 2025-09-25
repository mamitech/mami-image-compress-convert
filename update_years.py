#!/usr/bin/env python3
"""
Utility script to update year references in LICENSE and SECURITY.md to current year.
"""
import re
from datetime import datetime
from pathlib import Path

def update_file(path: Path):
    text = path.read_text(encoding="utf-8")
    now = datetime.now()
    # Update copyright year using a replacement function to avoid backreference issues
    def repl_copyright(m):
        return f"{m.group(1)}{now.year}"
    text = re.sub(r"(Copyright \(c\)\s*)\d{4}", repl_copyright, text)
    # Update last updated month and year
    def repl_last_updated(m):
        return f"{m.group(1)}{now.strftime('%B %Y')}"
    text = re.sub(r"(\*\*Last updated\*\*:\s*)[A-Za-z]+\s*\d{4}", repl_last_updated, text)
    path.write_text(text, encoding="utf-8")

def main():
    for filename in ("LICENSE", "README.md"):
        p = Path(__file__).parent / filename
        if p.exists():
            update_file(p)
            print(f"Updated {filename} to current year")
        else:
            print(f"File not found: {filename}")

if __name__ == "__main__":
    main()
