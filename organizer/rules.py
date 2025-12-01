import os

def categorize_file(file, categories):
    ext = os.path.splitext(file)[1].lower()
    for group, exts in categories.items():
        if ext in exts:
            return group
    return "misc"

def size_group(size, limits):
    if size <= limits["small"]:
        return "small"
    if size <= limits["medium"]:
        return "medium"
    return "large"
