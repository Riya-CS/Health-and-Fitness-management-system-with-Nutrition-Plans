from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
import mysql.connector
from datetime import datetime, timedelta
import sys
import subprocess
from db_config import DB_CONFIG

conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()
    

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).parent.parent / 'build/assets/frame4'

global username
username = sys.argv[1] if len(sys.argv) > 1 else "User"

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

def get_health_metrics(week_number, year):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
   
    start_date = datetime(year, 1, 1) + timedelta(weeks=week_number-1)
    end_date = start_date + timedelta(days=6)

    cursor.execute("""
    SELECT * FROM HealthMetrics WHERE date BETWEEN %s AND %s
    """, (start_date.date(), end_date.date()))
    
    result = cursor.fetchall()
    return result
    


def display_metrics():
    
    week = 4 
    metrics = get_health_metrics(week)
    if metrics:
        metrics_text = f"Week: {metrics[1]}, Heart Rate: {metrics[2]} BPM, Blood Pressure: {metrics[3]}, Height: {metrics[4]} cm, Weight: {metrics[5]} kg"
    else:
        metrics_text = "No data available for the selected week."

    
    canvas.create_text(
        768.0, 636.0,  
        text=metrics_text,
        fill="#3C98A4",
        font=("Otomanopee One", 18),
        anchor="center"
    )


def new_func():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    image_6 = canvas.create_image(908.0, 636.0, image=image_image_6)
    image_6 = canvas.create_image(908.0, 636.0, image=image_image_6)
    image_6 = canvas.create_image(908.0, 636.0, image=image_image_6)
    image_6 = canvas.create_image(908.0, 636.0, image=image_image_6)
    current_date = datetime.now().date()
    cursor.execute("""
        SELECT * FROM HealthMetrics WHERE USERNAME=%s AND Date = %s 
    """, (username,current_date,))
    result = cursor.fetchall()
    print(result)
    current_date = datetime.now().date()
    cursor.execute("""
        SELECT Username, BMI, BloodPressure, HeartRate, Date FROM HealthMetrics WHERE USERNAME=%s AND Date = %s ORDER BY MetricID DESC 
        LIMIT 5
    """, (username, current_date,))
    result = cursor.fetchall()

        
    if not result:
            result_str = "No data available"
    else:
            result_str = "-" * 95 + "\n"
            result_str += "Username\t| BMI\t| BloodPressure\t| HeartRate\t| Date\n"
            result_str += "-" * 95 + "\n"
            for row in result:
                
                result_str += f"{row[0]}\t\t| {row[1]}\t| {row[2]}\t\t| {row[3]}\t\t| {row[4]}\n"
        
    canvas.delete("result_label")
    label = canvas.create_text(440, 510, text="Recent entries -", font=("Otomanopee One", 13), fill="#1a646e", anchor="nw")
    label = canvas.create_text(440, 535, text=result_str, font=("Otomanopee One", 13), fill="#3C98A4", anchor="nw",tags="result_label")
    conn.commit() 
    conn.close()#

def calculate_bmi(weight, height):
    height_in_meters = height / 100  
    bmi = weight / (height_in_meters ** 2)  
    return round(bmi, 2)

def display_bmi():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    try:
        #print(entry_1.get(),entry_2.get(),entry_3.get(),entry_4.get())
        weight = float(entry_2.get()) 
        height = float(entry_1.get())  
        heart_rate = float(entry_4.get())
        blood_pressure = entry_3.get()
        if 1==1:
            if heart_rate < 60:
                heart_rate_message = "Low Heart Rate"
            elif 60 <= heart_rate <= 100:
                heart_rate_message = "Normal Heart Rate"
            else:
                heart_rate_message = "High Heart Rate"

            
            systolic, diastolic = map(int, blood_pressure.split('/'))  # Assuming blood pressure is in "systolic/diastolic" format
            if systolic < 90 or diastolic < 60:
                blood_pressure_message = "Low Blood Pressure"
            elif 90 <= systolic <= 120 and 60 <= diastolic <= 80:
                blood_pressure_message = "Normal Blood Pressure"
            else:
                blood_pressure_message = "High Blood Pressure"

            # Calculate BMI
            height_in_meters = height / 100 
            if weight <= 0 or height <= 0:
                raise ValueError("Weight and height must be positive values.")

            bmi = weight / (height_in_meters ** 2)

            if bmi < 18.5:
                bmi_category = "Underweight"
            elif 18.5 <= bmi <= 25:
                bmi_category = "Normal weight"
            else:
                bmi_category = "Overweight"

            
            metrics_text = (f"Height: {height} cm, Weight: {weight} kg\t"
                            f"Heart Rate: {heart_rate} BPM ({heart_rate_message})\n"
                            f"BMI: {bmi:.2f} ({bmi_category})\t\t"
                            f"BP: {blood_pressure} mmHg ({blood_pressure_message})")

        else:
            metrics_text = "No data available for the selected week."
    
    except ValueError as e:
        metrics_text = f"Error: {str(e)}"  
    
    label = Label(window, text=metrics_text, font=("Otomanopee One", 14), 
              fg="#e87a7e",bg="#FFFFFF")
 
    label.place(x=470, y=430) 
    
    current_date = datetime.now().date()

   
    cursor.execute("""
    INSERT INTO HealthMetrics (bmi, BloodPressure, HeartRate, date, username)
    VALUES (%s, %s, %s, %s, %s)
    """, (bmi, blood_pressure, heart_rate, current_date, username ))
    conn.commit() 
    conn.close()
    new_func()

    
