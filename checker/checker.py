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

folder_path = 'data'
files = ['value.pkl', 'content.pkl', 'names.pkl']
result_path = os.path.join('checker', 'result.txt')
# Set data

result = check(folder_path, files)

with open(result_path, 'w') as result_file:
    result_file.write(result) # Write result to txt file
print("Checking was complete.")
