"""
  DecodeLabs Internship - Python Project 1         
  CLI To-Do List App                                                                                
  Name   : Rabeesh                                                                               
  Concepts : Lists, Dictionaries, Loops, File I/O, JSON   

"""

import json
import os
from datetime import datetime



#  CONFIGURATION

DATA_FILE = "tasks.json"          # JSON file for persistence
DIVIDER   = "─" * 45             # Visual separator line



#  FILE I/O — PERSISTENCE LAYER
def load_tasks() -> list:
    """Load tasks from JSON file. Returns empty list if file not found."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks: list) -> None:
    """Save the current task list to JSON file (persistence)."""
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


#  CORE FUNCTIONS — DATA LOGIC (MODEL LAYER)

def add_task(tasks: list, task_name: str) -> None:
    """
    Add a new task dictionary to the tasks list.
    Each task = a 'row' in our in-memory database.
    Uses list.append() — the key skill for this project.
    """
    task = {
        "id"       : len(tasks) + 1,
        "task"     : task_name,
        "status"   : "Pending",
        "created"  : datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    tasks.append(task)        # KEY CONCEPT: list.append()
    save_tasks(tasks)
    print(f"\n  ✅ Task added → '{task_name}'")


def view_tasks(tasks: list) -> None:
    """
    Display all tasks using enumerate() — the professional way.
    Demonstrates the READ operation (Display layer).
    """
    print(f"\n  {'ID':<5} {'STATUS':<12} {'TASK':<25} {'CREATED'}")
    print(f"  {DIVIDER}")

    if not tasks:
        print("  📋  No tasks yet! Add your first task.\n")
        return

    # KEY CONCEPT: enumerate() loop — professional Python
    for index, task in enumerate(tasks, start=1):
        status_icon = "✅" if task["status"] == "Done" else "🔲"
        print(
            f"  {index:<5}"
            f"{status_icon} {task['status']:<10}"
            f"{task['task']:<25}"
            f"{task['created']}"
        )
    print()


def mark_done(tasks: list, task_id: int) -> None:
    """Mark a task as completed by updating its status field."""
    if 1 <= task_id <= len(tasks):
        tasks[task_id - 1]["status"] = "Done"
        save_tasks(tasks)
        print(f"\n  ✅ Task {task_id} marked as Done!\n")
    else:
        print("\n  ❌ Invalid task ID.\n")


def delete_task(tasks: list, task_id: int) -> None:
    """Remove a task from the list by index."""
    if 1 <= task_id <= len(tasks):
        removed = tasks.pop(task_id - 1)
        # Re-assign IDs after deletion
        for i, task in enumerate(tasks, start=1):
            task["id"] = i
        save_tasks(tasks)
        print(f"\n  🗑️  Deleted → '{removed['task']}'\n")
    else:
        print("\n  ❌ Invalid task ID.\n")


def clear_all(tasks: list) -> None:
    """Clear all tasks after confirmation."""
    confirm = input("  ⚠️  Clear ALL tasks? (yes/no): ").strip().lower()
    if confirm == "yes":
        tasks.clear()
        save_tasks(tasks)
        print("\n  🗑️  All tasks cleared.\n")
    else:
        print("\n  Cancelled.\n")

#  UI LAYER — VIEW (DISPLAY FUNCTIONS)


def print_banner() -> None:
    """Print the application header banner."""
    print("\n" + "═" * 47)
    print("  🚀  DecodeLabs │ Python Project 1")
    print("       CLI To-Do List  │  Batch 2026")
    print("═" * 47)


def print_menu() -> None:
    """Print the main menu options."""
    print(f"\n  {DIVIDER}")
    print("  [1]  ➕  Add Task")
    print("  [2]  📋  View Tasks")
    print("  [3]  ✅  Mark Task as Done")
    print("  [4]  🗑️   Delete a Task")
    print("  [5]  💣  Clear All Tasks")
    print("  [6]  🚪  Exit")
    print(f"  {DIVIDER}")


def get_integer_input(prompt: str) -> int:
    """Safely get an integer input from the user."""
    try:
        return int(input(prompt).strip())
    except ValueError:
        print("\n  ❌ Please enter a valid number.\n")
        return -1



#  MAIN ENTRY POINT

def main() -> None:
    """
    Main application loop.
    Follows IPO Model: Input → Process → Output
    Professional pattern: if __name__ == '__main__'
    """
    tasks = load_tasks()       # Load from disk (persistence)
    print_banner()

    while True:
        print_menu()
        choice = input("  Choose an option (1-6): ").strip()

        if choice == "1":
            task_name = input("\n  Enter task description: ").strip()
            if task_name:
                add_task(tasks, task_name)
            else:
                print("\n  ❌ Task name cannot be empty.\n")

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            view_tasks(tasks)
            task_id = get_integer_input("  Enter Task ID to mark Done: ")
            if task_id != -1:
                mark_done(tasks, task_id)

        elif choice == "4":
            view_tasks(tasks)
            task_id = get_integer_input("  Enter Task ID to delete: ")
            if task_id != -1:
                delete_task(tasks, task_id)

        elif choice == "5":
            clear_all(tasks)

        elif choice == "6":
            print("\n  👋  Goodbye! Keep building. — DecodeLabs\n")
            break

        else:
            print("\n  ❌ Invalid option. Choose between 1 and 6.\n")


#  PROGRAM ENTRY GUARD
if __name__ == "__main__":
    main()
