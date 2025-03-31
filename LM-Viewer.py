import os, ast, webbrowser
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

def openDocs():
    webbrowser.open('https://github.com/2012Miron/List-Manager/tree/main/docs')

def about():
    messagebox.showinfo('List Manager Viewer', 'List Manager Viewer 1.0.\nList Manager 1.3.1.\nGitHub: https://github.com/2012Miron/List-Manager')

def mainWindow(columns: list, mainlist: list, elements: int):
    root = tk.Tk()
    root.title('List Manager Viewer')

    menubar = tk.Menu(root)
    root.config(menu=menubar)

    file_menu = tk.Menu(menubar)
    file_menu.add_command(label='Open', command=loadList)
    file_menu.add_command(label='Create New', command=createList)
    menubar.add_cascade(label='File', menu=file_menu)

    help_menu = tk.Menu(menubar)
    help_menu.add_command(label='Documentation', command=openDocs)
    help_menu.add_command(label='About', command=about)
    menubar.add_cascade(label='Help', menu=help_menu)

    content_tree = ttk.Treeview(root, columns=[i for i in range(elements)], show='headings')
    
    for col in [i for i in range(elements)]:
        if col == 'Classes':
            content_tree.heading(col, text=str(col))
        else:
            content_tree.heading(col, text='#' + str(col))
    
    for row in mainlist:
        content_tree.insert('', tk.END, values=row)
    
    for cls in columns:
        content_tree.insert('', tk.END, values=cls)
    
    content_tree.pack(expand=True, fill="both")

    root.mainloop()

def loadList():
    global mainlist, class_names, elements, filepath
    filepath = filedialog.askopenfilename(
        title='Chose database:',
        filetypes=(('Database files', '*.db'), ('List Manager standart files', '*.lmdb'), ('All files', '*.*'))
    )
    if filepath and os.path.exists(filepath):
        with open(filepath, 'r') as file:
            mainlist = file.read()
        class_names = mainlist[mainlist.find('\n\n\n\n[') + 4:]
        mainlist = mainlist.replace(mainlist[mainlist.find('\n\n\n\n'):], '')
        mainlist = ast.literal_eval(mainlist)
        class_names = ast.literal_eval(class_names)
        elements = len(class_names)
        class_names = ['', class_names]
        mainWindow(columns=class_names, mainlist=mainlist, elements=elements)
    else:
        return

def createList():
    filepath = filedialog.asksaveasfilename(
        title='Create new database file:',
        filetypes=(('Database files', '*.db'), ('List Manager standart files', '*.lmdb'), ('All files', '*.*'))
    )
    with open(filepath, 'x') as file:
        file.write("[['test'],\n['For editing, run LM-Bash.py'],\n['1']]\n\n\n\n['name', 'content', 'value']")
    loadList()

chose_window = tk.Tk()
chose_window.title('LM Hello Window')

greeting_lbl = ttk.Label(chose_window, text='Welcome to List Manager Viewer!\nChoose option:')
greeting_lbl.pack(anchor=tk.CENTER)

technical_lbl = ttk.Label(chose_window, text='', width=46)
technical_lbl.pack()

buttons_frm = ttk.Frame(chose_window)
buttons_frm.pack()

open_btn = ttk.Button(buttons_frm, text='Open file', command=loadList)
open_btn.pack()

create_btn = ttk.Button(buttons_frm, text='Create new file', command=createList)
create_btn.pack()

chose_window.mainloop()