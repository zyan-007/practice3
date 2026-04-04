tasks = []

def add_task(task):
    tasks.append({"task": task, "done": False})

def show_tasks():
    for i, t in enumerate(tasks):
        status = "✔" if t["done"] else "✘"
        print(f"{i+1}. {t['task']} [{status}]")

def main():
    while True:
        cmd = input("Enter command (add/show/exit): ")

        if cmd == "add":
            task = input("Enter task: ")
            add_task(task)

        elif cmd == "show":
            show_tasks()

        elif cmd == "exit":
            break

if __name__ == "__main__":
    main()