__author__ = 'venkat'

'''
from tkinter import *

toplevel = Tk()
toplevel.title("Port Statistics")
toplevel.geometry("1000x1000")

rows = []
for i in range(3):
    cols = []
    for j in range(4):
        e = Entry(toplevel, relief=RIDGE)
        e.grid(row=i, column=j, sticky=NSEW)
        if i == 0:
            if j == 0:
                e.insert(END, "  No Of Rx Packets")
            elif j == 1:
                e.insert(END, "  No Of Rx Packets")
            elif j == 2:
                e.insert(END, "  No Of Rx Drops")
            elif j == 3:
                e.insert(END, "  No Of Tx Packets")
            elif j == 4:
                e.insert(END, "  No Of TxPackets")
            elif j == 5:
                e.insert(END, "  No Of TxPackets")
        cols.append(e)
    rows.append(cols)

toplevel.mainloop()

'''

