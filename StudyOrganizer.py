TASK_FILE = "tasks.txt"
tasks = []  # [ [name, category, status], ... ]

def load_tasks():
    """Load tasks from file into list"""
    try:
        with open(TASK_FILE, "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    tasks.append(parts)
    except FileNotFoundError:
        pass  # If file doesn't exist, start empty

def save_tasks():
    """Save tasks list into file"""
    with open(TASK_FILE, "w") as file:
        for t in tasks:
            file.write("|".join(t) + "\n")

def add_task():
    name = input("Task name: ")
    category = input("Category: ")
    tasks.append([name, category, "Pending"])
    print("✅ Task added!")

def list_tasks():
    if len(tasks) == 0:
        print("No tasks yet!")
    else:
        print("\n--- TASK LIST ---")
        for i, t in enumerate(tasks):
            print(f"{i+1}. {t[0]} - {t[1]} - {t[2]}")

def mark_done():
    list_tasks()
    index = int(input("Task number to mark as done: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index][2] = "Done"
        print("✅ Task marked as completed!")
    else:
        print("❌ Invalid selection!")

def delete_task():
    list_tasks()
    index = int(input("Task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"🗑 Deleted: {removed[0]}")
    else:
        print("❌ Invalid selection!")

def main():
    load_tasks()

    while True:
        print("""
===== STUDY ORGANIZER =====
1 - Add Task
2 - List Tasks
3 - Mark Task as Done
4 - Delete Task
5 - Exit
""")

        choice = input("Choose: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            save_tasks()
            print("Saved and goodbye!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
