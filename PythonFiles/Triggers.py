import mysql.connector
import sys
from db_config import DB_CONFIG


global username
username = sys.argv[1] if len(sys.argv) > 1 else "User"
print("In trigger")

def setup_database_triggers():
    try:

        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS DeletedRecordsLog (
                LogID INT AUTO_INCREMENT PRIMARY KEY,
                TableName VARCHAR(50) NOT NULL,
                DeletedRecord JSON NOT NULL,
                Username VARCHAR(50) NOT NULL,
                DeletedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

 
        cursor.execute('''
        CREATE TRIGGER IF NOT EXISTS Log_UserProfile_Delete
        AFTER DELETE ON UserProfile
        FOR EACH ROW
        BEGIN
            INSERT INTO DeletedRecordsLog (TableName, DeletedRecord, Username)
            VALUES (
                'UserProfile',
                JSON_OBJECT(
                    'Username', OLD.Username,
                    'Name', OLD.Name,
                    'Age', OLD.Age,
                    'Gender', OLD.Gender,
                    'PhoneNo', OLD.PhoneNo,
                    'Specialization', OLD.Specialization
                ),
                OLD.Username
            );
        END
        ''')


        cursor.execute('''
        CREATE TRIGGER IF NOT EXISTS Log_Workout_Delete
        AFTER DELETE ON Workout
        FOR EACH ROW
        BEGIN
            INSERT INTO DeletedRecordsLog (TableName, DeletedRecord, Username)
            VALUES (
                'Workout',
                JSON_OBJECT(
                    'WorkoutID', OLD.WorkoutID,
                    'Username', OLD.Username,
                    'WorkoutType', OLD.WorkoutType,
                    'Duration', OLD.Duration,
                    'CaloriesBurned', OLD.CaloriesBurned,
                    'Date', OLD.Date
                ),
                OLD.Username
            );
        END
        ''')


        cursor.execute('''
        CREATE TRIGGER IF NOT EXISTS Log_NutritionLog_Delete
        AFTER DELETE ON NutritionLog
        FOR EACH ROW
        BEGIN
            INSERT INTO DeletedRecordsLog (TableName, DeletedRecord, Username)
            VALUES (
                'NutritionLog',
                JSON_OBJECT(
                    'LogID', OLD.LogID,
                    'Username', OLD.Username,
                    'Date', OLD.Date,
                    'MealDescription', OLD.MealDescription,
                    'CaloriesConsumed', OLD.CaloriesConsumed,
                    'MacroNutrients', OLD.MacroNutrients
                ),
                OLD.Username
            );
        END
        ''')

        cursor.execute('''
        CREATE TRIGGER IF NOT EXISTS Log_HealthMetrics_Delete
        AFTER DELETE ON HealthMetrics
        FOR EACH ROW
        BEGIN
            INSERT INTO DeletedRecordsLog (TableName, DeletedRecord, Username)
            VALUES (
                'HealthMetrics',
                JSON_OBJECT(
                    'MetricID', OLD.MetricID,
                    'Username', OLD.Username,
                    'BMI', OLD.BMI,
                    'BloodPressure', OLD.BloodPressure,
                    'HeartRate', OLD.HeartRate,
                    'Date', OLD.Date
                ),
                OLD.Username
            );
        END
        ''')


        cursor.execute('''
        CREATE TRIGGER IF NOT EXISTS Log_GoalsAndProgress_Delete
        AFTER DELETE ON GoalsAndProgress
        FOR EACH ROW
        BEGIN
            INSERT INTO DeletedRecordsLog (TableName, DeletedRecord, Username)
            VALUES (
                'GoalsAndProgress',
                JSON_OBJECT(
                    'ReportID', OLD.ReportID,
                    'Username', OLD.Username,
                    'Goal', OLD.Goal,
                    'Target', OLD.Target,
                    'Status', OLD.Status,
                    'Date', OLD.Date
                ),
                OLD.Username
            );
        END
        ''')


        cursor.execute('''
        CREATE TRIGGER IF NOT EXISTS Log_User_Delete
        AFTER DELETE ON User
        FOR EACH ROW
        BEGIN
            INSERT INTO DeletedRecordsLog (TableName, DeletedRecord, Username)
            VALUES (
                'User',
                JSON_OBJECT(
                    'Username', OLD.Username,
                    'Email', OLD.Email,
                    'Password', OLD.Password,
                    'RegistrationDate', OLD.RegistrationDate
                ),
                OLD.Username
            );
        END
        ''')

 
        conn.commit()
        print("Triggers and DeletedRecordsLog table created successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        

    finally:

        if cursor:
            cursor.close()
        if conn:
            conn.close()

setup_database_triggers()
