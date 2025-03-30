# Please change the file path accordingly

import mysql.connector

def create_database_and_tables():
    try:
        
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your password"
        )
        cursor = conn.cursor()
        
        
        cursor.execute("DROP DATABASE IF EXISTS health_fitness")
        cursor.execute("CREATE DATABASE health_fitness")
        conn.commit()

        
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your password",
            database="health_fitness"
        )
        cursor = conn.cursor()

        
        cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS User (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    registrationDate DATE

            )
        ''')

        cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS UserProfile (
            Username VARCHAR(50),
            Name VARCHAR(255) NOT NULL,
            Age INT CHECK (Age >= 0),
            Gender VARCHAR(15),
            PhoneNo VARCHAR(12),
            Specialization VARCHAR(50),
            FOREIGN KEY (Username) REFERENCES User(Username) ON DELETE CASCADE ON UPDATE CASCADE
        )
        ''')

        cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS Workout (
                WorkoutID INT AUTO_INCREMENT PRIMARY KEY,
                Username VARCHAR(50),
                WorkoutType VARCHAR(50) NOT NULL,
                Duration VARCHAR(50) NOT NULL ,
                CaloriesBurned INT NOT NULL CHECK (CaloriesBurned >= 0),
                Date DATE NOT NULL,
                FOREIGN KEY (Username) REFERENCES User(Username) ON DELETE CASCADE ON UPDATE CASCADE
            )
        ''')

        
        cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS NutritionPlans (
                PlanID INT AUTO_INCREMENT PRIMARY KEY,
                MealTime VARCHAR(50) NOT NULL,  -- Breakfast, Lunch, Dinner, Snacks
                MealType VARCHAR(50) NOT NULL,  -- Meal category: Veg, Vegan, High Protein, Keto, Low Carb, etc.
                CalorieCount INT NOT NULL CHECK (CalorieCount >= 0),
                Description TEXT               -- Detailed meal description
            )
        ''')


        cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS NutritionLog (
                LogID INT AUTO_INCREMENT PRIMARY KEY,
                Username VARCHAR(50),
                Date DATE NOT NULL,
                MealDescription TEXT NOT NULL,
                CaloriesConsumed INT NOT NULL CHECK (CaloriesConsumed >= 0),
                MacroNutrients TEXT,
                FOREIGN KEY (Username) REFERENCES User(Username) ON DELETE CASCADE ON UPDATE CASCADE

            )
        ''')

        cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS HealthMetrics (
                MetricID INT AUTO_INCREMENT PRIMARY KEY,
                Username VARCHAR(50),
                BMI DECIMAL(4,2) CHECK (BMI > 0),
                BloodPressure VARCHAR(7),
                HeartRate INT CHECK (HeartRate > 0),
                Date DATE NOT NULL,
                FOREIGN KEY (Username) REFERENCES User(Username) ON DELETE CASCADE ON UPDATE CASCADE
            )
        ''')

        cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS GoalsAndProgress (
                ReportID INT AUTO_INCREMENT PRIMARY KEY,
                Username VARCHAR(50),
                Goal TEXT NOT NULL,
                Target TEXT,
                Status VARCHAR(20) CHECK (Status IN ('Pending', 'In Progress', 'Completed')),
                Date DATE NOT NULL,
                FOREIGN KEY (Username) REFERENCES User(Username) ON DELETE CASCADE ON UPDATE CASCADE
            )
        ''')

        cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS Trainer (
                TrainerID INT AUTO_INCREMENT PRIMARY KEY,
                Name VARCHAR(255) NOT NULL,
                Specialization VARCHAR(50) NOT NULL,
                ContactInfo VARCHAR(255) NOT NULL UNIQUE
            )
        ''')

 
        cursor.execute('''
    INSERT INTO Trainer (Name, Specialization, ContactInfo) VALUES
    ('Pranay Saxena', 'Cardio Fitness Trainer', 'pranay.saxena@gmail.com'),
    ('Riya Shetty', 'Strength Training Expert', 'riya.shetty@gmail.com'),
    ('Pranav Rao', 'HIIT Trainer', 'pranav.rao@gmail.com'),
    ('Pranav Acharya', 'Yoga and Flexibility Trainer', 'pranav.acharya@gmail.com'),
    ('Rishika Narayan', 'Weight Loss Coach', 'rishika.narayan@gmail.com'),
    ('Rishita Singh', 'Cardio Fitness Trainer', 'rishita.singh@gmail.com'),
    ('Rishav Sinha', 'Strength Training Expert', 'rishav.sinha@gmail.com'),
    ('Prithvi SK', 'HIIT Trainer', 'prithvi.sk@gmail.com')
''')

        
        
        
        sample_plans = [
            
            ("Breakfast", "Veg", 350, "Vegetable paratha with yogurt and pickle",),
            ("Lunch", "Veg", 600, "Chole (chickpea curry) with basmati rice and raita",),
            ("Dinner", "Veg", 550, "Aloo gobi (potato and cauliflower curry) with chapati",),
            ("Snacks", "Veg", 150, "Samosas with mint chutney",),

            
            ("Breakfast", "Vegan", 300, "Poha with peas and peanuts",),
            ("Lunch", "Vegan", 500, "Masoor dal (red lentils) with brown rice and salad",),
            ("Dinner", "Vegan", 550, "Tofu curry with roti and steamed vegetables",),
            ("Snacks", "Vegan", 200, "Cucumber and carrot sticks with hummus",),

            
            ("Breakfast", "High Protein", 400, "Moong dal chilla (mung bean pancakes) with chutney",),
            ("Lunch", "High Protein", 700, "Grilled chicken tikka with quinoa and green salad",),
            ("Dinner", "High Protein", 650, "Fish curry with steamed broccoli and brown rice",),
            ("Snacks", "High Protein", 250, "Greek yogurt with almonds and a drizzle of honey",),

            
            ("Breakfast", "Keto", 350, "Scrambled eggs with spinach and paneer (Indian cottage cheese)",),
            ("Lunch", "Keto", 600, "Cauliflower rice with chicken curry and a side of avocado",),
            ("Dinner", "Keto", 700, "Paneer tikka (grilled cottage cheese) with a side of sautÃ©ed spinach",),
            ("Snacks", "Keto", 150, "Cheese and cucumber slices",),

            
            ("Breakfast", "Weight Loss", 250, "Oats porridge with almonds and chia seeds",),
            ("Lunch", "Weight Loss", 450, "Grilled tofu with quinoa and a side of mixed veggies",),
            ("Dinner", "Weight Loss", 400, "Baked salmon with roasted vegetables",),
            ("Snacks", "Weight Loss", 100, "Cucumber slices with lemon and salt",),

            
            ("Breakfast", "Low Carb", 350, "Masala omelette with spinach and mushrooms",),
            ("Lunch", "Low Carb", 600, "Grilled chicken with cauliflower rice and a side of salad",),
            ("Dinner", "Low Carb", 650, "Paneer tikka with sautÃ©ed bell peppers and zucchini",),
            ("Snacks", "Low Carb", 200, "Cheese and cucumber slices",)
        ]
        
        for plan in sample_plans:
            cursor.execute('''
                INSERT INTO NutritionPlans (MealTime, MealType, CalorieCount, Description)
                VALUES (%s, %s, %s, %s)
            ''', plan)


        
        conn.commit()
        print("Tables created and data inserted successfully.")

    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


create_database_and_tables()
