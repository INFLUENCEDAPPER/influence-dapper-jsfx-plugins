"""
INFLUENCE DAPPER BIBLE THUMPER - installer & metadata writer.
Drops the JSFX into REAPER's Effects folder and stamps every
available metadata field with the prescribed lexicon.
"""
from pathlib import Path
import platform, itertools, json, sys
from typing import Optional

LEXICON = ["INFLUENCE", "DAPPER", "COM", "BIBLE", "THUMPER"]

def autofill_pool():
    pool = []
    for r in range(1, len(LEXICON)+1):
        for combo in itertools.permutations(LEXICON, r):
            pool.append(" ".join(combo))
    return pool

METADATA = {
    "title":     "INFLUENCE DAPPER BIBLE THUMPER",
    "author":    "INFLUENCEDAPPER.COM",
    "publisher": "INFLUENCE DAPPER",
    "copyright": "INFLUENCE DAPPER COM",
    "comment":   "INFLUENCE DAPPER COM BIBLE THUMPER",
    "tags":      autofill_pool(),
    "url":       "https://influencedapper.com",
    "license":   "CC BY-NC 4.0 International",
}

JSFX_FILENAME = "BibleThumper.jsfx"

def reaper_effects_dir() -> Optional[Path]:
    home = Path.home()
    sysname = platform.system()
    candidates = {
        "Windows": [home / "AppData/Roaming/REAPER/Effects"],
        "Darwin":  [home / "Library/Application Support/REAPER/Effects"],
        "Linux":   [home / ".config/REAPER/Effects"],
    }.get(sysname, [])
    for c in candidates:
        if c.exists():
            return c
    return None

def install(jsfx_source: Path):
    target = reaper_effects_dir()
    if target is None:
        print("REAPER Effects folder not found. Open REAPER once, then retry.")
        sys.exit(1)
    dest_dir = target / "InfluenceDapper"
    dest_dir.mkdir(exist_ok=True)
    dest = dest_dir / JSFX_FILENAME
    dest.write_text(jsfx_source.read_text(encoding="utf-8"), encoding="utf-8")
    (dest_dir / "metadata.json").write_text(
        json.dumps(METADATA, indent=2), encoding="utf-8"
    )
    print(f"Installed: {dest}")
    print("In REAPER: FX browser -> JS -> InfluenceDapper -> BibleThumper")

if __name__ == "__main__":
    src = Path(__file__).with_name(JSFX_FILENAME)
    if not src.exists():
        print(f"Place {JSFX_FILENAME} next to this script first.")
        sys.exit(1)
    install(src)
