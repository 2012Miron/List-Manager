import os
import pickle
from checker import check

# Set data
files = ['value.pkl', 'content.pkl', 'names.pkl']
folder_path = 'data'
firstStart_path = os.path.join(folder_path, 'firstStart.pkl')
firstStart = ""

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        firstStart = "yes"
        with open(firstStart_path, 'wb') as file:
            pickle.dump(firstStart, file)

def create_files(folder_path, EN, EV, EC):
    folder_path = os.path.join(folder_path, 'names.pkl')
    with open(folder_path, 'wb') as file:
        pickle.dump(EN, file)
    folder_path = 'data'
    folder_path = os.path.join(folder_path, 'content.pkl')
    with open(folder_path, 'wb') as file:
        pickle.dump(EC, file)
    folder_path = 'data'
    folder_path = os.path.join(folder_path, 'value.pkl')
    with open(folder_path, 'wb') as file:
        pickle.dump(EV, file)

status = check(folder_path, files)

if status == "No files/folder":
    EN = ["hide commands"]
    EC = ["version -- version of program"]
    EV = ["0"]
    create_folder(folder_path)
    create_files(folder_path, EN, EV, EC)
    print("No files/folder. Problem solved")

if status == "Ok":
    print("All files is Ok")
