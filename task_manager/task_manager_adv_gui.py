import sys
import json
import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, font

tasks = []

def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            global tasks
            tasks = json.load(file)

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task_gui(task, priority='Medium'):
    tasks.append({"task": task, "completed": False, "created_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "completed_at": None, "priority": priority})
    messagebox.showinfo("Success", f'Added task: {task} with priority: {priority}')
    save_tasks()
    view_tasks_gui()

def delete_task_gui(task_index):
    try:
        removed_task = tasks.pop(task_index)
        messagebox.showinfo("Success", f'Deleted task: {removed_task["task"]}')
        save_tasks()
        view_tasks_gui()
    except IndexError:
        messagebox.showerror("Error", "Invalid task number")

def view_tasks_gui():
    for widget in frame_tasks.winfo_children():
        widget.destroy()
    if not tasks:
        lbl_no_tasks = tk.Label(frame_tasks, text="No tasks available", font=label_font, bg="#e0f7fa", fg="#333")
        lbl_no_tasks.pack()
    else:
        for i, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"
            task_info = f'{i + 1}. {task["task"]} [{status}] (Priority: {task["priority"]}, Created: {task["created_at"]}, Completed: {task["completed_at"]})'
            lbl_task = tk.Label(frame_tasks, text=task_info, font=label_font, bg="#e0f7fa", fg="#333")
            lbl_task.pack()
            
def mark_task_completed_gui(task_index):
    try:
        tasks[task_index]["completed"] = True
        tasks[task_index]["completed_at"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        messagebox.showinfo("Success", f'Marked task as completed: {tasks[task_index]["task"]}')
        save_tasks()
        view_tasks_gui()
    except IndexError:
        messagebox.showerror("Error", "Invalid task number")

def mark_task_incomplete_gui(task_index):
    try:
        tasks[task_index]["completed"] = False
        tasks[task_index]["completed_at"] = None
        messagebox.showinfo("Success", f'Marked task as incomplete: {tasks[task_index]["task"]}')
        save_tasks()
        view_tasks_gui()
    except IndexError:
        messagebox.showerror("Error", "Invalid task number")

def add_task_window():
    def save_task():
        task = entry_task.get()
        priority = priority_var.get()
        add_task_gui(task, priority)
        add_task_win.destroy()

    add_task_win = tk.Toplevel(app)
    add_task_win.title("Add Task")
    add_task_win.geometry("500x400")
    add_task_win.configure(bg="#e0f7fa")

    tk.Label(add_task_win, text="Task:", font=label_font, bg="#e0f7fa", fg="#333").pack(pady=10)
    entry_task = tk.Entry(add_task_win, font=label_font)
    entry_task.pack(pady=10)

    tk.Label(add_task_win, text="Priority:", font=label_font, bg="#e0f7fa", fg="#333").pack(pady=10)
    priority_var = tk.StringVar(value="Medium")
    tk.Radiobutton(add_task_win, text="Low", variable=priority_var, value="Low", font=label_font, bg="#e0f7fa", fg="#333").pack()
    tk.Radiobutton(add_task_win, text="Medium", variable=priority_var, value="Medium", font=label_font, bg="#e0f7fa", fg="#333").pack()
    tk.Radiobutton(add_task_win, text="High", variable=priority_var, value="High", font=label_font, bg="#e0f7fa", fg="#333").pack()

    tk.Button(add_task_win, text="Add Task", command=save_task, font=button_font, bg="#4CAF50", fg="#fff", relief="raised", bd=2).pack(pady=20)

app = tk.Tk()
app.title("Task Manager")
app.geometry("800x700")  # Increased size of the window
app.configure(bg="#e0f7fa")

header_font = font.Font(family="Helvetica", size=24, weight="bold", slant="italic")
label_font = font.Font(family="Helvetica", size=16, weight="bold", slant="italic")
button_font = font.Font(family="Helvetica", size=14, weight="bold", slant="italic")

tk.Label(app, text="Task Manager", font=header_font, bg="#e0f7fa", fg="#333").pack(pady=20)

frame_buttons = tk.Frame(app, bg="#e0f7fa")
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Add Task", command=add_task_window, font=button_font, bg="#4CAF50", fg="#fff", relief="raised", bd=2).pack(side=tk.LEFT, padx=10)
tk.Button(frame_buttons, text="View Tasks", command=view_tasks_gui, font=button_font, bg="#2196F3", fg="#fff", relief="raised", bd=2).pack(side=tk.LEFT, padx=10)
tk.Button(frame_buttons, text="Mark Complete", command=lambda: mark_task_completed_gui(task_index.get()-1), font=button_font, bg="#FF5722", fg="#fff", relief="raised", bd=2).pack(side=tk.LEFT, padx=10)
tk.Button(frame_buttons, text="Mark Incomplete", command=lambda: mark_task_incomplete_gui(task_index.get()-1), font=button_font, bg="#FFC107", fg="#fff", relief="raised", bd=2).pack(side=tk.LEFT, padx=10)
tk.Button(frame_buttons, text="Delete Task", command=lambda: delete_task_gui(task_index.get()-1), font=button_font, bg="#D32F2F", fg="#fff", relief="raised", bd=2).pack(side=tk.LEFT, padx=10)
tk.Button(frame_buttons, text="Exit", command=app.quit, font=button_font, bg="#9C27B0", fg="#fff", relief="raised", bd=2).pack(side=tk.LEFT, padx=10)

tk.Label(app, text="Task Index:", font=label_font, bg="#e0f7fa", fg="#333").pack(pady=10)
task_index = tk.IntVar()
tk.Entry(app, textvariable=task_index, font=label_font).pack(pady=10)

frame_tasks = tk.Frame(app, bg="#e0f7fa")
frame_tasks.pack(pady=20, fill=tk.BOTH, expand=True)

view_tasks_gui()

app.mainloop()
