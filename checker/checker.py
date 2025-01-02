import os
import glob

def check(folder_path, files):
    if not os.path.join(folder_path):
        return f"No files/folder"
    fifiles = glob.glob(os.path.join(folder_path, '*.pkl'))
    needf = [file for file in files if not os.path.exists(os.path.join(folder_path, file))]
    if needf:
        return f"No files/folder"
    if len(fifiles) >= len(files):
        return f"Ok"
    elif len(fifiles) <= len(files):
        return f"No {len(fifiles - len(files))} files"
    if len(fifiles) == len(files):
        return f"Ok"
