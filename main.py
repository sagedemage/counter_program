from tkinter import *
from tkinter import ttk

win_width = 300
win_height = 170

root = Tk()
root.title("Counter")
root.minsize(width=win_width, height=win_height)
root.maxsize(width=win_width, height=win_height)

counter = 0
counter_label = StringVar(value="Counter: 0")

frm = ttk.Frame(root, padding=0)
frm.pack(fill="both", expand=True)

counter_info_label = ttk.Label(frm, 
                               textvariable=counter_label,
                               font=("Arial", 16, "bold"),
                               )

counter_info_label.place(relx=0.5, rely=0.33, anchor=CENTER)

def clicked():
    global counter
    counter += 1
    counter_label.set("Counter: " + str(counter))

click_button = ttk.Button(frm, text="Click Me!", command=clicked).place(relx=0.5, rely=0.66, anchor=CENTER)

root.mainloop()