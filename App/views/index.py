from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from flask_jwt_extended import jwt_required, current_user, unset_jwt_cookies, set_access_cookies
from App.models import db
from App.controllers import(
    create_user, 
    list_all_workouts, 
    list_all_workouts_json, 
    list_workouts_by_body_part,
    list_workouts_by_level,
    list_workouts_by_type

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
    return render_template('routine.html')
    
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
