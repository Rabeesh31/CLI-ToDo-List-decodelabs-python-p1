# CLI To-Do List Application

**DecodeLabs Python Internship — Project 1**

## Overview

This project is a terminal-based To-Do List application developed as part of the DecodeLabs Python Internship (Batch 2026). It demonstrates fundamental Python programming concepts through a practical, real-world use case — managing tasks from the command line with full data persistence across sessions.

## Author

| Field        | Details                             |
|--------------|-------------------------------------|
| **Name**     | Rabeesh                             |
| **Program**  | DecodeLabs Python Internship        |
| **Batch**    | 2026                                |
| **Project**  | Project 1 — CLI To-Do List App      |


## Project Structure

cli-todo-list/
│
├── todo_list.py        # Main application — all logic and UI
├── tasks.json          # Persistent task storage (auto-generated at runtime)
└── README.md           # Project documentation


> **Note:** `tasks.json` is created automatically on first run. It should be added to `.gitignore` and not committed to version control.


## Features

| No. | Feature         | Description                                            |
|-----|-----------------|--------------------------------------------------------|
| 1   | Add Task        | Creates a new task with a unique ID and timestamp      |
| 2   | View Tasks      | Lists all tasks with their current status              |
| 3   | Mark as Done    | Updates a task's status from `Pending` to `Done`       |
| 4   | Delete Task     | Removes a specific task by ID, with ID re-indexing     |
| 5   | Clear All       | Deletes all tasks after an explicit confirmation step  |
| 6   | Exit            | Saves state and exits the application cleanly          |


## Concepts Demonstrated

| Concept                | Application in Project                                          |
|------------------------|-----------------------------------------------------------------|
| **Lists**              | In-memory storage and manipulation of task collections          |
| **Dictionaries**       | Structured task objects with `id`, `task`, `status`, `created`  |
| **Loops**              | `while` loop for the menu; `enumerate()` for task display       |
| **File I/O**           | Reading and writing data using `open()`                         |
| **JSON**               | Persistence via `json.load()` and `json.dump()`                 |
| **Functions**          | Modular design following the MVC (Model-View-Controller) pattern|
| **Exception Handling** | Safe numeric input parsing using `try/except`                   |


## Getting Started

### Prerequisites

- Python **3.7 or higher**
- No external libraries required — standard library only

### Installation & Usage

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/cli-todo-list.git

# 2. Navigate into the project directory
cd cli-todo-list

# 3. Run the application
python todo_list.py
```


## Sample Output

═══════════════════════════════════════════════════
  🚀  DecodeLabs │ Python Project 1
       CLI To-Do List  │  Batch 2026
═══════════════════════════════════════════════════

  ─────────────────────────────────────────────
  [1]  Add Task
  [2]  View Tasks
  [3]  Mark Task as Done
  [4]  Delete a Task
  [5]  Clear All Tasks
  [6]  Exit
  ─────────────────────────────────────────────
  Choose an option (1–6):

## Data Storage

Tasks are persisted locally in `tasks.json`. Each record follows this structure:

```json
{
    "id": 1,
    "task": "Complete Python project",
    "status": "Pending",
    "created": "2026-06-10 14:30"
}
```

The file is read on startup and written after every modification, ensuring no data loss between sessions.

## File Reference

| File            | Format  | Description                          |
|-----------------|---------|--------------------------------------|
| `todo_list.py`  | `.py`   | Core application source code         |
| `tasks.json`    | `.json` | Runtime-generated persistent storage |
| `README.md`     | `.md`   | Project documentation (this file)    |

