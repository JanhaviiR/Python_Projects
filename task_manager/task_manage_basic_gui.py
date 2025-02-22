import sys
import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})
    messagebox.showinfo("Success", f'Added task: {task}')

def delete_task(task_index):
    try:
        removed_task = tasks.pop(task_index)
        messagebox.showinfo("Success", f'Deleted task: {removed_task["task"]}')
    except IndexError:
        messagebox.showerror("Error", "Invalid task number")

def view_tasks():
    if not tasks:
        messagebox.showinfo("Info", "No tasks available")
    else:
        tasks_list = ""
        for i, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"
            tasks_list += f'{i + 1}. {task["task"]} [{status}]\n'
        messagebox.showinfo("Tasks", tasks_list)

def mark_task_completed(task_index):
    try:
        tasks[task_index]["completed"] = True
        messagebox.showinfo("Success", f'Marked task as completed: {tasks[task_index]["task"]}')
    except IndexError:
        messagebox.showerror("Error", "Invalid task number")

def show_help():
    help_text = """
    Available commands:
    - Add Task: Add a new task
    - Delete Task: Delete a task by its number
    - View Tasks: View all tasks
    - Mark Complete: Mark a task as completed
    - Exit: Exit the application
    """
    messagebox.showinfo("Help", help_text)

def add_task_window():
    def save_task():
        task = entry_task.get()
        add_task(task)
        add_task_win.destroy()

    add_task_win = tk.Toplevel(app)
    add_task_win.title("Add Task")
    add_task_win.geometry("300x200")

    tk.Label(add_task_win, text="Task:").pack(pady=10)
    entry_task = tk.Entry(add_task_win)
    entry_task.pack(pady=10)

    tk.Button(add_task_win, text="Add Task", command=save_task).pack(pady=10)

def delete_task_window():
    def delete_task_by_index():
        task_index = int(entry_task_index.get()) - 1
        delete_task(task_index)
        delete_task_win.destroy()

    delete_task_win = tk.Toplevel(app)
    delete_task_win.title("Delete Task")
    delete_task_win.geometry("300x200")

    tk.Label(delete_task_win, text="Task Number:").pack(pady=10)
    entry_task_index = tk.Entry(delete_task_win)
    entry_task_index.pack(pady=10)

    tk.Button(delete_task_win, text="Delete Task", command=delete_task_by_index).pack(pady=10)

def mark_task_completed_window():
    def mark_task_completed_by_index():
        task_index = int(entry_task_index.get()) - 1
        mark_task_completed(task_index)
        mark_task_completed_win.destroy()

    mark_task_completed_win = tk.Toplevel(app)
    mark_task_completed_win.title("Mark Task Completed")
    mark_task_completed_win.geometry("300x200")

    tk.Label(mark_task_completed_win, text="Task Number:").pack(pady=10)
    entry_task_index = tk.Entry(mark_task_completed_win)
    entry_task_index.pack(pady=10)

    tk.Button(mark_task_completed_win, text="Mark Completed", command=mark_task_completed_by_index).pack(pady=10)

app = tk.Tk()
app.title("Task Manager")
app.geometry("400x300")

tk.Label(app, text="Task Manager Application").pack(pady=10)

tk.Button(app, text="Add Task", command=add_task_window).pack(pady=10)
tk.Button(app, text="Delete Task", command=delete_task_window).pack(pady=10)
tk.Button(app, text="View Tasks", command=view_tasks).pack(pady=10)
tk.Button(app, text="Mark Complete", command=mark_task_completed_window).pack(pady=10)
tk.Button(app, text="Help", command=show_help).pack(pady=10)
tk.Button(app, text="Exit", command=app.quit).pack(pady=10)

app.mainloop()
