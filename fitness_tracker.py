import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import font
from datetime import datetime

class Workout:
    def __init__(self, date, exercise_type, duration, calories_burned):
        self.date = date
        self.exercise_type = exercise_type
        self.duration = duration
        self.calories_burned = calories_burned

    def __str__(self):
        return f"{self.date}: {self.exercise_type} for {self.duration} minutes, {self.calories_burned} calories burned"

class User:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.workouts = []

    def add_workout(self, workout):
        self.workouts.append(workout)

    def view_workouts(self):
        return "\n".join(str(workout) for workout in self.workouts)

    def save_data(self, filename):
        with open(filename, 'w') as file:
            for workout in self.workouts:
                file.write(f"{workout.date},{workout.exercise_type},{workout.duration},{workout.calories_burned}\n")

    def load_data(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                date, exercise_type, duration, calories_burned = line.strip().split(',')
                workout = Workout(date, exercise_type, int(duration), int(calories_burned))
                self.workouts.append(workout)

class WorkoutApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Workout Tracker")
        self.root.geometry("500x600")
        self.root.configure(bg='#ADD8E6')  # Background color

        self.user = None

        # Title Label
        title_font = font.Font(family='Helvetica', size=18, weight='bold')
        title_label = tk.Label(root, text="Workout Tracker", bg='#ADD8E6', font=title_font)
        title_label.pack(pady=10)

        # User Info Frame
        user_info_frame = tk.Frame(root, bg='#ADD8E6')
        user_info_frame.pack(pady=10)

        tk.Label(user_info_frame, text="Name:", bg='#ADD8E6').grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(user_info_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(user_info_frame, text="Age:", bg='#ADD8E6').grid(row=1, column=0, padx=5, pady=5)
        self.age_entry = tk.Entry(user_info_frame)
        self.age_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(user_info_frame, text="Weight:", bg='#ADD8E6').grid(row=2, column=0, padx=5, pady=5)
        self.weight_entry = tk.Entry(user_info_frame)
        self.weight_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(user_info_frame, text="Create User", command=self.create_user).grid(row=3, columnspan=2, pady=10)

        # Workout Frame
        workout_frame = tk.Frame(root, bg='#ADD8E6')
        workout_frame.pack(pady=10)

        tk.Label(workout_frame, text="Date (YYYY-MM-DD):", bg='#ADD8E6').grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = tk.Entry(workout_frame)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(workout_frame, text="Exercise Type:", bg='#ADD8E6').grid(row=1, column=0, padx=5, pady=5)
        self.exercise_type_entry = tk.Entry(workout_frame)
        self.exercise_type_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(workout_frame, text="Duration (minutes):", bg='#ADD8E6').grid(row=2, column=0, padx=5, pady=5)
        self.duration_entry = tk.Entry(workout_frame)
        self.duration_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(workout_frame, text="Calories Burned:", bg='#ADD8E6').grid(row=3, column=0, padx=5, pady=5)
        self.calories_burned_entry = tk.Entry(workout_frame)
        self.calories_burned_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Button(workout_frame, text="Add Workout", command=self.add_workout).grid(row=4, columnspan=2, pady=10)

        # View Workouts Frame
        view_frame = tk.Frame(root, bg='#ADD8E6')
        view_frame.pack(pady=10)
        tk.Button(view_frame, text="View Workouts", command=self.view_workouts).pack()
        self.workouts_text = tk.Text(view_frame, height=10, width=50)
        self.workouts_text.pack(pady=10)

        # Save/Load Frame
        save_load_frame = tk.Frame(root, bg='#ADD8E6')
        save_load_frame.pack(pady=10)
        tk.Button(save_load_frame, text="Save Data", command=self.save_data).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(save_load_frame, text="Load Data", command=self.load_data).grid(row=0, column=1, padx=5, pady=5)

    def create_user(self):
        name = self.name_entry.get()
        age = int(self.age_entry.get())
        weight = float(self.weight_entry.get())
        self.user = User(name, age, weight)
        messagebox.showinfo("User Created", f"User {name} created successfully!")

    def add_workout(self):
        date = self.date_entry.get()
        exercise_type = self.exercise_type_entry.get()
        duration = int(self.duration_entry.get())
        calories_burned = int(self.calories_burned_entry.get())
        workout = Workout(date, exercise_type, duration, calories_burned)
        self.user.add_workout(workout)
        messagebox.showinfo("Workout Added", "Workout added successfully!")

    def view_workouts(self):
        self.workouts_text.delete(1.0, tk.END)
        workouts = self.user.view_workouts()
        self.workouts_text.insert(tk.END, workouts)

    def save_data(self):
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if filename:
            self.user.save_data(filename)
            messagebox.showinfo("Data Saved", "Data saved successfully!")

    def load_data(self):
        filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if filename:
            self.user.load_data(filename)
            messagebox.showinfo("Data Loaded", "Data loaded successfully!")
            self.view_workouts()

if __name__ == "__main__":
    root = tk.Tk()
    app = WorkoutApp(root)
    root.mainloop()
