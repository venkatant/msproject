from tkinter import*
import tkinter

root = Tk()

def grid():
   i = 0
   rows = []
   for i in range(5):
        cols = []
        for j in range(4):
            e = Entry(root, relief=RIDGE)
            e.grid(row=i, column=j, sticky=NSEW)
            e.insert(END, '%d.%d' % (i, j))
            cols.append(e)
        rows.append(cols)
   e.after(5000, grid)
grid()
root.mainloop()

'''
import tkinter
root = tkinter.Tk()
for r in range(3):
    for c in range(4):
        tkinter.Label(root, text='|R%s/C%s'%(r,c),
            borderwidth=1 ).grid(row=r,column=c)
root.mainloop()
'''