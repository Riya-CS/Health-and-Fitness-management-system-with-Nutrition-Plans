# Please change the file path accordingly
import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
import mysql.connector
import sys, subprocess
import pop_ups

global username
username = sys.argv[1] if len(sys.argv) > 1 else "User"


def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your password",
        database="health_fitness"
    )


def load_user_details():
  
    conn = connect_db()
    cursor = conn.cursor()

  
    cursor.execute("SELECT * FROM UserProfile WHERE username = %s", (username,))
    user = cursor.fetchone()

    if user:
        
        name_entry.delete(0, tk.END)
        name_entry.insert(0, user[0])  
        gender_var.set(user[3])  
        age_entry.delete(0, tk.END)
        age_entry.insert(0, user[2])  
        spec_var.set(user[3])  
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, user[4])  
    else:
        
        name_entry.delete(0, tk.END)
        gender_var.set("Male")  
        age_entry.delete(0, tk.END)
        spec_var.set("")  
        phone_entry.delete(0, tk.END)

    conn.close()

def save_trainer():
    name = name_entry.get()
    gender = gender_var.get()
    age = age_entry.get()
    specialization = spec_var.get()
    phone = phone_entry.get()


    if not name or not gender or not age or not specialization or not phone:
        pop_ups.popup_message("All fields must be filled out.","Error")
        return


    try:
        age = int(age)
        if age < 1 or age > 99:
            raise ValueError
    except ValueError:
        pop_ups.popup_message( "Age must be a number between 1 and 99.","Error")
        return

    if age < 18:
        pop_ups.popup_message( "Only users over 18 are allowed.","Error")
        return


    if len(phone) != 10 or not phone.isdigit():
        pop_ups.popup_message( "Phone number must be exactly 10 digits.","Error")
        return

 
    conn = connect_db()
    cursor = conn.cursor()


    cursor.execute("SELECT * FROM UserProfile WHERE username = %s", (username,))
    user = cursor.fetchone()
    print(user)

    if user:

        cursor.execute('''
            UPDATE UserProfile
            SET name = %s, gender = %s, age = %s, specialization = %s, phoneno = %s
            WHERE username = %s
        ''', (name, gender, age, specialization, phone, username))
        pop_ups.popup_message("User details updated successfully!","Success")
    else:

        cursor.execute('''
            INSERT INTO UserProfile (username, name, gender, age, specialization, phoneno)
            VALUES (%s, %s, %s, %s, %s, %s)
        ''', (username, name, gender, age, specialization, phone))
        pop_ups.popup_message("New user added successfully!", "Success")



    conn.commit()
    conn.close()

    disable_fields()  


def enable_editing():
    name_entry.config(state="normal")
    age_entry.config(state="normal")
    phone_entry.config(state="normal")
    gender_dropdown.config(state="normal")
    for rb in spec_radiobuttons:
        rb.config(state="normal")

    edit_button.config(state="disabled")  


def disable_fields():
    name_entry.config(state="disabled")
    age_entry.config(state="disabled")
    phone_entry.config(state="disabled")
    gender_dropdown.config(state="disabled")
    for rb in spec_radiobuttons:
        rb.config(state="disabled")

    edit_button.config(state="normal")  

def on_close():
    try:
        
        print("from here")
        next_script_path = r"C:\Users\hicha\OneDrive\Desktop\DBMSSSS\DBMS_Project_code\User_dashboard.py"  # Replace with the actual path
        subprocess.Popen(['python', next_script_path, username])  
    except Exception as e:
        pop_ups.popup_message("Error", f"Failed to open the next script: {e}")
    finally:
        root.destroy()  


root = tk.Tk()
root.title("User Details")


window_width = 1572
window_height = 770
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


x = (screen_width // 2) - (window_width // 2)
y = 0


root.geometry(f"{window_width}x{window_height}+{x}+{y}")


root.configure(bg="#82BBB5")

bg_image = tk.PhotoImage(file=r"C:\Users\hicha\OneDrive\Desktop\DBMSSSS\DBMS_Project_code\build\assets\image_234.png")  # Replace with your image file


bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1) 


