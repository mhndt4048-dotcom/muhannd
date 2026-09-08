tasks = []

while True:
    print("\n=== To-Do List ===")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Delete task")
    print("4. Mark task as completed")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append({"task": task, "completed": False})
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i, item in enumerate(tasks, start=1):
                status = "Done" if item["completed"] else "Not Done"
                print(f"{i}. {item['task']} - {status}")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, item in enumerate(tasks, start=1):
                print(f"{i}. {item['task']}")

            try:
                number = int(input("Enter task number to delete: "))
                if 1 <= number <= len(tasks):
                    deleted = tasks.pop(number - 1)
                    print(f"Task '{deleted['task']}' deleted successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        if not tasks:
            print("No tasks to complete.")
        else:
            for i, item in enumerate(tasks, start=1):
                print(f"{i}. {item['task']}")

            try:
                number = int(input("Enter task number to mark as completed: "))
                if 1 <= number <= len(tasks):
                    tasks[number - 1]["completed"] = True
                    print("Task marked as completed!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
