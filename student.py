import tkinter as tk
from tkinter import messagebox, font
from PIL import Image, ImageTk

class Student:
    def __init__(self, student_id, name, grade, age):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.age = age

    def display_info(self):
        return f"ID: {self.student_id}, Name: {self.name}, Grade: {self.grade}, Age: {self.age}"

students = {}

def add_student():
    student_id = entry_student_id.get()
    name = entry_name.get()
    grade = entry_grade.get()
    age = entry_age.get()

    if student_id and name and grade and age:
        students[student_id] = Student(student_id, name, grade, age)
        messagebox.showinfo("Success", "Student added successfully!")
    else:
        messagebox.showerror("Error", "All fields are required!")
    clear_entries()

def update_student():
    student_id = entry_student_id.get()
    if student_id in students:
        students[student_id].name = entry_name.get()
        students[student_id].grade = entry_grade.get()
        students[student_id].age = entry_age.get()
        messagebox.showinfo("Success", "Student updated successfully!")
    else:
        messagebox.showerror("Error", "Student not found!")
    clear_entries()

def delete_student():
    student_id = entry_student_id.get()
    if student_id in students:
        del students[student_id]
        messagebox.showinfo("Success", "Student deleted successfully!")
    else:
        messagebox.showerror("Error", "Student not found!")
    clear_entries()

def display_student():
    student_id = entry_student_id.get()
    if student_id in students:
        info = students[student_id].display_info()
        messagebox.showinfo("Student Info", info)
    else:
        messagebox.showerror("Error", "Student not found!")
    clear_entries()

def clear_entries():
    entry_student_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_grade.delete(0, tk.END)
    entry_age.delete(0, tk.END)

app = tk.Tk()
app.title("Student Record Management System")
app.geometry("600x600")

app.configure(bg="#f0f0f0")
app.configure(bg="#ADD8E6")

header_font = font.Font(family="Helvetica", size=20, weight="bold")
label_font = font.Font(family="Helvetica", size=14)
button_font = font.Font(family="Helvetica", size=12, weight="bold")

tk.Label(app, text="Student Record Management", font=header_font, bg="#f0f0f0", fg="#333").pack(pady=20)

frame = tk.Frame(app, bg="#f0f0f0")
frame.pack(pady=20)

tk.Label(frame, text="Student ID:", font=label_font, bg="#f0f0f0", fg="#333").grid(row=0, column=0, sticky="w", pady=10, padx=20)
entry_student_id = tk.Entry(frame, font=label_font)
entry_student_id.grid(row=0, column=1, pady=10, padx=20)

tk.Label(frame, text="Name:", font=label_font, bg="#f0f0f0", fg="#333").grid(row=1, column=0, sticky="w", pady=10, padx=20)
entry_name = tk.Entry(frame, font=label_font)
entry_name.grid(row=1, column=1, pady=10, padx=20)

tk.Label(frame, text="Grade:", font=label_font, bg="#f0f0f0", fg="#333").grid(row=2, column=0, sticky="w", pady=10, padx=20)
entry_grade = tk.Entry(frame, font=label_font)
entry_grade.grid(row=2, column=1, pady=10, padx=20)

tk.Label(frame, text="Age:", font=label_font, bg="#f0f0f0", fg="#333").grid(row=3, column=0, sticky="w", pady=10, padx=20)
entry_age = tk.Entry(frame, font=label_font)
entry_age.grid(row=3, column=1, pady=10, padx=20)

tk.Button(frame, text="Add Student", command=add_student, font=button_font, bg="#4CAF50", fg="#fff", relief="raised", bd=2).grid(row=4, column=0, pady=20, padx=20)
tk.Button(frame, text="Update Student", command=update_student, font=button_font, bg="#2196F3", fg="#fff", relief="raised", bd=2).grid(row=4, column=1, pady=20, padx=20)
tk.Button(frame, text="Delete Student", command=delete_student, font=button_font, bg="#FF5722", fg="#fff", relief="raised", bd=2).grid(row=4, column=2, pady=20, padx=20)
tk.Button(frame, text="Display Student", command=display_student, font=button_font, bg="#9C27B0", fg="#fff", relief="raised", bd=2).grid(row=5, column=0, pady=20, padx=20)

app.mainloop()
