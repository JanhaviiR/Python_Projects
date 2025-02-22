import sys
import json
import os
from datetime import datetime

tasks = []

def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            global tasks
            tasks = json.load(file)

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(task, priority='Medium'):
    tasks.append({"task": task, "completed": False, "created_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "completed_at": None, "priority": priority})
    print(f'Added task: {task} with priority: {priority}')
    save_tasks()

def delete_task(task_index):
    try:
        removed_task = tasks.pop(task_index)
        print(f'Deleted task: {removed_task["task"]}')
        save_tasks()
    except IndexError:
        print("Invalid task number")

def view_tasks():
    if not tasks:
        print("No tasks available")
    else:
        for i, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"
            print(f'{i + 1}. {task["task"]} [{status}] (Priority: {task["priority"]}, Created: {task["created_at"]}, Completed: {task["completed_at"]})')

def mark_task_completed(task_index):
    try:
        tasks[task_index]["completed"] = True
        tasks[task_index]["completed_at"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'Marked task as completed: {tasks[task_index]["task"]}')
        save_tasks()
    except IndexError:
        print("Invalid task number")

def show_help():
    print("""
    Available commands:
    - add <task> [priority]: Add a new task with an optional priority (Low, Medium, High)
    - delete <task_number>: Delete a task by its number
    - view: View all tasks
    - complete <task_number>: Mark a task as completed
    - help: Show this help message
    - exit: Exit the application
    Command aliases:
    - a: add
    - d: delete
    - v: view
    - c: complete
    - h: help
    - e: exit
    """)

def main():
    load_tasks()
    print("Task Manager Application")
    show_help()
    while True:
        command = input("Enter command: ").strip().split()
        if not command:
            continue
        action = command[0].lower()
        if action in ("add", "a"):
            priority = 'Medium'
            if len(command) > 2 and command[-1].capitalize() in ("Low", "Medium", "High"):
                priority = command.pop().capitalize()
            add_task(" ".join(command[1:]), priority)
        elif action in ("delete", "d"):
            if len(command) > 1 and command[1].isdigit():
                delete_task(int(command[1]) - 1)
            else:
                print("Invalid command")
        elif action in ("view", "v"):
            view_tasks()
        elif action in ("complete", "c"):
            if len(command) > 1 and command[1].isdigit():
                mark_task_completed(int(command[1]) - 1)
            else:
                print("Invalid command")
        elif action in ("help", "h"):
            show_help()
        elif action in ("exit", "e"):
            print("Exiting the application. Goodbye!")
            sys.exit()
        else:
            print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    main()
