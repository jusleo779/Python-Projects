from datetime import datetime # imports the class named datetime inside the library datetime
import json # read, update, save data in a file 
import os # files: checks, rename, removes, etc. 
import argparse # argument security check

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
    print("Task added successfully (ID: ", i, ")" )
    i += 1
    

    with open("task.json","w") as f:
        json.dump(tasks, f, indent = 4)
        # adds the data from tasks -> file 
        # indent = 4 adds line breaks / indent 4 spaces for nested info

    
# update
def updateTask(n, task):
    n = str(n)
    print("original Task:", tasks[n]["task"])
    tasks[n]["task"] = task
    tasks[n]["updatedAt"] = datetime.now().isoformat()
    print("New Task:", task)

    with open("task.json","w") as f:
        json.dump(tasks, f, indent = 4)

# remove
def removeTask(n):
    n = str(n)
    del tasks[n]
    print("Task has successfully been removed")

    with open("task.json","w") as f:
        json.dump(tasks, f, indent = 4)

#updates status
def updateStatus(n, actionArg):
    n = str(n)
    
    if(tasks[n]["status"] == "done"):
        print("[!] Error: Cannot change completed task!")
        return
    
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


parser = argparse.ArgumentParser("Task Tracker")

# 1. Create the 'switchboard'
subparser = parser.add_subparsers(dest="command", required=True)

# Branch 1: Add
add_p = subparser.add_parser("add")
add_p.add_argument("task_text", type=str) # The word after 'add'

# Branch 2: Delete
del_p = subparser.add_parser("delete")
del_p.add_argument("id", type=int)        # The number after 'delete'

# Branch 3: Update
upd_p = subparser.add_parser("update")
upd_p.add_argument("id", type=int)        # Which ID to change
upd_p.add_argument("new_text", nargs="*") # What to change it to (vacuuming up words)

# Branch 4: List
l_p = subparser.add_parser("list")
l_p.add_argument("status", nargs="?", default="all") # Optional: 'todo', 'done', etc.\

# Branch 5: Mark 
mark_p = subparser.add_parser("mark-done", aliases=["mark-in-progress"])
mark_p.add_argument("id", type=int)


# Now we run the 'Emergency Brake' / Validation check
args = parser.parse_args()


aliases = {
    "mark-done" : "mark",
    "mark-in-progress" : "mark",
    "remove" : "delete"
}

actionChecker = aliases.get(args.command, args.command) # first val checks through dictionary # second val is backup if it fails to find smthing
actions = {
        "add" : lambda: addTask(args.task_text), 
        "mark" : lambda: updateStatus(args.id, args.command), 
        "list" : lambda: listStatus(args.status),
        "update" : lambda: updateTask(args.id, " ".join(args.new_text)),
        "delete" : lambda: removeTask(args.id)
        }

actions[actionChecker]()

    

