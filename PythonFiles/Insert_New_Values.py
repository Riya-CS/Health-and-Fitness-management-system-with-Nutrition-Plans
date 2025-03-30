# Please change the file path accordingly
import mysql.connector
from datetime import datetime
from Create_Tables import create_database_and_tables  

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your password",
        database="health_fitness"  
    )

def insert_user_profile(username, name, age, gender, height, weight, goals):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO UserProfile (username, Name, Age, Gender, Height, Weight, Goals) VALUES (%s, %s, %s, %s, %s, %s, %s)''',
                       (username, name, age, gender, height, weight, goals))
        conn.commit()

def insert_workout(username, workout_type, duration, calories_burned):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO Workout (username, WorkoutType, Duration, CaloriesBurned, Date) VALUES (%s, %s, %s, %s, %s)''',
                       (username, workout_type, duration, calories_burned, datetime.now().isoformat()))
        conn.commit()

def insert_nutrition_plan(username, meal_type, calories):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO NutritionPlans (username, MealType, Calories, Date) VALUES (%s, %s, %s, %s)''',
                       (username, meal_type, calories, datetime.now().isoformat()))
        conn.commit()

def insert_nutrition_log(username, plan_id, meal_description, calories_consumed, macronutrients):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO NutritionLog (username, PlanID, Date, MealDescription, CaloriesConsumed, MacroNutrients) VALUES (%s, %s, %s, %s, %s, %s)''',
                       (username, plan_id, datetime.now().isoformat(), meal_description, calories_consumed, macronutrients))
        conn.commit()

def insert_health_metrics(username, bmi, blood_pressure, heart_rate):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO HealthMetrics (username, BMI, BloodPressure, HeartRate, Date) VALUES (%s, %s, %s, %s, %s)''',
                       (username, bmi, blood_pressure, heart_rate, datetime.now().isoformat()))
        conn.commit()

def insert_goals_and_progress(username, goal, target, status, summary):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO GoalsAndProgress (username, Goal, Target, Status, Summary, Date) VALUES (%s, %s, %s, %s, %s, %s)''',
                       (username, goal, target, status, summary, datetime.now().isoformat()))
        conn.commit()

def insert_notifications(username, notification_type, message):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO Notifications (username, NotificationType, Message, Date) VALUES (%s, %s, %s, %s)''',
                       (username, notification_type, message, datetime.now().isoformat()))
        conn.commit()

def insert_trainer(name, specialization, contact_info):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO Trainer (Name, Specialization, ContactInfo) VALUES (%s, %s, %s)''',
                       (name, specialization, contact_info))
        conn.commit()

def insert_user_trainer_mapping(username, trainer_id, start_date, end_date):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO UserTrainerMapping (username, TrainerID, StartDate, EndDate) VALUES (%s, %s, %s, %s)''',
                       (username, trainer_id, start_date, end_date))
        conn.commit()

def send_daily_notifications(username):
    notifications = [
        ("Morning Reminder", "Good morning! Time to start your day with a healthy breakfast."),
        ("Afternoon Reminder", "It's lunchtime! Don't forget to eat something nutritious."),
        ("Evening Reminder", "Great job today! Remember to stay hydrated and relax.")
    ]
    
    for notification_type, message in notifications:
        insert_notifications(username, notification_type, message)

if __name__ == '__main__':
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your password",
        database="health_fitness"
    )
    cursor = conn.cursor()

    create_database_and_tables() 
