import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
from pathlib import Path

# Sample data to populate the workout table
sample_workouts = [
    {"WorkoutType": "Running", "Duration": 30, "CaloriesBurned": 300, "Date": "2024-10-05"},
    {"WorkoutType": "Cycling", "Duration": 45, "CaloriesBurned": 450, "Date": "2024-10-10"},
]

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame5")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class WorkoutApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Workout Tracker")
        self.root.geometry("1536x806")
        self.root.configure(bg="#FFFFFF")

        # Canvas
        self.canvas = tk.Canvas(self.root, bg="#FFFFFF", height=806, width=1536, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        # Background Image
        self.image_image_1 = tk.PhotoImage(file=relative_to_assets("image_1.png"))
        self.canvas.create_image(768.0, 403.0, image=self.image_image_1)

        # Title Label
        tk.Label(self.root, text="Workout Tracker", font=("Helvetica", 16, "bold"), bg="#FFFFFF").pack(pady=10)

        # Table Frame
        table_frame = tk.Frame(self.root, bg="#FFFFFF")
        table_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Treeview Table
        columns = ("WorkoutType", "Duration", "CaloriesBurned", "Date")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=100)
        self.tree.pack(fill="both", expand=True)

        # Add sample data to the table
        for workout in sample_workouts:
            self.tree.insert("", "end", values=(workout["WorkoutType"], workout["Duration"], workout["CaloriesBurned"], workout["Date"]))

        # Buttons Frame
        btn_frame = tk.Frame(self.root, bg="#FFFFFF")
        btn_frame.pack(pady=10)

        # Add buttons with images
        self.add_button_with_image(btn_frame, "Log New Workout", "button_1.png", self.open_add_workout_form)
        self.add_button_with_image(btn_frame, "Edit Selected Workout", "button_2.png", self.open_edit_workout_form)
        self.add_button_with_image(btn_frame, "Delete Selected Workout", "button_3.png", self.delete_workout)

    def add_button_with_image(self, frame, text, image_filename, command):
        button_image = tk.PhotoImage(file=relative_to_assets(image_filename))
        button = tk.Button(frame, image=button_image, borderwidth=0, highlightthickness=0, command=command, relief="flat")
        button.image = button_image  # Keep reference to the image to prevent it from being garbage collected
        button.pack(side="left", padx=5)

    def open_add_workout_form(self):
        self.open_workout_form("Log New Workout")

    def open_edit_workout_form(self):
        selected = self.tree.focus()
        if selected:
            workout_data = self.tree.item(selected)["values"]
            self.open_workout_form("Edit Workout", workout_data)
        else:
            messagebox.showwarning("Warning", "Please select a workout to edit")

    def open_workout_form(self, title, workout_data=None):
        # Workout Form Popup
        form = tk.Toplevel(self.root)
        form.title(title)
        form.geometry("300x300")

        # Form Labels and Entries
        tk.Label(form, text="Workout Type:").pack(pady=5)
        workout_type_entry = ttk.Combobox(form, values=["Running", "Cycling", "Swimming", "Yoga"], state="readonly")
        workout_type_entry.pack()
        if workout_data:
            workout_type_entry.set(workout_data[0])

        tk.Label(form, text="Duration (minutes):").pack(pady=5)
        duration_entry = tk.Entry(form, width=30)
        duration_entry.pack()
        if workout_data:
            duration_entry.insert(0, workout_data[1])

        tk.Label(form, text="Calories Burned:").pack(pady=5)
        calories_entry = tk.Entry(form, width=30)
        calories_entry.pack()
        if workout_data:
            calories_entry.insert(0, workout_data[2])

        tk.Label(form, text="Date:").pack(pady=5)
        date_entry = tk.Entry(form, width=30)
        date_entry.pack()
        date_entry.insert(0, date.today() if not workout_data else workout_data[3])

        # Save Button
        save_btn = tk.Button(form, text="Save", command=lambda: self.save_workout(form, workout_type_entry.get(), duration_entry.get(), calories_entry.get(), date_entry.get()))
        save_btn.pack(pady=10)

    def save_workout(self, form, workout_type, duration, calories, workout_date):
        if not workout_type or not duration or not calories or not workout_date:
            messagebox.showwarning("Warning", "Please fill in all fields")
            return
        self.tree.insert("", "end", values=(workout_type, duration, calories, workout_date))
        form.destroy()

    def delete_workout(self):
        selected = self.tree.selection()
        if selected:
            self.tree.delete(selected)
        else:
            messagebox.showwarning("Warning", "Please select a workout to delete")

if __name__ == "__main__":
    window = tk.Tk()
    app = WorkoutApp(window)
    window.mainloop()
