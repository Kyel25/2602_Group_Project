from App.database import db
from App.models import Workouts, Routines

def calculate_bmr(weight, height, age, sex):
    if sex == "male":
        bmr = 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age)
    else:
        bmr = 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age)
    return round(bmr, 2) 

def calculate_daily_calories(bmr, activity_level):
    if activity_level == "sedentary":
        calories = bmr * 1.2
    elif activity_level == "lightly active":
        calories = bmr * 1.375
    elif activity_level == "moderately active":
        calories = bmr * 1.55
    else:
        calories = bmr * 1.725
    return round(calories, 2)  

def calculate_daily_calories_loss(bmr, activity_level):
    loss_factor = {
        "mild": 0.09,
        "normal": 0.17,
        "extreme": 0.34
    }

    calories = calculate_daily_calories(bmr, activity_level)
    mild_loss_calories = round(calories - (calories * loss_factor["mild"]), 2)
    normal_loss_calories = round(calories - (calories * loss_factor["normal"]), 2)
    extreme_loss_calories = round(calories - (calories * loss_factor["extreme"]), 2)

    return mild_loss_calories, normal_loss_calories, extreme_loss_calories

def calculate_daily_calories_gain(bmr, activity_level):
    gain_factor = {
        "mild": 0.09,
        "normal": 0.17,
        "extreme": 0.34
    }

    calories = calculate_daily_calories(bmr, activity_level)
    mild_gain_calories = round(calories + (calories * gain_factor["mild"]), 2)
    normal_gain_calories = round(calories + (calories * gain_factor["normal"]), 2)
    extreme_gain_calories = round(calories + (calories * gain_factor["extreme"]), 2)

    return mild_gain_calories, normal_gain_calories, extreme_gain_calories


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