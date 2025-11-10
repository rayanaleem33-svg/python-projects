import os

FILENAME = "tasks.txt"

def load_tasks():
    """Load tasks from file"""
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    """Save tasks to file"""
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    """Display the task list"""
    if not tasks:
        print("\n No tasks yet!")
    else:
        print("\n Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

def to_do_list():
    tasks = load_tasks()

    while True:
        print("========== TO-DO MENU ==========")
        print("1️ Add Task")
        print("2️ View Tasks")
        print("3️ Mark Task as Done")
        print("4️ Delete Task")
        print("5️ Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            new_task = input("Enter a new task: ").strip()
            if new_task:
                tasks.append(new_task)
                save_tasks(tasks)
                print("Task added!\n")

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            show_tasks(tasks)
            try:
                index = int(input("Enter task number to mark as done: ")) - 1
                if 0 <= index < len(tasks):
                    tasks[index] = f"✔️ {tasks[index]}"
                    save_tasks(tasks)
                    print("Task marked as done!\n")
                else:
                    print("Invalid number!\n")
            except ValueError:
                print("Please enter a valid number!\n")

        elif choice == "4":
            show_tasks(tasks)
            try:
                index = int(input("Enter task number to delete: ")) - 1
                if 0 <= index < len(tasks):
                    deleted = tasks.pop(index)
                    save_tasks(tasks)
                    print(f"Deleted task: {deleted}\n")
                else:
                    print("Invalid number!\n")
            except ValueError:
                print("Please enter a valid number!\n")

        elif choice == "5":
            print("Goodbye! Tasks saved.")
            break
        else:
            print("Invalid choice, try again!\n")

# Run the app
to_do_list()
