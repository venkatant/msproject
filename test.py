from tkinter import*
import tkinter

top_row = 0
bottom_row = 0
root = Tk()
root.geometry("800x400")

top_frame= Frame(root, bg="red")
top_frame.pack(side=TOP)

top_label=Label(top_frame, text="Select the Switch to Get the Flow Table Information", fg="red")
top_label.grid(row=top_row)
top_row=top_row+1

bottom_frame= Frame(root)
bottom_frame.pack(side=TOP)

bottom_label=Label(bottom_frame, fg="green")
bottom_label.grid(row=bottom_row)
bottom_row=bottom_row+1

scrollbar = Scrollbar(top_frame)
listbox = Listbox(top_frame, yscrollcommand=scrollbar.set)
listbox.config(height=4)

listbox.insert(END, "venkat")
listbox.insert(END, "narayana")

listbox.grid(row=top_row,column=0,sticky="nsew", padx=1, pady=1)
scrollbar.grid(row=top_row,column=1,sticky="nsew", padx=1, pady=1)

scrollbar.config(command=listbox.yview)

for column in range(6):
    if column == 0:
        label = Label(bottom_frame, text="Switch ID", borderwidth=0, width=15, fg="red")
    elif column == 1:
        label = Label(bottom_frame, text="Port ID", borderwidth=0, width=10, fg="red")
    elif column == 2:
        label = Label(bottom_frame, text="Port MAC", borderwidth=0, width=10, fg="red")
    elif column == 3:
        label = Label(bottom_frame, text="Port IP", borderwidth=0, width=10, fg="red")
    elif column == 4:
        label = Label(bottom_frame, text="Port VLAN", borderwidth=0, width=10, fg="red")
    elif column == 5:
        label = Label(bottom_frame, text="Static Host", borderwidth=0, width=10, fg="red")

    label.configure(bg="white")
    label.grid(row=bottom_row, column=column, sticky="nsew", padx=1, pady=1)

bottom_row=bottom_row+1

for row in range(4):

    current_row = []

    for column in range(6):
        if column == 0:
            label = Label(bottom_frame, text="%s" % "Venkat", borderwidth=0, width=15)
        elif column == 1:
            label = Label(bottom_frame, text="%s" % "Venkat", borderwidth=0, width=10)
        elif column == 2:
            label = Label(bottom_frame, text="%s" % "Venkat", borderwidth=0, width=10)
        elif column == 3:
            label = Label(bottom_frame, text="%s" % "Venkat", borderwidth=0, width=10)
        elif column == 4:
            label = Label(bottom_frame, text="%s" % "Venkat", borderwidth=0, width=10)
        elif column == 5:
            label = Label(bottom_frame, text="%s" % "Venkat", borderwidth=0, width=10)
        label.configure(bg="white")
        label.grid(row=bottom_row, column=column, sticky="nsew", padx=1, pady=1)

        current_row.append(label)

    bottom_row=bottom_row+1

    for column in range(6):
        bottom_frame.grid_columnconfigure(column, weight=1)

root.mainloop()