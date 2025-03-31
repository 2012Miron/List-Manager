# Plugins
### Why?
With update 1.2, List Manager have plugin support. This file contaits documentation about plugins.
## How to create plugin
Before starting, remember _two things_:
1. Plugin can have any name, but recommend to `plugin_` and your `name.py`.
2. Plugin is need to **connect manually**, becouse LM don't have auto connect.

Now, documentation:
### 1. Create file.
Download project, and in folder `plugins` create your file. Next, if this need, write code to list loading. Like this:
```Python
from plugin_main import mainlist, class_names
```

Now, you can use `mainlist` variable with data base.

After, write functions to manipulate with list, or other functionality.
Like this:
```Python
def createCopy():
    are_want = input('Are you want to create copy of list? (yes, no):> ')
    if are_want.lower() == 'yes':
        with open('data/copy.lmdb', 'x') as file:
            file.write(f'{mainlist}\n\n\n\n{class_names}')
        print('Copy created succesful')
        return
    else:
        print('Canceled')
        return
```

### 2. Connect plugin to the program
Save your plugin file, and go to `General.py`. Add import of your plugin, like this:
```Python
import os
import pickle
from plugins import plugin_main, plugin_my
```

And, between lines `plugin_main.deleteList(CMDI[6:])`, and `else:`, add commands of your plugin:
```Python
elif CMDI.startswith("delli"):
    plugin_main.deleteList(CMDI[6:])
elif CMDI == 'mkcopy':
    plugin_my.createCopy()
else:
```
Now you know, how create plugin for List Manager.