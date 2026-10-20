
taskList = []

def addTask(task):
    task_text = task.get().strip()
    taskList.append(task_text)
    task.set("")

def deleteTask(task):
    taskList.remove(task)