import os
import pickle
import plugins.plugin_main

folder_path = 'data'
first_start_file = 'data/firstStart.pkl'

def loadfirstfile():
    try:
        with open(first_start_file, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return None

if os.path.exists(folder_path):
    if loadfirstfile() == 'yes':
        print("Welcome to List Manager!")
        print("See documentation in docs folder, or type help to see all commands.")
        os.remove(first_start_file)
else:
    print("Error. Not found necessary files. Please, check script plugins/plugin_main.py.")
    print("If you haven't this file, download it from GitHub. Here link: https://github.com/2012Miron/List-Manager")
    input("Press Enter to exit...")
    exit()

while True:
    CMDI = input("Enter command:> ")

    if CMDI == "exit":
        print("Goodbye! See you soon.")
        print("Closing program...")
        plugins.plugin_main.saveData()
        break
    elif CMDI == "help":
        plugins.plugin_main.cmdHelp()
    elif CMDI == "version":
        plugins.plugin_main.cmdVersion()
    elif CMDI == "credits":
        plugins.plugin_main.cmdCredits()
    elif CMDI == "list":
        plugins.plugin_main.cmdList()
    elif CMDI.startswith("elem"):
        plugins.plugin_main.cmdElem(CMDI[5:])
    elif CMDI.startswith("edit"):
        plugins.plugin_main.cmdEdit(CMDI[5:])
    elif CMDI == "mkel":
        plugins.plugin_main.cmdMakelement()
    elif CMDI[:4] == "del ":
        plugins.plugin_main.cmdDelete(CMDI[4:])
    elif CMDI == "save":
        plugins.plugin_main.saveData()
        print("data saved")
    elif CMDI == "classes":
        plugins.plugin_main.classes()
    elif CMDI == "mkcls":
        plugins.plugin_main.makeClass()
    elif CMDI.startswith("delcls"):
        plugins.plugin_main.deleteClass(CMDI[7:])
    elif CMDI == "cl":
        plugins.plugin_main.changeList()
    elif CMDI == "lists":
        print(os.listdir('data'))
    elif CMDI == "curlist":
        plugins.plugin_main.currentList()
    elif CMDI == "mkli":
        plugins.plugin_main.makeList()
    elif CMDI.startswith("delli"):
        plugins.plugin_main.deleteList(CMDI[6:])
    else:
        print("")
        print("unknown command. type help to see all commands")
