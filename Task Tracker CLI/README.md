# Task Tracker CLI

# OVERVIEW
Task Tracker CLI is a command-line application built with Python that manages tasks efficiently on your local machine. It tracks essential metadata for each task including: creation date, last modified timestamp, and current status allowing for easy organization and monitoring for work.

# FEATURES

* **Add**  - Create task and adds to your list
* **Update** - Modify task description
* **Delete** - Remove unwanted/completed tasks 
* **List** - View tasks or filter by todo, in-progress, done
* **mark-done** - Updates the task status to done
* **mark-in-progress** - Updates the task status to in-progress


# USAGE

* **Command Syntax**: [python] ["fileName"] ["action"]["--ID number or task"]["--New Task description"]

* python task2.py add  "Task"
* python task2.py update 1 "New Task"
* python task2.py remove 1
* python task2.py list
* python task2.py list todo
* python task2.py list done
* python task2.py list in-progress
* python task2.py mark-done
* python task2.py mark-in-progress



# TECHNICAL IMPLEMENTATIONS

## KEY DESIGN DECISIONS

* Data Structures Matter: Hashmap/dictionary lookups outperform list searches for large datasets
* Dispatcher Pattern: Eliminates if/else chains and improves maintainability
* Argument Validation – argparse validates the argument and format, preventing invalid input from stoping the code.
* Storage – JSON storage with timestamps enables reliable data recovery and track trails for task modifications.
* Modular Functions – Each operation (add, list, delete, update) is implemented as a separate function, improving testability and reusability.

# CONNECTION TO HARDWARE ENGINEERING

This project demonstrates two skills essential to hardware engineering:

**Test Automation** – Using tools like subprocess and argparse, automated testing reveals issues faster than manual verification. In hardware contexts, this principle applies to sensor validation, microcontroller debugging, and signal integrity checks. Through automation, checking for issues reduces the time and improves reliability.

**Program Organization** – Well-structured code is critical for collaboration and scalability. Hardware engineering teams depend on organized codebases to understand project goals, track remaining tasks, and integrate new features. Scalable designs, like the hashmap structure, make it straightforward to add functionality without changing essential code.

## LESSONS LEARNED

* Data structure selection directly impacts performance under higher loads
* Dispatcher patterns improve code clarity and adaptability
* Input validation through the command line prevents future errors
* Consistent timestamp formatting enables reliable data tracking
* The Python standard library often provides sufficient tools to solve common issues




