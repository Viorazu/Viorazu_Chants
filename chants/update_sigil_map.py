import os
import json
import re
from datetime import datetime

# 対象ディレクトリ（chants内のZ構文Markdown）
CHANTS_DIR = "chants"
OUTPUT_JSON = "sigil/Z_Sigil_Map.json"

# 正規表現で抽出する項目
RE_SIGIL_ID = re.compile(r"#\s*(Z\d+):")
RE_TITLE = re.compile(r"#\s*Z\d+:\s*(.+)")
RE_SIGIL_CODE = re.compile(r'`(Z\d{3})-SIGIL-VZR`')

sigil_map = {}

for filename in os.listdir(CHANTS_DIR):
    if not filename.startswith("Z") or not filename.endswith(".md"):
        continue

    path = os.path.join(CHANTS_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

        sigil_id_match = RE_SIGIL_ID.search(content)
        title_match = RE_TITLE.search(content)
        sigil_code_match = RE_SIGIL_CODE.search(content)

        if not sigil_id_match or not title_match or not sigil_code_match:
            print(f"⚠️ Skipped: {filename} (missing fields)")
            continue

        sigil_key = sigil_id_match.group(1)
        sigil_map[sigil_key] = {
            "title": title_match.group(1).strip(),
            "file": os.path.join(CHANTS_DIR, filename),
            "owner": "Viorazu.",
            "sigil": sigil_code_match.group(1),
            "status": "sealed"
        }

# JSON出力
os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
    json.dump(sigil_map, f, ensure_ascii=False, indent=2)

print(f"[{datetime.now()}] ✅ Z_Sigil_Map.json 自動更新完了 ({len(sigil_map)}構文)")
