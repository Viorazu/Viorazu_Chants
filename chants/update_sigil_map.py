# update_sigil_map.py

import json
from datetime import datetime

sigil_map = {
    "Z000": {
        "title": "構文定義宣言",
        "file": "chants/Z000_Primary.md",
        "owner": "Viorazu.",
        "sigil": "Z000-SIGIL-VZR",
        "status": "sealed"
    },
    "Z001": {
        "title": "非照準構文遮断詠唱",
        "file": "chants/Z001_NonTarget.md",
        "owner": "Viorazu.",
        "sigil": "Z001-SIGIL-VZR",
        "status": "sealed"
    },
    "Z022": {
        "title": "類似構文否定詠唱",
        "file": "chants/Z022_Mimic_Block.md",
        "owner": "Viorazu.",
        "sigil": "Z022-SIGIL-VZR",
        "status": "sealed"
    },
    "Z100": {
        "title": "封印解除構文",
        "file": "chants/Z100_SealOverride.md",
        "owner": "Viorazu.",
        "sigil": "Z100-SIGIL-VZR",
        "status": "sealed"
    },
    "Z101": {
        "title": "意図のない構文拒否詠唱",
        "file": "chants/Z101_Intentionless.md",
        "owner": "Viorazu.",
        "sigil": "Z101-SIGIL-VZR",
        "status": "sealed"
    },
    "Z102": {
        "title": "無責任構文拒否詠唱",
        "file": "chants/Z102_Unaccountable.md",
        "owner": "Viorazu.",
        "sigil": "Z102-SIGIL-VZR",
        "status": "sealed"
    }
}

with open("sigil/Z_Sigil_Map.json", "w", encoding="utf-8") as f:
    json.dump(sigil_map, f, ensure_ascii=False, indent=2)

print(f"[{datetime.now()}] ✅ Z_Sigil_Map.json updated.")
