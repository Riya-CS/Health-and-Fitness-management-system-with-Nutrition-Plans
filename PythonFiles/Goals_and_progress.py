﻿from pathlib import Path
import sys
import mysql.connector
from datetime import datetime
import subprocess
from db_config import DB_CONFIG

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label, OptionMenu, StringVar


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).parent.parent / 'build/assets/frame3'

def open_del(filename,username, delay=8000):
    script_path = OUTPUT_PATH / filename
    subprocess.Popen(['python', str(script_path), username])
    window.after(delay, window.destroy)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_file_with_delay(filename,username, delay=2000):
    script_path = OUTPUT_PATH / filename
    subprocess.Popen(['python', str(script_path), username])
    window.after(delay, window.destroy)

global username
username = sys.argv[1] if len(sys.argv) > 1 else "User"


def get_goals_and_progress():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT Goal, Target, Status, Date ,ReportID
        FROM GoalsAndProgress 
        WHERE Username = %s
        ORDER BY ReportID DESC LIMIT 5
        """, (username,))
        result = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return result
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def display_goals_and_progress():
    goals = get_goals_and_progress()
    if goals:
        goals_text = "-" * 70 + "\n"
        goals_text += (f"| ReportID | Goal\t\t| Target\t\t| Status\t| Date\n")
        goals_text += "-" * 70 + "\n"
        for goal in goals:
            if goal[2]=='Pending':
                goals_text += (f"| {goal[4]}\t | {goal[0]}\t| {goal[1]}\t| {goal[2]}\t\t| {goal[3]}\t|\n")
            else:
                goals_text += (f"| {goal[4]}\t | {goal[0]}\t| {goal[1]}\t| {goal[2]}\t| {goal[3]}\t|\n")
        goals_text += "-" * 70 + "\n"
    else:
        goals_text = "No goals or progress data available for the user."

     
    y_position = 560 + (len(goals) * 20) if goals else 590  

    
    canvas.delete("goals_text")
    canvas.create_text(
        500.0, y_position-80,
        text="Your Goals-",
        fill="#a5bf63",
        font=("Otomanopee One", 16),
        tags="goals_text"
    )

    canvas.create_text(
        900.0, y_position,
        text=goals_text,
        fill="#3C98A4",
        font=("Otomanopee One", 12),
        anchor="center",
        tags="goals_text"
    )


def submit_goal():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        goal = entry_goal.get()
        target = entry_target.get()
        status = status_var.get()
        date = datetime.now().date()    
        
        if not goal:
            print("Goal field is required.")
            return

        cursor.execute("""
        INSERT INTO GoalsAndProgress (Username, Goal, Target, Status, Date)
        VALUES (%s, %s, %s, %s, %s)
        """, (username, goal, target, status, date))
        conn.commit()
        cursor.close()
        conn.close()

        print("Goal successfully added.")
        entry_goal.delete(0, 'end')
        entry_target.delete(0, 'end')

        
        display_goals_and_progress()

    except mysql.connector.Error as err:
        print(f"Error: {err}")



window = Tk()

window.geometry("1536x806+0+0")
window.configure(bg = "#FFFFFF")



canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 806,
    width = 1536,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    768.0,
    496.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    768.0,
    496.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    916.0,
    103.0,
    image=image_image_3
)


canvas.create_text(
    528.0,
    60.0,
    anchor="nw",
    text="GOALS AND PROGRESS",
    fill="#84A928",
    font=("Otomanopee One", 64 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    916.0,
    508.0,
    image=image_image_4
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
    background="#3C98A4"
)
button_1.place(
    x=103.0,
    y=13.0,
    width=180.0,
    height=188.51348876953125
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    196.0,
    508.0,
    image=image_image_5
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_file_with_delay("Health_metrics.py",username),
    relief="flat",
    background="#CAE2CC"
)
button_2.place(
    x=88.769287109375,
    y=333.84423828125,
    width=214.46151733398438,
    height=72.76707458496094
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat",
    background="#CAE2CC"
)
button_3.place(
    x=88.769287109375,
    y=416.3134765625,
    width=214.46151733398438,
    height=72.76707458496094
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:open_file_with_delay("Nutrition_plans.py",username),
    relief="flat",
    background="#CAE2CC"
)
button_4.place(
    x=88.769287109375,
    y=589.984375,
    width=214.4615478515625,
    height=72.76707458496094
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_file_with_delay("User_dashboard.py",username),
    relief="flat",
    background="#CAE2CC"
)
button_5.place(
    x=88.769287109375,
    y=254.285400390625,
    width=214.46151733398438,
    height=72.76707458496094
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:open_file_with_delay("Workouts.py",username),
    relief="flat",
    background="#CAE2CC"
)
button_6.place(
    x=88.769287109375,
    y=500.723388671875,
    width=214.46151733398438,
    height=72.76707458496094
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:open_file_with_delay("User_profile.py",username),
    relief="flat",
    background="#CAE2CC"
)
button_7.place(
    x=89.0,
    y=680.0,
    width=95.0,
    height=88.0
)
#delete
button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_del("Delete_all.py",username),
    relief="flat",
    background="#CAE2CC"
)
button_8.place(
    x=196.0,
    y=680.0,
    width=95.0,
    height=88.0
)


image_image_5 = PhotoImage(
    file=relative_to_assets(r"C:\Users\hicha\OneDrive\Desktop\DBMSSSS\DBMS_Project_code\build\assets\frame4\image_5.png"))
image_5 = canvas.create_image(
    195.0,
    510.0,
    image=image_image_5
)
image_image_image = PhotoImage(
    file=relative_to_assets(r"C:\Users\hicha\OneDrive\Desktop\DBMSSSS\DBMS_Project_code\build\assets\frame0\image_5.png"))
image_5 = canvas.create_image(
    915.0,
    630.0,
    image=image_image_image
)



display_goals_and_progress()


label_goal = Label(window, text="Goal:", font=("Otomanopee One", 20), fg='#84A928',bg="#FFFFFF")
label_goal.place(x=550, y=300)
entry_goal = Entry(window, font=("Otomanopee One", 16), width=30,bg="#d6e8ad",
    fg="#698a19",
    border=6,
    highlightthickness=0,
    justify='center')
entry_goal.place(x=800, y=300)

label_target = Label(window, text="Target:", font=("Otomanopee One", 20), fg='#84A928',bg="#FFFFFF")
label_target.place(x=550, y=350)
entry_target = Entry(window, font=("Otomanopee One", 16), width=30,bg="#d6e8ad",
    fg="#84A928",
    border=6,
    highlightthickness=0,
    justify='center')
entry_target.place(x=800, y=350)


label_status = Label(window, text="Status:", font=("Otomanopee One", 20),fg='#84A928',bg="#FFFFFF")
label_status.place(x=550, y=400)


status_var = StringVar(window)
status_var.set("Progress")  

status_options = ["Pending", "In Progress", "Completed"]


dropdown_status = OptionMenu(window, status_var, *status_options)
dropdown_status.config(font=("Otomanopee One", 20), fg="#84A928", bg="#d6e8ad")  # Main button font, color, and background
dropdown_status["menu"].config(font=("Otomanopee One", 20), fg="#84A928", bg="#d6e8ad")  # Dropdown options font, color, and background


dropdown_status.place(x=800, y=400, width=200, height=50) 

button_save = Button(window, text="  Save  ", font=("Otomanopee One", 16), command=submit_goal, fg="#84A928", bg="#d6e8ad")
button_save.place(x=1070, y=400)


window.resizable(True, True)
window.mainloop()
