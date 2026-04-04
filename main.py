tasks = []

def add_task(task):
    tasks.append({"task": task, "done": False})

def show_tasks():
    for i, t in enumerate(tasks):
        status = "✔" if t["done"] else "✘"
        print(f"{i+1}. {t['task']} [{status}]")

def main():
    print("Task Manager Started")

if __name__ == "__main__":
    main()