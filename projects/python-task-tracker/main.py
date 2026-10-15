"""A small command-line task tracker for practicing Python fundamentals."""


def show_tasks(tasks):
    """Print all tasks with their numbers and completion status."""
    if not tasks:
        print("\nNo tasks yet. Add one to get started.")
        return

    print("\nYour tasks:")
    for number, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not done"
        print(f"{number}. [{status}] {task['title']}")


def add_task(tasks):
    """Ask for a task title and add it to the list."""
    title = input("Task title: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return

    tasks.append({"title": title, "done": False})
    print("Task added.")


def complete_task(tasks):
    """Mark a task as completed by its displayed number."""
    if not tasks:
        print("There are no tasks to complete.")
        return

    show_tasks(tasks)
    try:
        number = int(input("Task number to mark as done: "))
    except ValueError:
        print("Please enter a whole number.")
        return

    if number < 1 or number > len(tasks):
        print("That task number doesn't exist.")
        return

    tasks[number - 1]["done"] = True
    print("Task marked as done.")


def remove_task(tasks):
    """Remove a task by its displayed number."""
    if not tasks:
        print("There are no tasks to remove.")
        return

    show_tasks(tasks)
    try:
        number = int(input("Task number to remove: "))
    except ValueError:
        print("Please enter a whole number.")
        return

    if number < 1 or number > len(tasks):
        print("That task number doesn't exist.")
        return

    removed_task = tasks.pop(number - 1)
    print(f"Removed: {removed_task['title']}")


def main():
    """Run the interactive task tracker menu."""
    tasks = []

    while True:
        print("\n=== Python Task Tracker ===")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Remove task")
        print("5. Quit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
