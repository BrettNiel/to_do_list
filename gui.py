from tkinter import *
from tkinter import ttk
from main import root

# Title
root.title("To Do List")

# Frame inside window (necessary to provide theme to avoid old Tkinter classic version, NWES means it will stretch to expand with window size) 
mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# Note that takes a string value and attaches it to the frame with a label
note = StringVar()
note_entry = ttk.Entry(mainframe, width=30, textvariable=note)
ttk.Label(mainframe, text="Enter task below").grid(column=1, row=1, sticky=(N, W, E, S))
note_entry.grid(column=1, row=2, sticky=(N, W, E, S))

