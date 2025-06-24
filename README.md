# HEALTH AND FITNESS MANAGEMENT SYSTEM WITH NUTRITION PLANS

## Overview
The **Health and Fitness Tracker** is a comprehensive application that helps users monitor their health, track workouts, maintain nutrition plans, and set fitness goals. It provides a seamless experience with user authentication, interactive dashboards, and personalized coaching.

---

## Features
### 🔹 Start Page
- **Sign Up**: Register as a new user.
- **Log In**: Authenticate existing users and access the dashboard.

### 🔹 Dashboard
A central hub summarizing all health and fitness data, including:
- Quick access to all features
- Personalized Workout Coach
- Calories Burnt & Intake Overview

### 🔹 User Profile
- Update personal information (name, gender, age, contact details).
- Select a preferred workout type to get assigned a coach.

### 🔹 Health Metrics
Track health parameters:
- Height & Weight
- Blood Pressure
- Heart Rate
- BMI Calculations
- Warnings for abnormal BP, Heart Rate, or BMI

### 🔹 Goals and Progress
- Set personal fitness targets.
- Monitor progress towards health goals.

### 🔹 Workouts
- Log workout details (duration, calories burnt).
- View past workouts for performance analysis.

### 🔹 Nutrition Plans
- Access various meal plans based on health goals.
- Toggle between different diet options.

### 🔹 Nutrition Logs
- Track daily meal intake.
- Available as a toggle feature in the Nutrition Plans section.

---

## 🎯 How It Works
1. **Start Page**: Sign up or log in.
2. **Dashboard**: View an overview of fitness progress.
3. **User Profile**: Update personal details and select workout preferences.
4. **Coach Assignment**: A coach is assigned based on the selected workout type.
5. **Health Metrics**: Input health stats and receive insights.
6. **Goals & Progress**: Set and track fitness goals.
7. **Workouts**: Log workout sessions and calories burnt.
8. **Nutrition Plans**: Choose a meal plan and track intake.
9. **Nutrition Logs**: Monitor daily food consumption.

---

## 🛠️ Tech Stack
- **Frontend**: Tkinter (GUI designed using Figma)
- **Backend**: Python
- **Database**: MySQL

---

## 🏁 Installation Guide
### 1. Clone the Repository
```sh
 git clone https://github.com/Riya-CS/Health-and-Fitness-management-system-with-Nutrition-Plans
 cd Health-and-Fitness-management-system-with-Nutrition-Plans
```
### 2. Install Dependencies
```sh
 pip install -r requirements.txt
```
### 3. Configure Database Credentials
Before running the application, open the `PythonFiles/db_config.py` file and update the MySQL `user` and `password` fields with your own MySQL username and password. For example:
```python
db_config.py
DB_CONFIG = {
    "host": "localhost",
    "user": "your_mysql_username",
    "password": "your_mysql_password",
    "database": "health_fitness"
}
```
You only need to update your credentials in this one file.

### 4. Run the Application
```
cd PythonFiles
python Create_Tables.py  # Run this ONLY ONCE to create the database and tables
python Start_page.py     # Launches the main application```
```
📝 Note:

You only need to run Create_Tables.py once to set up the database schema.

Do not run it again, unless you want to drop existing data.

---

## 🤝 Contributing
1. **Fork** the repository.
2. **Create a new branch** (`feature-branch`).
3. **Commit changes** and push to GitHub.
4. **Create a pull request** for review.

---

## 📩 Contact
For queries or suggestions, contact: **riyacsapkale@gmail.com**

