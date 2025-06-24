import mysql.connector
from tkinter import *
from pathlib import Path
from datetime import datetime
import sys
import subprocess
from db_config import DB_CONFIG

global username
username = sys.argv[1] if len(sys.argv) > 1 else "User"
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).parent.parent / 'build/assets/frame5'

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_file_with_delay(filename,username, delay=2000):
    script_path = OUTPUT_PATH / filename
    subprocess.Popen(['python', str(script_path), username])
    window.after(delay, window.destroy)
    
def open_del(filename,username, delay=8000):
    script_path = OUTPUT_PATH / filename
    subprocess.Popen(['python', str(script_path), username])
    window.after(delay, window.destroy)

def log_workout_data():
    workout_type = entry_1.get()
    duration = entry_2.get()
    calories_burned = entry_3.get()
    date = datetime.now().date()

    if not username or not workout_type or not duration or not calories_burned:
        print("Please fill in all fields!")
        return

    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        query = '''INSERT INTO Workout (Username, WorkoutType, Duration, CaloriesBurned, Date) 
                   VALUES (%s, %s, %s, %s, %s)'''
        data = (username, workout_type, duration, int(calories_burned), date)
        
        cursor.execute(query, data)
        conn.commit()
        cursor.close()
        conn.close()

        print_logs()
        print("Workout data logged successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def print_logs():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        query = '''
        SELECT WorkoutID, Username, WorkoutType, Duration, CaloriesBurned, Date
        FROM Workout
        WHERE Username = %s AND Date = %s
        ORDER BY WorkoutID DESC
        '''
        cursor.execute(query, (username, datetime.now().date()))
        results = cursor.fetchall()
        if results:
            result_str = "-" * 100 + "\n"
            result_str += "ID  | USERNAME | TYPE       | DURATION | CALORIES | DATE\n"
            result_str += "-" * 100 + "\n"
            
            for row in results:
                result_str += f"{row[0]:<4}| {row[1]:<8}| {row[2]:<10}| {row[3]:<8}| {row[4]:<8}| {row[5]}\n"
            result_str += "-" * 100 + "\n"
        else:
            result_str = "No data available"
        canvas.delete("result_label")
        canvas.create_text(
            459, 485, 
            text="Your workouts -", 
            font=("Otomanopee One", 18), 
            fill="#e87a7e", 
            anchor="nw", 
            tags="result_label"
        )
        canvas.create_text(
            459, 517, 
            text=result_str, 
            font=("Otomanopee One", 11), 
            fill="#12BCAA", 
            anchor="nw", 
            tags="result_label"
        )
        conn.commit()
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")


def delete_log_input():
    
    canvas.create_text(
        523.0,
        710.0,
        anchor="nw",
        text="Enter Log ID to delete",
        fill="#e87a7e",
        font=("Otomanopee One", 30 * -1)
    )

    
    entry_image_logid = PhotoImage(file=relative_to_assets("entry_2.png"))
    canvas.create_image(
        737.0,
        700.0,
        image=entry_image_logid
    )

   
    global entry_logid  
    entry_logid = Entry(canvas, font=("Otomanopee One", 14), bd=0, bg="#f0f0f0", fg="#12BCAA",highlightthickness=0)
    entry_logid.place(
        x=897.5,
        y=710.0,
        width=200.0, 
        height=40.0  
    )

    
    button_delete.config(command=delete_log) 


def delete_log():
    conn = mysql.connector.connect(**DB_CONFIG)
    
    cursor = conn.cursor()
    
    log_id = entry_logid.get()  

    if not log_id:
        print("Please enter a Log ID to delete!")
        return

    try:
        conn1 = connect_to_db()
        cursor = conn1.cursor()

        
        query = "DELETE FROM Workout WHERE workoutID = %s"
        cursor.execute(query, (log_id,))
        conn1.commit()

        cursor.close()
        conn.close()

        print(f"Log with ID {log_id} deleted successfully!")
        print_logs()  

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    cursor.close()
    conn1.close()



def connect_to_db():
    return mysql.connector.connect(**DB_CONFIG)

window = Tk()
window.geometry("1536x806+0+0")
window.configure(bg="#FFFFFF")


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
    403.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    768.0,
    510.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    908.0,
    504.0,
    image=image_image_3
)

canvas.create_text(
    519.0,
    274.0,
    anchor="nw",
    text="Workout",
    fill="#12BCAA",
    font=("Otomanopee One", 36 * -1)
)

canvas.create_text(
    507.0,
    338.0,
    anchor="nw",
    text="Duration",
    fill="#12BCAA",
    font=("Otomanopee One", 36 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    1007.0,
    309.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#c0ddda",
    highlightthickness=0,
    font=("Otomanopee One", 22 * -1),
    fg="#157885"
)
entry_1.place(
    x=820.5,
    y=282.0,
    width=373.0,
    height=53.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    904.0,
    373.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#c0ddda",
    highlightthickness=0,
    font=("Otomanopee One", 22 * -1),
    fg="#157885"
)
entry_2.place(
    x=820.5,
    y=346.0,
    width=167.0,
    height=53.0
)

canvas.create_text(
    479.0,
    406.0,
    anchor="nw",
    text="Calories Burnt",
    fill="#12BCAA",
    font=("Otomanopee One", 36 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    904.0,
    434.5,
    image=entry_image_3,
    
)
entry_3 = Entry(
    bd=0,
    bg="#c0ddda",
    highlightthickness=0,
    font=("Otomanopee One", 22 * -1),
    fg="#157885"

)
entry_3.place(
    x=820.5,
    y=407.0,
    width=167.0,
    height=53.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=log_workout_data,
    relief="flat",
    background="#ffffff"
)
button_1.place(
    x=1315.0,
    y=384.0,
    width=83.0,
    height=84.0
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    915.0,
    592.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    908.0,
    115.0,
    image=image_image_5
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat",
    background="#3C98A4"
)
button_2.place(
    x=81.0,
    y=17.0,
    width=180.0,
    height=188.51348876953125
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    174.0,
    512.0,
    image=image_image_6
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_file_with_delay("Health_metrics.py",username),
    relief="flat",
    background="#CAE2CC"
)
button_3.place(
    x=66.76922607421875,
    y=337.84423828125,
    width=214.46151733398438,
    height=72.76707458496094
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_file_with_delay("Goals_and_progress.py",username),
    relief="flat",
    background="#CAE2CC"
)
button_4.place(
    x=66.76922607421875,
    y=420.3134765625,
    width=214.46151733398438,
    height=72.76707458496094
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:open_file_with_delay("Nutrition_plans.py",username),
    relief="flat",
    background="#CAE2CC"
)
button_5.place(
    x=66.76922607421875,
    y=593.984375,
    width=214.4615478515625,
    height=72.76707458496094
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_file_with_delay("User_dashboard.py",username),
    relief="flat",
    background="#CAE2CC"
)
button_6.place(
    x=66.76922607421875,
    y=258.285400390625,
    width=214.46151733398438,
    height=72.76707458496094
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat",
    background="#CAE2CC"
)
button_7.place(
    x=66.76922607421875,
    y=504.723388671875,
    width=214.46151733398438,
    height=72.76707458496094
)

button_image_b = PhotoImage(
    file=relative_to_assets("image_7.png"))
button_b = Button(
    image=button_image_b,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_file_with_delay("User_profile.py",username),
    relief="flat",
    background="#CAE2CC"
)
button_b.place(
    x=70.76922607421875,
    y=685.244140625,  
    width=95.0,
    height=88.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:open_del("Delete_all.py",username),
    relief="flat",
    background="#CAE2CC"
)
button_8.place(
    x=174.0,
    y=684.0,
    width=95.0,
    height=88.0
)

button_delete = Button(
    text="Delete a row",  
    font=("Otomanopee One", 14),  
    borderwidth=0,
    highlightthickness=0,
    command=delete_log_input,
    relief="flat",
    fg="white",  
    bg="#e76c74",  
)
button_delete.place(
    x=1235.0,
    y=710.0,
)

print_logs()
window.resizable(True, True)
window.mainloop()
