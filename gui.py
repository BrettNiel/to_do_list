from tkinter import *
from tkinter import ttk
from models import *

def setup_gui(root):

    root.title("To Do List")

    main_frame = ttk.Frame(root, padding=(3, 3, 12, 12))
    main_frame.grid(column=0, row=0, sticky=(N, W, E, S))

    task_var = StringVar()
    task_entry = ttk.Entry(main_frame, width=30, textvariable=task_var)
    task_entry.bind("<Return>", lambda e: addTask(task_var))
    ttk.Label(main_frame, text="Enter task below").grid(column=1, row=1, sticky=(N, W), padx=50, pady=10)
    task_entry.grid(column=1, row=2, sticky=(N, W))

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    task_container = ttk.Frame(main_frame)
    task_container.grid(column=2, row=0, sticky=(N, W, E, S))
    ttk.Label(main_frame, text="Task List").grid(column=2, row=1, sticky=(N, W), padx=50, pady=10)

    #task_container.destroy()
    for task in taskList:
        ttk.Label(task_container, text=task).grid(column=2, row=2, sticky=(N, W), padx=50, pady=10)
        row += 1 

    