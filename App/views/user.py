from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user, set_access_cookies

from.index import index_views

from App.controllers import (
    create_user,
    get_all_users,
    get_all_users_json,
    jwt_required,
    get_user_by_username,
    login
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

@user_views.route('/signup', methods=['GET'])
def signup_page():
    return render_template('signup.html')

@user_views.route('/create', methods=['POST'])
def create_user_action():
    data = request.form
    user = get_user_by_username(data['username'])
    response = redirect(url_for('index_views.home_page'))
    if not user:
        flash(f"User {data['username']} created!")
        create_user(data['username'], data['password'])
        token = login(data['username'], data['password'])
        set_access_cookies(response, token) 
        return response
    else:
        flash('User already exists')
        return render_template('signup.html')

@user_views.route('/api/users', methods=['GET'])
def get_users_action():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/api/users', methods=['POST'])
def create_user_endpoint():
    data = request.json
    user = create_user(data['username'], data['password'])
    return jsonify({'message': f"user {user.username} created with id {user.id}"})

@user_views.route('/static/users', methods=['GET'])
def static_user_page():
  return send_from_directory('static', 'static-user.html')