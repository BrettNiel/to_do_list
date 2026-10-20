from functools import partial
from tkinter import *
from tkinter import ttk
from models import *

def setup_gui(root):

    root.title("To Do List")

    main_frame = ttk.Frame(root, padding=(3, 3, 12, 12))
    main_frame.grid(column=0, row=0, sticky=(N, W, E, S))

    task_var = StringVar()
    task_entry = ttk.Entry(main_frame, width=30, textvariable=task_var)

    task_container = ttk.Frame(main_frame)
    task_container.grid(column=2, row=2, sticky=(N, W, E, S))
    ttk.Label(main_frame, text="Task List").grid(column=2, row=1, sticky=(N, W), padx=50, pady=10)

    def refresh_task_list():
        for widget in task_container.winfo_children():
            widget.destroy()

        for index, task in enumerate(taskList, start=2):
            ttk.Label(task_container, text=task).grid(column=2, row=index, sticky=(N, W), padx=50, pady=10)
            ttk.Button(task_container, text="Delete", command=partial(handle_delete, task)).grid(column=3, row=index, sticky=(N, W), padx=50, pady=10)

    def handle_add(event):
        addTask(task_var)
        refresh_task_list()

    def handle_delete(task):
        deleteTask(task)
        refresh_task_list()

    task_entry.bind("<Return>", handle_add)
    ttk.Label(main_frame, text="Enter task below").grid(column=1, row=1, sticky=(N, W), padx=50, pady=10)
    task_entry.grid(column=1, row=2, sticky=(N, W))

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)