import os

def get_file_info(path):
    stats = os.stat(path)
    return {
        "size": stats.st_size,
        "created": stats.st_ctime
    }
