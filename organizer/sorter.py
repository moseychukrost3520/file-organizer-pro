import os
import shutil
from datetime import datetime
from organizer.rules import categorize_file, size_group
from utils.file_helpers import get_file_info

def sort_files(files, cfg):
    out = cfg["output_directory"]
    cats = cfg["categories"]
    limits = cfg["size_limits"]

    for f in files:
        info = get_file_info(f)
        cat = categorize_file(f, cats)
        size_cat = size_group(info["size"], limits)
        date_cat = datetime.fromtimestamp(info["created"]).strftime("%Y-%m-%d")

        folder = os.path.join(out, cat, size_cat, date_cat)
        os.makedirs(folder, exist_ok=True)

        shutil.copy(f, folder)
