import os

def scan_directory(path):
    return [os.path.join(path, f) for f in os.listdir(path)]
