import os
import ast
import pickle

curList = ""

first = 1
current_dir = os.path.abspath(__file__)
current_dir = os.path.dirname(current_dir)
data_folder = os.path.dirname(current_dir)
data_folder = os.path.join(data_folder, 'data')

def loadList(List: str):
    global EN, EC, EV
    if os.path.exists('data'):
        with open(f'data/{List}', 'r') as file:
            list1 = file.read()
        names = list1[list1.find("["):list1.find("]") + 1]
        content = list1[list1.find("[", list1.find("]")):list1.find("]", list1.find("]") + 1) + 1]
        value = list1[list1.find("[", list1.find("]", list1.find("]"))):list1.find("]", list1.find("]", list1.find("]") + 1)) + 1]
        EN = ast.literal_eval(names)
        EC = ast.literal_eval(content)
        EV = ast.literal_eval(value)
        print("List load sucsessfull")
    else:
        print("Error. Can't load data")

def changeList():
    global curList
    while True:
        print("Choose list:")
        print(os.listdir(data_folder))
        CMDI = input("Enter file name from list:> ")
        if CMDI in os.listdir(data_folder):
            loadList(CMDI)
            curList = CMDI
            break
        else:
            print("Incorrect input\n")
        if CMDI == "cancel" or CMDI == "stop" and first == 0:
            break

if not os.path.exists(data_folder):
    os.mkdir("data")
    with open('data/list1.lmdb', 'w') as file:
        file.write("class names 0: ['hide commands']\nclass content 1: ['version -- version of program']\nclass value 2: ['1']")
    with open('data/firstStart.pkl', 'w') as file:
        pickle.dump("yes", file)

changeList()

first = 0

def cmdHelp():
    print("Commands:")
    print("list -- see all elements in list")
    print("elem [NAME OF ELEMENT] -- see full information of element")
    print("edit [ELEMENT] -- edit part of element (be cerful! when you edit part of element it data is be overwritten!)")
    print("mkel -- create element")
    print("save -- save changes")
    print("del [ELEMENT] -- delete element")
    print("lists -- see all lists")
    print("cl -- change list")
    print("mkli -- create new list")
    print("delli [LIST NAME] -- delete list")
    print("exit -- save changes and exit from program")
    print("credits -- see developmenters")

def cmdCredits():
    print("")
    print("Developmenter: 2012 Miron")
    print("Testers: golubdok (no in GitHub)")

def cmdVersion():
    print("")
    print("List Manager, version 1.2.")

def cmdList():
    print(EN)

def cmdElem(CMDI):
    if CMDI in EN:
        start = EN.index(CMDI)
        end = start + 1
        print(EN[start:end])
        print(EC[start:end])
        print("value: ", EV[start:end])
    else:
        print("Element not found. Check it, typing list")

def cmdEdit(CMDI):
    if CMDI in EN:
        start = EN.index(CMDI)
        WE = input("What part edit? (name, content, value):> ")
        if WE == "name":
            NewData = input("Enter new name:> ")
            EN[start] = NewData
            print("Name edit sucsesfull")
        elif WE == "content":
            NewData = input("Enter new content:> ")
            EC[start] = NewData
            print("Content edit sucsesfull")
        elif WE == "value":
            NewData = input("Enter new value:> ")
            EV[start] = NewData
            print("Value changed sucsesfull")
        elif WE == "exit":
            return
        else:
            print("Incorrect input")
    else:
        print("Element not found. Check it, typing list")

def cmdMakelement():
    NNel = input("Enter element name:> ")
    if NNel == "exit" or NNel == "cancel":
        return
    NCel = input("Enter content of element:> ")
    if NCel == "exit" or NCel == "cancel":
        return
    NVel = input("Enter element value:> ")
    if NVel == "exit" or NVel == "cancel":
        return
    EN.append(NNel)
    EC.append(NCel)
    EV.append(NVel)
    print("Element created sucsesfull")

def cmdDelete(CMDI):
    WE = input(f"Are you want to delete element {CMDI}? (yes, no):> ")
    if WE == "yes":
        if CMDI in EN:
            start = EN.index(CMDI)
            EN.remove(CMDI)
            EC.pop(start)
            EV.pop(start)
            print("Element delete sucsesfull")
        else:
            print("Element not found. Maybe, it was delete")
    elif WE == "no":
        print("")
    else:
        print("Incorrect input")

def saveData():
    with open(f'data/{curList}', 'w') as file:
        file.write(f"class names 0: {EN}\nclass content 1: {EC}\nclass value 2: {EV}")

def currentList():
    global curList
    print(curList)

def makeList():
    CMDI = input("Enter name of new list:> ")
    if CMDI == "cancel" or CMDI == "stop":
        return
    with open(f'{data_folder}/{CMDI}.lmdb', 'w') as file:
        file.write("['hide commands']\n['version -- version of program']\n['1']")
    print("List created sucsessfull")

def deleteList(List: str):
    CMDI = input(f"Are you want to delete list {List}? (yes, no):>")
    if CMDI == "yes":
        os.remove(f'{data_folder}/{List}.lmdb')
        print("List was deleted")
    else:
        return
