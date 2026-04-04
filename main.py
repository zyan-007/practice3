tasks = []

def add_task(task):
    tasks.append({"task": task, "done": False})

def show_tasks():
    for i, t in enumerate(tasks):
        status = "✔" if t["done"] else "✘"
        print(f"{i+1}. {t['task']} [{status}]")

def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True

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