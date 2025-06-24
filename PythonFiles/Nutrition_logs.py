import mysql.connector
from tkinter import *
from pathlib import Path
from datetime import datetime
import sys
import subprocess
from db_config import DB_CONFIG

global username
username = sys.argv[1] if len(sys.argv) > 1 else "User"

def open_file_with_delay(filename,username, delay=2000):
    script_path = Path(__file__).parent / filename
    subprocess.Popen(['python', str(script_path), username])
    window.after(delay, window.destroy)

def open_del(filename,username, delay=8000):
    script_path = Path(__file__).parent / filename
    subprocess.Popen(['python', str(script_path), username])
    window.after(delay, window.destroy)

# MySQL database connection
def connect_to_db():
    return mysql.connector.connect(**DB_CONFIG)


def open_file_with_delay(filename,username, delay=2000):
    script_path = Path(__file__).parent / filename
    subprocess.Popen(['python', str(script_path), username])
    window.after(delay, window.destroy)

def log_nutrition_data():
    
    meal = entry_4.get()          
    date = datetime.now().date()        
    calories = entry_5.get()     
    proteins = entry_6.get()      
    fats = entry_2.get()          
    carbs = entry_3.get()         

    
    if not username or not meal or not date or not calories or not proteins or not fats or not carbs:
        print("Please fill in all fields!")
        return

    
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        
        query = '''INSERT INTO NutritionLog (Username, Date, MealDescription, CaloriesConsumed, MacroNutrients) 
                    VALUES (%s, %s, %s, %s, %s)'''

        
        data = (username,  date, meal, int(calories), f"Proteins: {proteins}, Fats: {fats}, Carbs: {carbs}")
        
        cursor.execute(query, data)
        conn.commit()
        print_logs()
        cursor.close()
        conn.close()

        print("Data logged successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def print_logs():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
   
    cursor.execute("""
    SELECT USERNAME, MEALdescription, DATE, CALORIESCONSUMED, MACRONUTRIENTS , LOGID
    FROM NUTRITIONLOG
    WHERE USERNAME=%s AND DATE=%s ORDER BY LOGID DESC
""", (username, datetime.now().date()))

    
    results = cursor.fetchall()
    if results:
    
        result_str = "-" * 130 + "\n"
        result_str += "LOGID  |USERNAME  | MEAL\t\t| DATE\t  | CALORIES\t| MACRONUTRIENTS\n"
        result_str += "-" * 130 + "\n"
        
        
        for row in results:
            result_str += f"{row[5]}       |{row[0]}\t| {row[1]}\t| {row[2]} | {row[3]}\t\t| {row[4]}\n"
        result_str += "-" * 130 + "\n"
    else:
        result_str = "No data available."
    #
    canvas.delete("result_label")
    
    canvas.create_text(
        459, 465, 
        text="Your logs - ", 
        font=("Otomanopee One", 14), 
        fill="#FFB001",
        anchor="nw", 
        tags="result_label"  
    )
    
    
    canvas.create_text(
        459, 505, 
        text=result_str, 
        font=("Otomanopee One", 11), 
        fill="#84A928", 
        anchor="nw", 
        tags="result_label"  
    )
    conn.commit()
    cursor.close()
    conn.close()
    

def delete_log_input():
    
    canvas.create_text(
        523.0,
        675.0,
        anchor="nw",
        text="Enter Log ID to delete",
        fill="#84A928",
        font=("Otomanopee One", 30 * -1)
    )

    
    entry_image_logid = PhotoImage(file=relative_to_assets("entry_2.png"))
    canvas.create_image(
        737.0,
        700.0,
        image=entry_image_logid
    )

    
    global entry_logid  
    entry_logid = Entry(canvas, font=("Otomanopee One", 14), bd=0, bg="#f0f0f0", fg="#84A928",highlightthickness=0)
    entry_logid.place(
        x=897.5,
        y=680.0,
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

        
        query = "DELETE FROM NutritionLog WHERE LOGID = %s"
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


# Tkinter GUI setup
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).parent.parent / 'build/assets/frame1'

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("1536x817+0+0")
window.configure(bg="#84A928")

canvas = Canvas(window, bg="#84A928", height=817, width=1536, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)


canvas = Canvas(
    window,
    bg = "#84A928",
    height = 817,
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
    512.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    768.0,
    512.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    910.0,
    512.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    916.0,
    103.0,
    image=image_image_4
)

canvas.create_text(
    620.0,
    58.0,
    anchor="nw",
    text="NUTRITION LOGS",
    fill="#FFB001",
    font=("Otomanopee One", 64 * -1)
)

canvas.create_text(
    793.0,
    396.0,  
    anchor="nw",
    text="Fats",
    fill="#FFB001",
    font=("Otomanopee One", 36 * -1)
)

canvas.create_text(
    433.0,
    259.0,  
    anchor="nw",
    text="Meal",
    fill="#84A928",
    font=("Otomanopee One", 36 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    737.0,
    423.5,  
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#f8de9d",
    fg="#FFB001",
    highlightthickness=0,
    font=("Otomanopee One", 18 * -1)
)
entry_2.place(
    x=718.5,
    y=396.0, 
    width=37.0,
    height=53.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    969.5,
    424.0, 
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#f8de9d",
    fg="#FFB001",
    highlightthickness=0,
    font=("Otomanopee One", 18 * -1)
)
entry_3.place(
    x=952.0,
    y=396.0,  
    width=35.0,
    height=54.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    1001.5,
    286.5, 
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#d6e8ad",
    fg="#84A928",
    highlightthickness=0,
    font=("Otomanopee One", 18 * -1)
)
entry_4.place(
    x=715.5,
    y=259.0,  
    width=572.0,
    height=53.0
)

canvas.create_text(
    433.0,
    325.0, 
    anchor="nw",
    text="Calories",
    fill="#84A928",
    font=("Otomanopee One", 36 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    799.0,
    350.5, 
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#d6e8ad",
    highlightthickness=0,
    font=("Otomanopee One", 18 * -1),
    fg="#84A928"
)
entry_5.place(
    x=715.5,
    y=323.0,
    width=167.0,
    height=53.0
)

canvas.create_text(
    433.0,
    396.0, 
    anchor="nw",
    text="Proteins",
    fill="#FFB001",
    font=("Otomanopee One", 36 * -1)
)

canvas.create_text(
    1070.0,
    395.0,  
    anchor="nw",
    text="Carbs",
    fill="#FFB001",
    font=("Otomanopee One", 36 * -1)
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    1239.5,
    418.0, 
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#f8de9d",
    fg="#FFB001",
    highlightthickness=0,
    font=("Otomanopee One", 18 * -1)
)
entry_6.place(
    x=1222.0,
    y=390.0, 
    width=35.0,
    height=54.0
)



button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=log_nutrition_data,
    relief="flat",
    bg="white"
)


button_1.place(
    x=1315.0,
    y=380.0,
    width=83.0,
    height=84.0
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    915.0,
    564.0,
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
    x=85.0,
    y=20.0,
    width=180.0,
    height=188.51348876953125
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    178.0,
    515.0,
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
    x=70.769287109375,
    y=340.84423828125,
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
    x=70.769287109375,
    y=423.3134765625,
    width=214.46151733398438,
    height=72.76707458496094
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_file_with_delay("Nutrition_plans.py",username),
    relief="flat",
    background="#CAE2CC"
)
button_5.place(
    x=70.769287109375,
    y=596.984375,
    width=214.4615478515625,
    height=72.76707458496094
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:open_file_with_delay("User_dashboard.py",username),
    relief="flat",
    background="#CAE2CC"
)
button_6.place(
    x=70.769287109375,
    y=261.285400390625,
    width=214.46151733398438,
    height=72.76707458496094
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_file_with_delay("Workouts.py",username),
    relief="flat",
    background="#CAE2CC"
)
button_7.place(
    x=70.769287109375,
    y=507.723388671875,
    width=214.46151733398438,
    height=72.76707458496094
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_file_with_delay("User_profile.py",username),
    relief="flat",
    background="#CAE2CC"
)
button_8.place(
    x=71.0,
    y=687.0,
    width=95.0,
    height=88.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_del("Delete_all.py",username),
    relief="flat",
    background="#CAE2CC"
)
button_9.place(
    x=178.0,
    y=687.0,
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
    y=680.0,
)

print_logs()

window.resizable(True, True)
window.mainloop()
