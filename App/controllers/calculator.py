from App.database import db
from App.models import Workouts, Routines

def calculate_bmr(weight, height, age, sex):
    if sex == "male":
        bmr = 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age)
    else:
        bmr = 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age)
    return bmr

def calculate_daily_calories(bmr, activity_level):
    if activity_level == "sedentary":
        calories = bmr * 1.2
    elif activity_level == "lightly active":
        calories = bmr * 1.375
    elif activity_level == "moderately active":
        calories = bmr * 1.55
    else:
        calories = bmr * 1.725
    return calories

def calculate_bmi(weight, height):
    bmi = (weight / (height ** 2)) * 703
    bmi_rounded = round(bmi, 1)

    if bmi_rounded < 18.5:
        category = 'Underweight'
    elif 18.5 <= bmi_rounded <= 24.9:
        category = 'Normal Weight'
    elif 25 <= bmi_rounded <= 29.9:
        category = 'Overweight'
    else:
        category = 'Obese'
        
    return bmi_rounded, category