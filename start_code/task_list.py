tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# MVP

# As a user, to manage my task list I would like a program that allows me to:

# Print a list of uncompleted tasks

def uncompleted_tasks(list):
    uncompleted_tasks = []
    
    for task in list:
        if task["completed"] == False:
            uncompleted_tasks.append(task)
    return uncompleted_tasks
        
print(uncompleted_tasks(tasks))



# Print a list of completed tasks


def completed_tasks(list):
    completed_tasks = []
    
    for task in list:
        if task["completed"] == True:
            completed_tasks.append(task)
    return completed_tasks
        
print(completed_tasks(tasks))


# Print a list of all task descriptions

def task_decriptions(list):
    task_decriptions = []

    for task in list:
        task_decriptions.append(task["description"])
    return task_decriptions

print(task_decriptions(tasks))

# Print a list of tasks where time_taken is at least a given time

def time_taken(list, time):
    time_taken = []

    for task in list:
        if task["time_taken"] <= time:
            time_taken.append(task["description"]) 
        return time_taken

print(time_taken(tasks, 5))   

# Print any task with a given description

def task_descriptor(list, description):
    found_task = None 

    for task in list:
        if task["description"] == description:
            found_task = task
    return found_task

print(task_descriptor(tasks, "Wash Dishes"))


