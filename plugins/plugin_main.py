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
    global mainlist, class_names
    if os.path.exists('data'):
        with open(f'data/{List}', 'r') as file:
            mainlist = file.read()
        class_names = mainlist[mainlist.find('\n\n\n\n[') + 4:]
        mainlist = mainlist.replace(mainlist[mainlist.find('\n\n\n\n'):], '')
        mainlist = ast.literal_eval(mainlist)
        class_names = ast.literal_eval(class_names)
        print("List load sucsessfull")
    else:
        print("Error. Can't load data")

def changeList():
    global curList
    data_lists = os.listdir(data_folder)
    while True:
        print("Choose list:")
        print(data_lists)
        CMDI = input("Enter file name from list:> ")
        if CMDI in data_lists:
            loadList(CMDI)
            curList = CMDI
            break
        else:
            print("Incorrect input\n")
        if CMDI == "cancel" or CMDI == "stop" and first == 0:
            break

if not os.path.exists(data_folder):
    os.mkdir("data")
    with open('data/mainlist.lmdb', 'w') as file:
        file.write("[['hide commands'],\n['version -- version of program'],\n['1']]\n\n\n\n['name', 'content', 'value']")
    with open('data/firstStart.pkl', 'w') as file:
        pickle.dump("yes", file)

changeList()

first = 0

def cmdHelp():
    print("Commands:")
    print("list -- see all elements in list")
    print("elem [ELEMENT NAME] -- see full information of element")
    print("edit [ELEMENT] -- edit part of element (be cerful! when you edit part of element it data is be overwritten!)")
    print("mkel -- create element")
    print("save -- save changes")
    print("del [ELEMENT] -- delete element")
    print('mkcls -- create new class')
    print('classes -- see all classes in list')
    print('delcls [CLASS NAME] -- delete class, and all in-elements in him')
    print("lists -- see all lists")
    print("cl -- change list")
    print("mkli -- create new list")
    print("delli [LIST NAME] -- delete list")
    print("exit -- save changes and exit from program")
    print("credits -- see developmenters")

def cmdCredits():
    print("\nDeveloped by Miron")

def cmdVersion():
    print("\nList Manager, version 1.3.1.")

def cmdList():
    print(mainlist[0])

def cmdElem(CMDI):
    if CMDI in mainlist[0]:
        index = mainlist[0].index(CMDI)
        class_index = 0
        for elem in mainlist:
            print(f'{class_names[class_index]}: {elem[index]}')
            class_index += 1
    else:
        print("Element not found. Check it, typing list")

def cmdEdit(CMDI):
    if CMDI in mainlist[0]:
        elem_index = mainlist[0].index(CMDI)
        WE = input(f"What part edit? ({class_names}):> ")
        if WE.lower() == "name".lower():
            new_data = input("Enter new name:> ")
            mainlist[0][elem_index] = new_data
            print("Name edit succesful")
        elif WE.lower() in class_names:
            class_index = class_names.index(WE)
            new_data = input(f"Enter new {WE}:> ")
            mainlist[class_index][elem_index] = new_data
            print(f'{WE} edit succesful')
        elif WE.lower() == "cancel".lower() or WE.lower() == "stop".lower():
            return
        else:
            print("Incorrect input")
    else:
        print("Element not found. Check it, typing list")

def cmdMakelement():
    for i in range(len(class_names)):
        new_elem = input(f'Enter {class_names[i]}:> ')
        mainlist[i].append(new_elem)
    print('Element created')

def cmdDelete(CMDI):
    if CMDI in mainlist[0]:
        WE = input(f"Are you want to delete element {CMDI}? (yes, no):> ")
        if WE == "yes":
            if CMDI in mainlist[0]:
                elem_index = mainlist[0].index(CMDI)
                for class_index in range(len(mainlist)- 1):
                    mainlist[class_index].pop(elem_index)
                print("Element delete succesful")
        elif WE == "no":
            return
        else:
            print("Incorrect input")
    else:
        print("Element not found. Maybe, it was delete")

def saveData():
    with open(f'data/{curList}', 'w') as file:
        file.write(f"{mainlist}\n\n\n\n{class_names}")

def classes():
    print(class_names)

def makeClass():
    global class_names, mainlist
    new_class_name = input('Enter name of new class:> ')
    if not new_class_name in class_names:
        class_names.append(new_class_name)
        mainlist.append([])
        for _ in range(len(mainlist[0])):
            mainlist[class_names.index(new_class_name)].append('None')
        print('Class created succesful')
    elif new_class_name in class_names:
        print('Class with same name already exists. Choose other name.')
        return

def deleteClass(CMDI):
    if CMDI in class_names:
        DYW = input(f'Do you want to delete class {CMDI}? (yes, no):> ') # DYW -- Do You Want?
        if DYW.lower() == 'yes'.lower():
            class_index = class_names.index(CMDI)
            mainlist.pop(class_index)
            class_names.pop(class_index)
            print('Class was deleted')
        else:
            return
    else:
        print('This class does not exists.')

def currentList():
    print(curList)

def makeList():
    CMDI = input("Enter name of new list:> ")
    if CMDI == "cancel" or CMDI == "stop":
        return
    with open(f'{data_folder}/{CMDI}.lmdb', 'w') as file:
        file.write("[['hide commands'],\n['version -- version of program'],\n['1']]\n\n\n\n['name', 'content', 'value']")
    print("List created succesful")

def deleteList(List: str):
    CMDI = input(f"Are you want to delete list {List}? (yes, no):> ")
    if CMDI == "yes":
        os.remove(f'{data_folder}/{List}.lmdb')
        print("List was deleted")
    else:
        return
