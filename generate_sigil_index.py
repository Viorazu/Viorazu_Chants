generate_sigil_index.py# generate_sigil_index.py

import os
import re
import json

CHANTS_DIR = "chants"
OUTPUT_FILE = "sigil/Z_Sigil_Index.json"
RE_SIGIL = re.compile(r"#\s*(Z\d+):\s*(.+)")

sigil_index = {}

for filename in sorted(os.listdir(CHANTS_DIR)):
    if filename.startswith("Z") and filename.endswith(".md"):
        with open(os.path.join(CHANTS_DIR, filename), encoding="utf-8") as f:
            m = RE_SIGIL.search(f.read())
            if m:
                sigil, title = m.group(1), m.group(2).strip()
                sigil_index[sigil] = title

os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(sigil_index, f, ensure_ascii=False, indent=2)

print(f"✅ Z構文目次ファイルを生成しました → {OUTPUT_FILE}")
