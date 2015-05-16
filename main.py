__author__ = 'venkat'


from tkinter import *

import httplib2
import json
import time
from header import *
from host_tracker import *
from link_monitoring import *
from port_statistics import *

def mdumpfunction():
    return

def deepinspectionofpacket():
    return

def flowstatistics():
    toplevel = Toplevel()
    toplevel.geometry("500x500")
    toplevel.title("Flow Statistics Per Switch")

    scrollbar = Scrollbar(toplevel)
    nodelist = Listbox(toplevel, yscrollcommand=scrollbar.set)

    for line in range(100):
        nodelist.insert(END, "00:00:00:00:00:00:" + str(line))

    nodelist.pack(side=LEFT, fill=BOTH)
    scrollbar.pack(side=LEFT, fill=Y)

    # nodelist.bind('<<ListboxSelect>>', mdumpfunction)

    scrollbar.config(command=nodelist.yview)
    submit = Button(toplevel, text="Submit", command=mdumpfunction)

    submit.pack()

    return

def display_link_status():
    rows = []
    for i in range(5):
        cols = []
        for j in range(4):
            e = Entry(relief=RIDGE)
            e.grid(row=i, column=j, sticky=NSEW)
            e.insert(END, '%d.%d' % (i, j))
            cols.append(e)
        rows.append(cols)
    return

def mLinkFaultMenu():
    toplevel = Toplevel()
    linkLabel = Label(toplevel, text="Link Information")
    linkLabel.pack()
    print("I am Fault Menu Add Link Status")
    print()

    return

def start():
    root = Tk()

    # Main Menu Contruction
    # Menu is a class and put it in root 'window'

    mainMenu = Menu(root)

    # Configure Menu for main Menu
    root.config(menu=mainMenu)
    root.title("Network Monitoring Application")
    root.geometry("800x500")

    # Insert Image in Main Page

    # SubMenu which is now 'fault Menu'
    faultMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="Fault Monitoring", menu=faultMenu)

    # Command add functionality once we select the object in drop down list
    faultMenu.add_command(label="Node Status", command=linkfaultmenu)
    faultMenu.add_separator()
    faultMenu.add_command(label="Link Status", command=mLinkFaultMenu)

    # SubMenu which is now 'Configuration'
    configMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="Configuration", menu=configMenu)
    configMenu.add_command(label="Flow Addition", command=mdumpfunction)
    configMenu.add_separator()
    configMenu.add_command(label="Flow Deletion", command=mdumpfunction)
    configMenu.add_separator()
    configMenu.add_command(label="Flow Modify", command=mdumpfunction)

    # SubMenu which is now 'Accounting'
    flowMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="Accounting", menu=flowMenu)
    flowMenu.add_command(label="Flow Statistics", command=flowstatistics)
    flowMenu.add_separator()
    flowMenu.add_command(label="Port Statistics", command=portstatistics)
    flowMenu.add_separator()
    flowMenu.add_command(label="Host Tracker", command=hosttracker)

    # SubMenu which is now 'Performance'
    performance = Menu(mainMenu)
    mainMenu.add_cascade(label="Performance", menu=performance)

    # SubMenu which is now 'Security'
    securitymenu = Menu(mainMenu)
    mainMenu.add_cascade(label="Security", menu=securitymenu)
    securitymenu.add_command(label="DIP", command=deepinspectionofpacket)
    securitymenu.add_separator()

    root.mainloop()

if __name__ == '__main__':
    start()
