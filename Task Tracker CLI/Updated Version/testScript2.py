import subprocess
import json

def test1(): #answers in commments
    subprocess.run(["python", "task2.py", "add", "Hi"] ) # added in file
    subprocess.run(["python", "task2.py", "add", "Hi 2"]) # added in file
    subprocess.run(["python", "task2.py", "add", "Hi 3"]) # added in file
    subprocess.run(["python", "task2.py", "add", "Hi 4"]) # added in file
    subprocess.run(["python", "task2.py", "remove", "Hi"])# removed shouldn't have worked(Edge Case)
    subprocess.run(["python", "task2.py", "list", "todo"]) # gives list of todo with all 4 tasks(above)
    subprocess.run(["python", "task2.py", "list", "in-progress"]) # nothing in list
    subprocess.run(["python", "task2.py", "update", "1", "Hi again"]) # updates
    subprocess.run(["python", "task2.py", "update", "3", "coooool"]) # updates
    subprocess.run(["python", "task2.py", "mark-in-progress", "1"]) # mark in progress
    subprocess.run(["python", "task2.py", "mark-done", "1"]) # mark done
    subprocess.run(["python", "task2.py", "mark-in-progress", "2"]) # mark in progress
    subprocess.run(["python", "task2.py", "mark-done", "2"]) #mark done
    subprocess.run(["python", "task2.py", "mark-done", "3"]) # mark done
    subprocess.run(["python", "task2.py", "mark-in-progress", "2"]) # mark in progress shouldn't work




def test2(): # error / fails to run due to edge case
    subprocess.run(["python", "task2.py", "add", "21"])
    subprocess.run(["python", "task2.py", "add", "whats up"])
    subprocess.run(["python", "task2.py", "add", "cool too"])
    subprocess.run(["python", "task2.py", "add", "cool"])

    subprocess.run(["python", "task2.py", "mark-in-progress", "1"])
    subprocess.run(["python", "task2.py", "done", "HI"])# edge case shouldn't work
    subprocess.run(["python", "task2.py", "mark-in-progress", "2"])
    subprocess.run(["python", "task2.py", "done", "3"])

    subprocess.run(["python", "task2.py", "list", "done"])
    subprocess.run(["python", "task2.py", "list", "in-progress"])
    subprocess.run(["python", "task2.py", "list", "todo"])
    subprocess.run(["python", "task2.py", "list"])

def test3(): 
    subprocess.run(["python", "task2.py", "add", "21"])
    subprocess.run(["python", "task2.py", "add", "whats up"])
    subprocess.run(["python", "task2.py", "add", "cool too"])
    subprocess.run(["python", "task2.py", "add", "cool"])

    subprocess.run(["python", "task2.py", "mark-in-progress", "1"])
    subprocess.run(["python", "task2.py", "mark-done", "HI"])# edge case shouldn't work
    subprocess.run(["python", "task2.py", "mark-in-progress", "2"])
    subprocess.run(["python", "task2.py", "mark-done", "3"])

    subprocess.run(["python", "task2.py", "list", "done"])
    subprocess.run(["python", "task2.py", "list", "in-progress"])
    subprocess.run(["python", "task2.py", "list", "todo"])
    subprocess.run(["python", "task2.py", "list"])
# test 3 Final answers
# ID 0 -> task = "21" status = todo 
# ID 1 -> task = "whats up"  status = in progress
# ID 2 -> task = "cool too"  status = in progress
# ID 3 -> task = "cool"  status = done

def reset():
    with open("task.json", "w") as f:
        json.dump({},f)


test1()
reset()
test2()
reset()
test3()