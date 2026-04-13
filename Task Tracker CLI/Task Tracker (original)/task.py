import sys # arguments in command prompt
from datetime import datetime # imports the class named datetime inside the library datetime
import json # read, update, save data in a file 
import os # files: checks, rename, removes, etc. 

#sys.argv[#] --> you can have as many arguments as you want but it will only take the arguments you call for
#                so when you call more than the max arguments it will fail so you shouldn't call more than one
#                before you get to that point



   

if os.path.exists("task.json"): # checks if file exists
    with open("task.json","r") as f: #opens file and reads it and closes when finished
        tasks = json.load(f)
else:
    tasks = {}
    
i = len(tasks)

# add
def addTask(nTask):
    global i
    tasks.update({ str(i) :{"task" : nTask, "status": "todo", "createdAt" : datetime.now().isoformat(), "updatedAt" : datetime.now().isoformat()}})
    i += 1
    print("Task added successfully (ID: ", i, ")" )

    with open("task.json","w") as f:
        json.dump(tasks, f, indent = 4)
        # adds the data from tasks -> file 
        # indent = 4 adds line breaks / indent 4 spaces for nested info

    
# update
def updateTask(n, task):
    print("original Task:", tasks[n]["task"])
    tasks[n]["task"] = task
    tasks[n]["updatedAt"] = datetime.now().isoformat()
    print("New Task:", task)

    with open("task.json","w") as f:
        json.dump(tasks, f, indent = 4)

# remove
def removeTask(n):
    del tasks[n]
    print("Task has successfully been removed")

    with open("task.json","w") as f:
        json.dump(tasks, f, indent = 4)

#updates status
def updateStatus(n):
    if(actionArg == "mark-done"):
        tasks[n]["status"] = "done"
    elif(actionArg == "mark-in-progress"):
        tasks[n]["status"] = "in-progress"     
    else:
        tasks[n]["status"] = "todo"

    tasks[n]["updatedAt"] = datetime.now().isoformat()

    with open("task.json","w") as f:
        json.dump(tasks, f, indent = 4)

# list of current status
def listStatus(s):
    if(s in ["in-progress", "todo", "done"]):
        print(s, ": \n")
        for x in tasks.values():
            if(x["status"] == s):
                print(x["task"])
        print("\n")
    else:
        for x in tasks:
            print(x,": ", tasks[x]["task"], "\n")


# Checks if the argument given is allowed
def checkIndx():
    if(actionArg in ["update","delete"] or actionArg.startswith("mark")):
        try:
            indx = sys.argv[2]
            if(indx not in tasks.keys()):
                print("[!] Error - Task ID, {indx}, doesn't exist. Try 'list' for active ID")
            else:
                if actionArg.startswith("mark"):
                    updateStatus(indx)
                elif actionArg == "update":
                    nTask = sys.argv[3]
                    updateTask(indx, nTask)
                elif actionArg == "delete":
                    removeTask(indx)
            
        except IndexError:
            print("[!] Error - Missing Task ID. Usage: python task.py [action] [ID]}") 
    else:
        print("[!] Error - unknown command \n")
        print("actions: add, delete, list, mark-done, mark-in-progress")



actionArg = sys.argv[1].lower()

print(sys.argv[0], actionArg)

aliases = {
    "remove" : "delete",
    "mark-done" : "check",
    "mark-in-progress" : "check",
    "update" : "check"

}
actionChecker = aliases.get(actionArg, actionArg) # first val checks through dictionary # second val is backup if it fails to find smthing
actions = {"add" : lambda: addTask(sys.argv[2]), "check" : lambda: checkIndx(), "list" : lambda: listStatus(sys.argv[2] if(len(sys.argv) > 2) else "")}

actions[actionChecker]()

    

