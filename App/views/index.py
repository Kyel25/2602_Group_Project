from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from flask_jwt_extended import jwt_required, current_user, unset_jwt_cookies, set_access_cookies
from App.models import db
from App.controllers.calculator import calculate_bmr, calculate_daily_calories

from App.controllers import(
    create_user, 
    list_all_workouts, 
    list_all_workouts_json, 
    list_workouts_by_body_part,
    list_workouts_by_level,
    list_workouts_by_type,
    list_all_routines,
    get_routine_by_id,
    create_routine,
    delete_routine
)


index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def login_page():
    return render_template('login.html')

@index_views.route('/home', methods=['GET'])
@jwt_required()
def home_page():
    return render_template('index.html')

@index_views.route('/workout', methods=['GET'])
@jwt_required()
def workout_page():
    workouts = list_all_workouts()

    return render_template('workout.html', workouts = workouts)

@index_views.route('/routine', methods=['GET'])
@jwt_required()
def routine_page():
    routines = list_all_routines()
    return render_template('routine.html', routines=routines, user = current_user)

@index_views.route('/create-routine', methods=['POST'])
@jwt_required()
def create_routine_action():
    data = request.form
    name = data['routine-name']
    routines = create_routine(name)
    return redirect(request.referrer)

@index_views.route('/delete-routine/<int:id>', methods=['GET'])
@jwt_required()
def delete_routine_action(id):
    delete_routine(id)
    return redirect(request.referrer)

    
@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})

@index_views.route('/api/workouts', methods=['GET'])
def get_workouts_action():
    workouts = list_all_workouts_json()
    return jsonify(workouts)

@index_views.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        age = int(request.form['age'])
        sex = request.form['sex']
        activity_level = request.form['activity_level']

        bmr = calculate_bmr(weight, height, age, sex)
        calories = calculate_daily_calories(bmr, activity_level)

        return render_template('result.html', calories=calories)
    

@index_views.route('/result')
def results():
    return render_template('result.html')