tasks = []
with open ("task.md" , "r") as fd:
    tasks = [line.strip() for line in fd]

while True:
    print("\n************ MENU ************")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Save and Exit")

    choice = input("Choose: ")
    
    if choice == "1":
        task = input("Task: ")
        if task in tasks:
            print ("This task already exists.")
        else:
            tasks.append(task)

    elif choice == "2":

        for task in tasks:
            print(task)

    elif choice == "3":
        with open ("task.md" , "w") as fd:
            fd.writelines(task + "\n" for task in tasks)

        break