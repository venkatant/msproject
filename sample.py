__author__ = 'venkat'

from tkinter import *

root = Tk()

def send_mail():
    return
def send_trap():
    return
def mradioselect():
    return

check_gmail = IntVar()
check_snmp = IntVar()
var = IntVar()

#root.config(bg="grey")

LB=Label(root, text="All Node Link status", borderwidth=0)
LB.grid(row=0, columnspan=4)
#LB.configure(bg="orange")

CB1=Checkbutton(root, text="Send E-Mail", variable=check_gmail, width=10, command=send_mail)
CB1.grid(row=6, column=0,sticky=E)
#CB1.configure(bg="orange")

CB2=Checkbutton(root, text="Send Trap", variable=check_snmp, width=10, command=send_trap)
CB2.grid(row=6, column=1,sticky=E)
#CB2.configure(bg="orange")

RB1 = Radiobutton(root, text="1 Sec ", variable=var, value=1, width=10, command=mradioselect)
RB1.grid(row=8, column=0, sticky=W)
#RB1.configure(bg="orange")
RB2 = Radiobutton(root, text="5 Sec ", variable=var, value=5, width=10, command=mradioselect)
RB2.grid(row=8, column=1, sticky=W)
#RB2.configure(bg="orange")
RB3 = Radiobutton(root, text="10 Sec", variable=var, value=10, width=10, command=mradioselect)
RB3.grid(row=8, column=2, sticky=W)
#RB3.configure(bg="orange")
RB4 = Radiobutton(root, text="30 Sec", variable=var, value=30, width=10, command=mradioselect)
RB4.grid(row=8, column=3, sticky=W)
#RB4.configure(bg="orange")

def table():
    for row in range(5):

        current_row = []
        for column in range(4):
            if row != 0 :
                label = Label(root, text="%s/%s" % (row, column), borderwidth=0, width=10)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                label.configure(bg="white")
                if row==2:
                    label.config(bg="red")
                else:
                    label.config(fg="black")
                current_row.append(label)

        for column in range(4):
            root.grid_columnconfigure(column, weight=1)
        lb=Label(root, text="")
        lb.grid(row=5, sticky=W)
        #lb.configure(bg="orange")
    print("5 sec")
    root.after(5000,table)

table()

root.mainloop()

