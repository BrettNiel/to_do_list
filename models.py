import json

taskList = []
fileName = "to_do_tasks.json"

def addTask(task):
    task_text = task.get().strip()
    if task_text:
        taskList.append(task_text)
        saveTasks()
        task.set("")

def deleteTask(task):
    taskList.remove(task)
    saveTasks()

def saveTasks():    
    with open(fileName, "w") as file:
        json.dump(taskList, file, indent=4)

def loadTasks():
    global taskList
    try:
        with open(fileName, "r") as file:
            taskList = json.load(file)
    except FileNotFoundError:
        taskList = []

loadTasks()