# Task Tracker CLI
<a href="https://roadmap.sh/projects/task-tracker"> Project LINK</a>

This repository contains a simple **Task Tracker Command-Line Interface (CLI)** script for managing tasks. You can add, update, delete, and list tasks in different states such as "done," "to-do," or "in-progress." Task data is stored in a JSON file for persistence.

---

## Features

- **Add Tasks**: Create new tasks with unique IDs and descriptions.
- **Update Tasks**: Modify the description of an existing task.
- **Delete Tasks**: Remove a task by its ID.
- **Mark Tasks as "In Progress" or "Done"**: Change the status of a task.
- **List Tasks**: View tasks based on their status or list all tasks.

---

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd task-tracker-cli
   ```

2. Install Python (if not installed). This script works with **Python 3.x**.

3. Ensure the directory `./db/` exists and contains a `db.json` file. The `db.json` file should be initialized with an empty list:
   ```json
   []
   ```

---

## Usage

Run the script using the command:
```bash
python task_tracker.py
```

### Available Commands

You will interact with the program using the following commands in the CLI:

| Command                      | Description                                         | Example Command                          |
|------------------------------|-----------------------------------------------------|------------------------------------------|
| `add <description>`          | Add a new task.                                     | `add Write documentation`                |
| `update <id> <new-desc>`     | Update the description of a task by its ID.         | `update 1 Fix documentation typos`       |
| `delete <id>`                | Delete a task by its ID.                            | `delete 1`                               |
| `mark-in-progress <id>`      | Mark a task as "in-progress" by its ID.             | `mark-in-progress 2`                     |
| `mark-done <id>`             | Mark a task as "done" by its ID.                    | `mark-done 3`                            |
| `list`                       | List all tasks.                                     | `list`                                   |
| `list done`                  | List all tasks with status "done."                  | `list done`                              |
| `list todo`                  | List all tasks with status "to-do."                 | `list todo`                              |
| `list in-progress`           | List all tasks with status "in-progress."           | `list in-progress`                       |
| `exit`                       | Exit the program.                                   | `exit`                                   |

---

## Logs

The script logs actions and errors to `tasks_tracker.log`. Logs include:

- Errors loading the database file.
- Task additions, updates, and deletions.

---

## File Structure

- `task_tracker.py`: The main Python script.
- `db/`: Directory for storing the task database.
  - `db.json`: Stores the task data in JSON format.
- `tasks_tracker.log`: Log file for tracking operations and errors.

---

## Example Session

```bash
TASK TRACKER

INSERT ONE COMMAND
- Add(id:int)
- UPDATE(id:int)
- DELETE(id:int)
- STATUS(progress-finish)
- LIST(done - todo - in-progress)

add Write documentation

TASK CREATED: {'id': 1, 'description': 'Write documentation', 'status': 'not-done', 'createdAt': '2024-12-16 12:00:00', 'updatedAt': None}

list
{'id': 1, 'description': 'Write documentation', 'status': 'not-done', 'createdAt': '2024-12-16 12:00:00', 'updatedAt': None}

mark-done 1
TASK UPDATED: {'id': 1, 'description': 'Write documentation', 'status': 'done', 'createdAt': '2024-12-16 12:00:00', 'updatedAt': '2024-12-16 12:05:00'}

list done
{'id': 1, 'description': 'Write documentation', 'status': 'done', 'createdAt': '2024-12-16 12:00:00', 'updatedAt': '2024-12-16 12:05:00'}

exit
```

---

## Contribution

Feel free to open issues or create pull requests to improve the functionality or add features.

---

## License

This project is open-source and available under the MIT License.
