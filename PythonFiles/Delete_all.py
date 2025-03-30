# Please change the file path accordingly
import mysql.connector
import pop_ups
from pathlib import Path
import sys
from tkinter import *

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
import mysql.connector
import subprocess

global username
username = sys.argv[1] if len(sys.argv) > 1 else "User"

def delete_user_data(username):
    try:
        
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your password",
            database="health_fitness"
        )
        cursor = conn.cursor()

        
        tables_to_delete = [
            "UserProfile",
            "Workout",
            "NutritionLog",
            "HealthMetrics",
            "GoalsAndProgress",
            "User"
        ]

        
        for table in tables_to_delete:
            cursor.execute(f"DELETE FROM {table} WHERE Username = %s", (username,))
            print(f"Deleted records from {table} where Username = {username}")

        
        conn.commit()

        return(f"All data for Username = {username} has been deleted.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def setup_triggers():


    trigger_script_path = r"C:\Users\hicha\OneDrive\Desktop\DBMSSSS\DBMS_Project_code\Triggers.py"
    try:
        
        result = subprocess.run(
            ["python", trigger_script_path, username],
            capture_output=True,
            text=True
        )
        
        
        print("Subprocess STDOUT:", result.stdout)
        print("Subprocess STDERR:", result.stderr)

        if result.returncode == 0:
            print("Triggers re-created successfully.")
        else:
            print(f"Triggers script exited with errors (code {result.returncode}).")

    except Exception as e:
        print(f"Error running subprocess: {e}")

    try:
        
        subprocess.run(["python",r"C:\Users\hicha\OneDrive\Desktop\DBMSSSS\DBMS_Project_code\Triggers.py" ,username], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("Triggers re-created successfully.")
        else:
            print("Error while re-creating triggers:", result.stderr)

    except Exception as e:
        print(f"Error running subprocess: {e}")

from tkinter import Tk, Label, Button, messagebox, Frame



def confirm_delete_user():
    if not username:
        pop_ups.popup_message( "Please enter a username.")
        return

    confirm = messagebox.askyesno(
        "Confirm Deletion",
        f"Are you sure you want to permanently delete all data for user '{username}'?\nThis action cannot be undone."
    )

    if confirm:
        success = delete_user_data(username)
        print("here",success)
        setup_triggers()
        if success:
            pop_ups.popup_message("Success", f"All data for user '{username}' has been deleted.")
            
    else:
        pop_ups.popup_message("User data deletion was cancelled.")



def create_main_window():
    window = Tk()
    window.title("Delete User Data")

    
    window_width = 600
    window_height = 300

    
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    window.configure(bg="#CAE2CC")

    
    header_frame = Frame(window, bg="#CAE2CC", height=60)
    header_frame.pack(fill="x")
    header_label = Label(
        header_frame, text="Delete User Data", font=("Otomanopee one", 18, "bold"), bg="#CAE2CC", fg="#3C98A4"
    )
    header_label.pack(pady=10)

    
    content_frame = Frame(window, bg="#CAE2CC", padx=20, pady=20)
    content_frame.pack(expand=True, fill="both")

    
    info_label = Label(
        content_frame,
        text="This tool will permanently delete all data associated with a user.\nPlease proceed with caution.",
        font=("Otomanopee one", 12), bg="#CAE2CC", fg="#333333", justify="center"
    )
    info_label.pack(pady=(0, 20))

    # Buttons
    delete_button = Button(
        content_frame, text="Delete User", font=("Otomanopee one", 14, "bold"),
        bg="#D9534F", fg="white", activebackground="#C9302C", activeforeground="white",
        command=confirm_delete_user
    )
    delete_button.pack(pady=(10, 20), ipadx=10, ipady=5)

    exit_button = Button(
        content_frame, text="Exit", font=("Otomanopee one", 12),
        bg="#5BC0DE", fg="white", activebackground="#31B0D5", activeforeground="white",
        command=window.destroy
    )
    exit_button.pack(pady=(0, 10), ipadx=10, ipady=5)

    window.mainloop()



create_main_window()
