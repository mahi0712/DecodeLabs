
my_tasks = []


def add_task():
    task = input("Enter task: ").strip()
    if task == "":
        print("Task cannot be empty!")
    else:
        my_tasks.append(task)
        print(f"Task '{task}' added successfully!")


def view_tasks():
    if not my_tasks:
        print("No tasks yet. Add one first!")
    else:
        print("\n--- Your Tasks ---")
        for index, task in enumerate(my_tasks):
            print(f"{index + 1}. {task}")
        print("------------------")


def main():
    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()