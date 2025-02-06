import os
import pickle
import plugins
import plugins.plugin_main

folder_path = 'data/list1.lmdb'
ifinfirst = 'data/firstStart.pkl'
infirst = ""

if os.path.exists(folder_path):
    try:
        with open(ifinfirst, 'rb') as file:
            infirst = pickle.load(file)
        if infirst == "yes":
            print("Welcome to List Manager!")
            print("View documentation in folder docs, or type help.")
            print("")
            os.remove(ifinfirst)
    except FileNotFoundError:
        print("")
    print("Data load sucsesfull.")
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
    elif CMDI[:4] == "elem":
        plugins.plugin_main.cmdElem(CMDI[5:])
    elif CMDI[:4] == "edit":
        plugins.plugin_main.cmdEdit(CMDI[5:])
    elif CMDI == "mkel":
        plugins.plugin_main.cmdMakelement()
    elif CMDI[:3] == "del":
        plugins.plugin_main.cmdDelete(CMDI[4:])
    elif CMDI == "save":
        plugins.plugin_main.saveData()
        print("data saved")
    elif CMDI == "cl":
        plugins.plugin_main.changeList()
    elif CMDI == "lists":
        print(os.listdir('data'))
    elif CMDI == "curlist":
        plugins.plugin_main.currentList()
    elif CMDI == "mkli":
        plugins.plugin_main.makeList()
    elif CMDI[:5] == "delli":
        plugins.plugin_main.deleteList(CMDI[6:])
    else:
        print("")
        print("unknown command. type help to see all commands")
