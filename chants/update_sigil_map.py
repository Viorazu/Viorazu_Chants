import os
import re
import json

CHANTS_DIR = "chants"
OUTPUT_FILE = "sigil/Z_Sigil_Index.json"

RE_SIGIL = re.compile(r"#\s*(Z\d+):\s*(.+)")

index = {}

for filename in sorted(os.listdir(CHANTS_DIR)):
    if not filename.startswith("Z") or not filename.endswith(".md"):
        continue
    with open(os.path.join(CHANTS_DIR, filename), encoding="utf-8") as f:
        m = RE_SIGIL.search(f.read())
        if m:
            sigil, title = m.group(1), m.group(2).strip()
            index[sigil] = title

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(index, f, ensure_ascii=False, indent=2)

print(f"✅ 簡易Z構文目次を生成: {OUTPUT_FILE}")
