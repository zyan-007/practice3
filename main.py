import json

FILE = "tasks.json"

def load_tasks():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f)

tasks = load_tasks()

def add_task(task):
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print("Task added!")

def show_tasks():
    if not tasks:
        print("No tasks found.")
        return

    for i, t in enumerate(tasks):
        status = "✔" if t["done"] else "✘"
        print(f"{i+1}. {t['task']} [{status}]")

def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("Task marked as complete!")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nCommands: add | show | done | exit")
        cmd = input("Enter command: ").strip().lower()

        if cmd == "add":
            task = input("Enter task: ")
            add_task(task)

        elif cmd == "show":
            show_tasks()

        elif cmd == "done":
            show_tasks()
            try:
                i = int(input("Task number: ")) - 1
                complete_task(i)
            except:
                print("Please enter a valid number.")

        elif cmd == "exit":
            print("Goodbye!")
            break

        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()