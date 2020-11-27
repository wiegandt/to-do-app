import sys

task_list = []

def print_usage():
    print("""Command line arguments:
      -l   Lists all the tasks
      -a   Adds a new task
      -r   Removes a task
      -c   Completes a task""")

def list_tasks():
    #open the task file for reading
    #handle file missing exception
    #should read all lines and print them
    try:
        file = open("todos.txt", "r")
        f = file.readlines()
        if len(f) == 0:
            print("No todos for today :)")
        else:
            n = 1
            for i in f:
                print(str(n) + " - " + i)
                n += 1
    except FileNotFoundError:
        print("File not found")


def add_task(task):
    #open task file for writing
    #handle file missing exception
    #append the new task to the end of the file
    try:
        file = open("todos.txt", "a")
        file.write("[ ] " + task + "\n")
    except FileNotFoundError:
        print("File not found")
    print("add " + task + " to the list")

def remove_task(task):
    with open("todos.txt", "r") as f:
        lines = f.readlines()
    if len(lines) <= int(task):
        print("Unable to remove: index out of bound")
    with open("todos.txt", "w") as f:
        count = 1
        for line in lines:
            if count != int(task):
                f.write(line)
            count += 1
    print("remove " + task + " from list")


def check_task(task):
    with open("todos.txt", "r") as f:
        lines = f.readlines()
    if len(lines) <= int(task):
        print("Unable to check: index out of bound")
    with open("todos.txt", "w") as f:
        count = 1
        for line in lines:
            if count == int(task):
                line = line.replace("[ ] ", "[x] ")
                print(line)
            count += 1
            f.write(line)


#if len(sys.argv) == 1: #in case there is no command/argument
#    print_usage()
if len(sys.argv) == 2 and sys.argv[1] == "-l":
    list_tasks()
elif len(sys.argv) == 3 and sys.argv[1] == "-a":
    add_task(sys.argv[2])
elif len(sys.argv) == 2 and sys.argv[1] == "-a":
    print("Unable to add: no task provided")
elif len(sys.argv) == 3 and sys.argv[1] == "-r":
    try:
        task = int(sys.argv[2])
        remove_task(sys.argv[2])
    except ValueError:
        print("Unable to remove: index is not a number")
elif len(sys.argv) == 2 and sys.argv[1] == "-r":
    print("Unable to remove: index not provided")
elif len(sys.argv) ==2 and sys.argv[1] == "-c":
    print("Unable to check: no index provided")
elif len(sys.argv) == 3 and sys.argv[1] == "-c":
    try:
        task = int(sys.argv[2])
        check_task(sys.argv[2])
    except ValueError:
        print("Unable to remove: index is not a number")
else:
    print("Unsupported argument")
    print_usage()







