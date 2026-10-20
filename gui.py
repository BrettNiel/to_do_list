from functools import partial
from tkinter import *
from tkinter import ttk
from models import *

def setup_gui(root):

    def refresh_task_list():
            for widget in task_container.winfo_children():
                widget.destroy()
    
            for index, task in enumerate(taskList, start=2):
                ttk.Label(task_container, text=task).grid(column=2, row=index, sticky=(N, S, W, E), padx=50, pady=10)
                ttk.Button(task_container, text="Delete", command=partial(handle_delete, task)).grid(column=3, row=index, sticky=(N, S, W, E), padx=50, pady=10)
    
    def handle_add(event):
        addTask(task_var)
        refresh_task_list()
    
    def handle_delete(task):
        deleteTask(task)
        refresh_task_list()
    
    def update_scrollregion(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    root.title("To Do List")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure(".", font=("Helvetica", 12))

    main_frame = ttk.Frame(root, padding=(3, 3, 12, 12))
    main_frame.grid(column=0, row=0, sticky=(N, S, W, E))

    task_var = StringVar()
    task_entry = ttk.Entry(main_frame, width=30, textvariable=task_var)

    ttk.Label(main_frame, text="Task List").grid(column=2, row=1, sticky=(N, S, W, E), padx=50, pady=10)
    separator = ttk.Separator(main_frame, orient="horizontal")
    separator.grid(column=2, row=2, sticky=(W, E), padx=50, pady=10)

    canvas = Canvas(main_frame, highlightthickness=0, bg="#dcdad5")
    vertical_scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    horizontal_scrollbar = ttk.Scrollbar(main_frame, orient="horizontal", command=canvas.xview)

    task_container = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=task_container, anchor="nw")

    task_container.bind("<Configure>", update_scrollregion)
    canvas.configure(yscrollcommand=vertical_scrollbar.set)
    canvas.configure(xscrollcommand=horizontal_scrollbar.set)

    canvas.grid(column=2, row=3, sticky=(N, S, W, E))
    vertical_scrollbar.grid(column=3, row=3, sticky=(N, S))
    horizontal_scrollbar.grid(column=2, row=4, sticky=(W, E))

    task_entry.bind("<Return>", handle_add)
    ttk.Label(main_frame, text="Enter task below").grid(column=1, row=1, sticky=(N, W), padx=50, pady=10)
    task_entry.grid(column=1, row=2, sticky=(N))

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    main_frame.columnconfigure(2, weight=1)
    main_frame.rowconfigure(3, weight=1) 

    refresh_task_list()