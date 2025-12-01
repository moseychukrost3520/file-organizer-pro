import json
from organizer.scanner import scan_directory
from organizer.sorter import sort_files

with open("config/settings.json") as f:
    cfg = json.load(f)

files = scan_directory(cfg["target_directory"])
sort_files(files, cfg)

print("File organization complete!")
