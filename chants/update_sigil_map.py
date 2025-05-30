import os
import json
import re

# ディレクトリとパス定義
CHANTS_DIR = "chants"
SIGIL_PATH = "sigil/Z_Sigil_Map.json"

# 固定値
DEFAULT_OWNER = "Viorazu."
DEFAULT_STATUS = "sealed"

def extract_metadata(filepath):
    """Markdownファイルから構文ID・タイトル・署名コードを抽出"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # タイトルとZ構文IDの抽出（例: # Z101: 意図のない構文拒否詠唱）
    z_code_match = re.search(r"# (Z\d+): (.+)", content)

    if not z_code_match:
        return None

    z_code = z_code_match.group(1)
    title = z_code_match.group(2).strip()

    # 署名コードの抽出（例: 署名コード：Z101-SIGIL-VZR）
    sigil_match = re.search(r"署名コード：\s*([^\n]+)", content)
    sigil = sigil_match.group(1).strip() if sigil_match else f"{z_code}-SIGIL-VZR"

    return {
        "z_code": z_code,
        "title": title,
        "file": filepath.replace("\\", "/"),
        "sigil": sigil
    }

def update_sigil_map():
    """chants/ 以下の .md ファイルをスキャンして JSON を生成"""
    chant_files = sorted(
        [os.path.join(CHANTS_DIR, f) for f in os.listdir(CHANTS_DIR) if f.endswith(".md")]
    )

    sigil_map = {}

    for filepath in chant_files:
        meta = extract_metadata(filepath)
        if meta:
            sigil_map[meta["z_code"]] = {
                "title": meta["title"],
                "file": meta["file"],
                "owner": DEFAULT_OWNER,
                "sigil": meta["sigil"],
                "status": DEFAULT_STATUS
            }

    os.makedirs(os.path.dirname(SIGIL_PATH), exist_ok=True)

    with open(SIGIL_PATH, "w", encoding="utf-8") as f:
        json.dump(sigil_map, f, ensure_ascii=False, indent=2)

    print(f"✅ Z_Sigil_Map.json updated with {len(sigil_map)} entries.")

if __name__ == "__main__":
    update_sigil_map()
