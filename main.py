__author__ = 'venkat'

import tkinter
from host_tracker import *
from node_monitoring import *
from port_statistics import *
from flow_statistics import *

def deepinspectionofpacket():
    return

def mdumpfunction(self):
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

def create_button_with_scoped_image(root):
    img = tkinter.PhotoImage(file="78.png")  # reference PhotoImage in local variable
    button = tkinter.Label(root, image=img)
    button.img = img
    button.place(x=10, y=10, relwidth=1, relheight=1)
    button.grid()

def start():
    root = Tk()

    # Main Menu Contruction
    # Menu is a class and put it in root 'window'

    mainMenu = Menu(root)

    # Configure Menu for main Menu
    root.config(menu=mainMenu, bg="orange")
    root.title("Welcome to Network Monitoring System")
    root.geometry("605x300")

    # Insert Image in Main Page
    create_button_with_scoped_image(root)

    # SubMenu which is now 'fault Menu'
    faultMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="Fault Monitoring", menu=faultMenu)

    # Command add functionality once we select the object in drop down list
    faultMenu.add_command(label="Node Status", command=mLinkFaultMenu)
    faultMenu.add_separator()
    faultMenu.add_command(label="Link Status", command=linkfaultmenu)

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
