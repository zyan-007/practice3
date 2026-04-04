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

def show_tasks():
    for i, t in enumerate(tasks):
        status = "✔" if t["done"] else "✘"
        print(f"{i+1}. {t['task']} [{status}]")

def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)

def main():
    while True:
        cmd = input("Enter command (add/show/done/exit): ")

        if cmd == "add":
            task = input("Enter task: ")
            add_task(task)

        elif cmd == "show":
            show_tasks()

        elif cmd == "done":
            show_tasks()
            i = int(input("Enter task number: ")) - 1
            complete_task(i)

        elif cmd == "exit":
            break

if __name__ == "__main__":
    main()