font_otomanopee_h = tkFont.Font(family="Otomanopee One", size=30)
font_otomanopee = tkFont.Font(family="Otomanopee One", size=16)
font_otomanopee1 = tkFont.Font(family="Otomanopee One", size=13)

canvas = tk.Canvas(root, bg="#E7F2D6", bd=0, highlightthickness=0)
canvas.place(x=450, y=50, width=800, height=700)  


tk.Label(root, text="User Profile", bg="#E7F2D6", fg="#3C98A4", font=font_otomanopee_h).place(x=700, y=100)


tk.Label(root, text="Name                   ", bg="#82BBB5", fg="#E7F2D6", font=font_otomanopee).place(x=520, y=230)
name_entry = tk.Entry(root, font=font_otomanopee, fg="#82BBB5")
name_entry.place(x=810, y=230, width=200)

tk.Label(root, text="Gender                 ", bg="#82BBB5", fg="#E7F2D6", font=font_otomanopee).place(x=520, y=280)
gender_var = tk.StringVar()
gender_var.set("Male")  # Default value
gender_dropdown = tk.OptionMenu(root, gender_var, "Male", "Female", "Transgender", "Prefer not to say")
gender_dropdown.config(font=font_otomanopee, fg="#82BBB5")
gender_dropdown.place(x=810, y=280, width=200)

tk.Label(root, text="Age                      ", bg="#82BBB5", fg="#E7F2D6", font=font_otomanopee).place(x=520, y=340)
age_entry = tk.Entry(root, font=font_otomanopee, fg="#82BBB5")
age_entry.place(x=810, y=340, width=200)

tk.Label(root, text="Specialization        ", bg="#82BBB5", fg="#E7F2D6", font=font_otomanopee).place(x=520, y=400)
spec_var = tk.StringVar()
spec_var.set("")
spec_radiobuttons = [
    tk.Radiobutton(root, text="Cardio Fitness", variable=spec_var, value="Cardio Fitness Trainer", bg="#82BBB5", fg="#E7F2D6", font=font_otomanopee1, selectcolor="#FF6347", indicatoron=False),
    tk.Radiobutton(root, text="HIIT", variable=spec_var, value="HIIT Trainer", bg="#82BBB5", fg="#E7F2D6", font=font_otomanopee1, selectcolor="#FF6347", indicatoron=False),
    tk.Radiobutton(root, text="Strength Training", variable=spec_var, value="Strength Training Expert", bg="#82BBB5", fg="#E7F2D6", font=font_otomanopee1, selectcolor="#FF6347", indicatoron=False),
    tk.Radiobutton(root, text="Weight Loss", variable=spec_var, value="Weight Loss Coach", bg="#82BBB5", fg="#E7F2D6", font=font_otomanopee1, selectcolor="#FF6347", indicatoron=False),
    tk.Radiobutton(root, text="Yoga and Flexibility", variable=spec_var, value="Yoga and Flexibility Trainer", bg="#82BBB5", fg="#E7F2D6", font=font_otomanopee1, selectcolor="#FF6347", indicatoron=False)
]


spec_radiobuttons[0].place(x=810, y=400)
spec_radiobuttons[1].place(x=1015, y=400)
spec_radiobuttons[2].place(x=810, y=450)
spec_radiobuttons[3].place(x=1015, y=450)
spec_radiobuttons[4].place(x=810, y=500)


tk.Label(root, text="Phone Number       ", bg="#82BBB5", fg="#E7F2D6", font=font_otomanopee).place(x=520, y=580)
phone_entry = tk.Entry(root, font=font_otomanopee, fg="#82BBB5")
phone_entry.place(x=810, y=580, width=200)


save_button = tk.Button(root, text="Save", font=font_otomanopee, fg="#E7F2D6", bg="#82BBB5", command=save_trainer)
save_button.place(x=800, y=680,width=100)

edit_button = tk.Button(root, text="Edit", font=font_otomanopee, fg="#E7F2D6", bg="#82BBB5", command=enable_editing)
edit_button.place(x=680, y=680,width=100)


close_button = tk.Button(root, text="Close", font=font_otomanopee, fg="#E7F2D6", bg="#82BBB5", command=on_close)
close_button.place(x=920, y=680,width=100)


load_user_details()


disable_fields()


root.mainloop()
#perfect