window = Tk()

window.geometry("1528x820+0+0")

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
    403.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    768.0,
    500.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    908.0,
    512.0,
    image=image_image_3
)

canvas.create_text(
    843.0,
    363.0,
    anchor="nw",
    text="Heart Rate                    BPM",
    fill="#3C98A4",
    font=("Otomanopee One", 32 * -1)
)

canvas.create_text(
    843.0,
    273.0,
    anchor="nw",
    text="Blood Pressure              mmHg",
    fill="#3C98A4",
    font=("Otomanopee One", 32 * -1)
)

canvas.create_text(
    440.0,
    273.0,
    anchor="nw",
    text="Height               cm",
    fill="#3C98A4",
    font=("Otomanopee One", 32 * -1)
)

canvas.create_text(
    440.0,
    363.0,
    anchor="nw",
    text="Weight               kg",
    fill="#3C98A4",
    font=("Otomanopee One", 32 * -1)
)


image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    908.0,
    115.0,
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
    x=81.0,
    y=17.0,
    width=180.0,
    height=188.51348876953125
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    174.0,
    512.0,
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
    background="#CAE2CC"
)
button_2.place(
    x=66.76922607421875,
    y=337.84423828125,
    width=214.46151733398438,
    height=72.76707458496094
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_file_with_delay("Goals_and_progress.py",username),
    relief="flat",
    background="#CAE2CC"
)
button_3.place(
    x=66.76922607421875,
    y=420.3134765625,
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
    x=66.76922607421875,
    y=593.984375,
    width=214.4615478515625,
    height=72.76707458496094
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:open_file_with_delay("User_dashboard.py",username),
    relief="flat",
    background="#CAE2CC"
)
button_5.place(
    x=66.76922607421875,
    y=258.285400390625,
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
    x=66.76922607421875,
    y=504.723388671875,
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
    x=67.0,
    y=684.0,
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

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    656.5,
    294.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#82BBB5",
    fg="#000716",
    border=6,
    font=("Otomanopee One", 20),
    highlightthickness=0,
    justify='center'
)
entry_1.pack(pady=20)

entry_1.place(
    x=582.5,
    y=267.0,
    width=148.0,
    height=56.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    656.5,
    390.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#82BBB5",
    fg="#000716",
    border=6,
    font=("Otomanopee One", 20),
    highlightthickness=0,
    justify='center'
)
entry_2.place(
    x=582.5,
    y=363.0,
    width=148.0,
    height=56.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    1206.5,
    294.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#82BBB5",
    fg="#000716",
    border=6,
    font=("Otomanopee One", 20),
    highlightthickness=0,
    justify='center'
)
entry_3.place(
    x=1122.5,
    y=267.0,
    width=158.0,
    height=56.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    1206.5,
    387.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#82BBB5",
    fg="#000716",
    border=6,
    font=("Otomanopee One", 20),
    highlightthickness=0,
    justify='center'
)
entry_4.place(
    x=1122.5,
    y=360.0,
    width=158.0,
    height=56.0
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    908.0,
    636.0,
    image=image_image_6
)
new_func()

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=display_bmi, 
    relief="flat",
    bg="#FFFFFF"
)
button_9.place(
    x=1319.0,
    y=422.0,
    width=83.0,
    height=84.0
)

window.resizable(True, True)
window.mainloop()

cursor.close()
conn.close()
