from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from flask_jwt_extended import jwt_required, current_user, unset_jwt_cookies, set_access_cookies
from App.models import db
from App.controllers import create_routine

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

@index_views.route('/create-routine', methods=['POST'])
@jwt_required()
def create_routine_route():
    name = request.form.get('routine-name')
    new_routine = create_routine(name)
    if new_routine:
        return jsonify(message="Routine created successfully"), 201
    else:
        return jsonify(message="Failed to create routine"), 400

@index_views.route('/edit-routine', methods=['POST'])
@jwt_required()
def edit_routine_route():
    routine_id = request.form.get('routine-id')
    routine = get_routine_by_id(routine_id)
    if routine:
        pass
    else:
        return jsonify(message="Routine not found"), 404

@index_views.route('/delete-routine', methods=['POST'])
@jwt_required()
def delete_routine_route():
    routine_id = request.form.get('routine-id')
    routine = get_routine_by_id(routine_id)
    if routine:
        pass
    else:
        return jsonify(message="Routine not found"), 404






    
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
