import os
import pickle

folder_path = 'data'
ifinfirst = 'data/firstStart.pkl'
infirst = ""

def saveData(folder_path, EN, EC, EV):
    folder_path = 'data/names.pkl'
    with open(folder_path, 'wb') as file:
        pickle.dump(EN, file)
    folder_path = 'data/content.pkl'
    with open(folder_path, 'wb') as file:
        pickle.dump(EC, file)
    folder_path = 'data/value.pkl'
    with open(folder_path, 'wb') as file:
        pickle.dump(EV, file)

if os.path.exists(folder_path):
    folder_path = 'data/names.pkl'
    with open(folder_path, 'rb') as file:
        EN = pickle.load(file)
    folder_path = 'data/content.pkl'
    with open(folder_path, 'rb') as file:
        EC = pickle.load(file)
    folder_path = 'data/value.pkl'
    with open(folder_path, 'rb') as file:
        EV = pickle.load(file)
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
    print("Error. Not found necessary files. Please, check script checker.py, and ackter.py in folder checker.")
    print("If you haven't this files, download it from GitHub. Here link: https://github.com/2012Miron/List-Manager")
    input("Press Enter to exit...")
    exit()

while True:
    CMDI = input("Enter command: ")

    if CMDI == "help":
        print("Commands:")
        print("list -- see all elements in list")
        print("elem [NAME OF ELEMENT] -- see full information of element")
        print("edit [ELEMENT] -- edit part of element (be cerful! when you edit part of element it data is be overwritten!)")
        print("mkel -- create element")
        print("save -- save changes")
        print("del [ELEMENT] -- delete element")
        print("exit -- save changes and exit from program")
        print("credits -- see developmenters")
    elif CMDI == "credits":
        print("")
        print("Developmenter: 2012 Miron")
        print("Testers: golubdok (no in GitHub)")
    elif CMDI == "version":
        print("")
        print("List Manager, version 1.1")
    elif CMDI == "list":
        print(EN)
    elif CMDI[0:4] == "elem":
        if CMDI[5:] in EN:
            start = EN.index(CMDI[5:])
            end = start + 1
            print(EN[start:end])
            print(EC[start:end])
            print("value: ", EV[start:end])
        else:
            print("Element not found. Check it, typing list")
    elif CMDI == "mkel":
        for count in range(1):
            NNel = input("Enter element name: ")
            if NNel == "exit" or NNel == "cancel":
                break
            NCel = input("Enter content of element: ")
            if NCel == "exit" or NCel == "cancel":
                break
            NVel = input("Enter element value: ")
            if NVel == "exit" or NVel == "cancel":
                break
            EN.append(NNel)
            EC.append(NCel)
            EV.append(NVel)
            print("Element created sucsesfull")
    elif CMDI[:4] == "edit":
        if CMDI[5:] in EN:
            start = EN.index(CMDI[5:])
            WE = input("What part edit? (name, content, value) ")
            if WE == "name":
                NewData = input("Enter new name: ")
                EN[start] = NewData
                print("Name edit sucsesfull")
            elif WE == "content":
                NewData = input("Enter new content: ")
                EC[start] = NewData
                print("Content edit sucsesfull")
            elif WE == "value":
                NewData = input("Enter new value: ")
                EV[start] = NewData
                print("Value changed sucsesfull")
            elif WE == "exit" or WE == "cancel":
                print("Canceled sucsesfull")
            else:
                print("Incorrect input")
        else:
            print("Element not found. Check it, typing list")
    elif CMDI[:3] == "del":
        WE = input(f"Are you want to delete element {CMDI[4:]}? (yes, no): ")
        if WE == "yes":
            if CMDI[4:] in EN:
                start = EN.index(CMDI[4:])
                EN.remove(CMDI[4:])
                EC.pop(start)
                EV.pop(start)
                print("Element delete sucsesfull")
            else:
                print("Element not found. Maybe, it was delete")
        elif WE == "no":
            print("")
        else:
            print("Incorrect input")
    elif CMDI == "save":
        saveData(folder_path, EN, EC, EV)
        print("Data saved.")
    elif CMDI == "exit":
        print("Goodbye! See you soon.")
        print("Closing program...")
        saveData(folder_path, EN, EC, EV)
        break
    else:
        print("")
        print("unknown command. type help to see all commands")
