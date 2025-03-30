from pathlib import Path
from datetime import datetime
import subprocess
import sys
from tkinter import Tk, Canvas, Label, Button, PhotoImage
import mysql.connector


conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="riya2004",
            database="health_fitness"
        )
cursor = conn.cursor()
        
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\hicha\OneDrive\Desktop\DBMSSSS\DBMS_Project_code\build\assets\frame2")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_file_with_delay(filename,username, delay=2000):
    subprocess.Popen(['python', rf'C:\Users\hicha\OneDrive\Desktop\DBMSSSS\DBMS_Project_code\{filename}',username])
    window.after(delay, window.destroy)

def open_del(filename,username, delay=8000):
    subprocess.Popen(['python', rf'C:\Users\hicha\OneDrive\Desktop\DBMSSSS\DBMS_Project_code\{filename}',username])
    window.after(delay, window.destroy)

username = sys.argv[1] if len(sys.argv) > 1 else "User"

import random


order = random.choice(["ASC", "DESC"])


coach_query = f'''
    SELECT t.name ,t.specialization
    FROM trainer t, UserProfile
    WHERE t.specialization = UserProfile.specialization 
      AND UserProfile.username = %s 
    ORDER BY RAND() {order} 
    LIMIT 1
'''

cursor.execute(coach_query, (username,))
coach = cursor.fetchone()
coachname = coach[0]+'\n'+'Speciality - '+coach[1] if coach else "NA"
print(coach)



bmi_query = '''
            SELECT BMI 
            FROM HealthMetrics 
            WHERE Username = %s ORDER BY MetricID DESC LIMIT 1
        '''
cursor.execute(bmi_query, (username,))
bmi_result = cursor.fetchone()
bmii = bmi_result[0] if bmi_result else "NA"


goals_query = '''
            SELECT Goal 
            FROM GoalsAndProgress 
            WHERE Username = %s ORDER BY Date DESC LIMIT 1
        '''
cursor.execute(goals_query, (username,))
goals_result = cursor.fetchone()
Goals = goals_result[0] if goals_result else "NA"

        
workout_query = '''
            SELECT WorkoutType 
            FROM Workout 
            WHERE Username = %s ORDER BY Workoutid DESC LIMIT 1
        '''
cursor.execute(workout_query, (username,))
workout_result = cursor.fetchone()
Workouttt = workout_result[0] if workout_result else "NA"

        
meal_query = '''
            SELECT MealDescription 
            FROM NutritionLog 
            WHERE Username = %s ORDER BY LOGID DESC LIMIT 1
        '''
cursor.execute(meal_query, (username,))
meal_result = cursor.fetchone()
meal = meal_result[0] if meal_result else "NA"

        
cal_con_query = '''
            SELECT SUM(CaloriesConsumed) AS TotalCaloriesConsumed 
            FROM NutritionLog 
            WHERE Username = %s 
            GROUP BY Date
            ORDER BY LOGID DESC LIMIT 1
        '''
cursor.execute(cal_con_query, (username,))
cal_con_result = cursor.fetchone()
cal_con = cal_con_result[0] if cal_con_result else "NA"

        #
cal_burn_query = '''
            SELECT SUM(CaloriesBurned) AS TotalCaloriesBurned
            FROM Workout
            WHERE Username = %s
            GROUP BY Date
            ORDER BY Date DESC LIMIT 1;
        '''
cursor.execute(cal_burn_query, (username,))
cal_burn_result = cursor.fetchone()
cal_burn = cal_burn_result[0] if cal_burn_result else "NA"

window = Tk()
window.geometry("1528x1572+0+0")
window.configure(bg = "#E7F2D6")

canvas = Canvas(
    window,
    bg = "#E7F2D6",
    height = 1572,
    width = 1528,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    768.0,
    482.0,  
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    768.0,
    1221.0,  
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    780.0,
    447.0,  
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    768.0,
    1218.0,  
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    768.0,
    1320.0, 
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    924.0,
    484.0,  
    image=image_image_6
)

def get_greeting():
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "Good Morning!"
    elif 12 <= hour < 18:
        return "Good Afternoon!"
    else:
        return "Good Evening!"


canvas.create_text(
    441.0,
    238.0,
    anchor="nw",
    text=f"Hope you are having a {get_greeting()}",
    fill="#3C98A4",
    font=("Otomanopee One", 36 * -1)
)


canvas.create_text(
    441.0,
    308.0, 
    anchor="nw",
    text=f"Your Coach is - {coachname}\nBMI - {bmii}\nCurrent Goal - {Goals}\n",
    fill="#85A929",
    font=("Otomanopee One", 32 * -1)
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    935.0,
    625.0,  
    image=image_image_7
)

canvas.create_text(
    455.0,
    502.0,  
    anchor="nw",
    text="Recent Activities :",
    fill="#3C98A4",
    font=("Otomanopee One", 28 * -1)
)

canvas.create_text(
    455.0,
    558.0,  
    anchor="nw",
    text=f"Last Workout - {Workouttt}\nLast Meal Logged - {meal}\nCalories Consumed - {cal_con}\nCalories Burnt -{cal_burn}",
    fill="#82BBB5",
    font=("Otomanopee One", 28 * -1)
)


image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    713.0,
    88.0,  
    image=image_image_8
)

canvas.create_text(
    518.0,
    37.0,  
    anchor="nw",
    text=f"Hello {username}!",
    fill="#3C98A4",
    font=("Otomanopee One", 64 * -1)
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    1253.0,
    1176.0,  
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    518.0,
    1176.0,  
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    1277.0,
    88.0,  
    image=image_image_11
)


now = datetime.now()
date_str = now.strftime("%d %b %Y\n   %I:%M %p")  


canvas.create_text(
    1180.0,
    45.0,
    anchor="nw",
    text=date_str,
    fill="#3C98A4",
    font=("Otomanopee One", 30 * -1)
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
    x=90.0,
    y=10.0, 
    width=180.0,
    height=188.51348876953125
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    183.0,
    490.0, 
    image=image_image_12
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))

button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:open_file_with_delay("Health_metrics.py",username),
    relief="flat",
    background="#CAE2CC"
)

button_2.place(
    x=75.76922607421875,
    y=315.84423828125, 
    width=214.46151733398438,
    height=72.76707458496094
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:open_file_with_delay("Goals_and_progress.py",username),
    relief="flat",
    background="#CAE2CC"
)
button_3.place(
    x=75.76922607421875,
    y=398.3134765625, 
    width=214.46151733398438,
    height=72.76707458496094
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_file_with_delay("Nutrition_plans.py",username),
    relief="flat",
    background="#CAE2CC"
)
button_4.place(
    x=75.76922607421875,
    y=571.984375, 
    width=214.4615478515625,
    height=72.76707458496094
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat",
    background="#CAE2CC"
)
button_5.place(
    x=75.76922607421875,
    y=236.285400390625,
    width=214.46151733398438,
    height=72.76707458496094
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_file_with_delay("Workouts.py",username),
    relief="flat",
    background="#CAE2CC"
)
button_6.place(
    x=75.76922607421875,
    y=482.723388671875,  
    width=214.46151733398438,
    height=72.76707458496094
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_file_with_delay("User_profile.py",username),
    relief="flat",
    background="#CAE2CC"
)



button_7.place(
    x=76.76922607421875,
    y=660.244140625,  
    width=95.0,
    height=88.0
)

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
    x=183.0,
    y=660.0,
    width=95.0,
    height=88.0
)


window.resizable(False, False)
window.mainloop()
conn.commit()
cursor.close()