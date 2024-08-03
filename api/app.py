from flask import Flask, Blueprint, make_response, jsonify
import requests
import sqlite3
from api.db import get_db, init_db, get_user, create_user

# Generates a blueprint for routing and registering routes with the app factory
bp = Blueprint('api', __name__)

def generate_avatar_url():
    response = requests.get('https://randomuser.me/api/')
    data = response.json()
    return data['results'][0]['picture']['large']

users = [
        {
            'id': 1,
            'status': 'active',
            'name': 'Paula Abdul',
            'hobbies': ['singing', 'dancing'],
            'groups': ['trekking', 'cooking'],
            'interests': ['music', 'sports'],
            'about': 'I am a singer and dancer',
            'imageUrl': generate_avatar_url()
        },
        {
            'id': 2,
            'status': 'active',
            'name': 'Jimmy Abdul',
            'hobbies': ['singing', 'dancing'],
            'groups': ['trekking', 'cooking'],
            'interests': ['music', 'sports'],
            'about': 'I wish I was Paula Abdul\'s brother',
            'imageUrl': generate_avatar_url()
        },
        {
            'id': 3,
            'status': 'inactive',
            'name': 'Henry Abdul',
            'hobbies': ['singing', 'dancing'],
            'groups': ['trekking', 'cooking'],
            'interests': ['music', 'sports'],
            'about': 'I am Paula Abdul\'s brother',
            'imageUrl': generate_avatar_url()
        },
        {
            'id': 4,
            'status': 'active',
            'name': 'Lenny Kravitz',
            'hobbies': ['singing', 'guitar'],
            'groups': ['trekking', 'cooking'],
            'interests': ['music', 'sports'],
            'about': 'I am a rockstar',
            'imageUrl': generate_avatar_url()
        },
        {
            'id': 5,
            'status': 'active',
            'name': 'Jimmy Hendrix',
            'hobbies': ['singing', 'guitar'],
            'groups': ['trekking', 'cooking'],
            'interests': ['music', 'sports'],
            'about': 'I am a rockstar',
            'imageUrl': generate_avatar_url()
        },
        {
            'id': 6,
            'status': 'inactive',
            'name': 'Hedy Lamar',
            'hobbies': ['singing', 'dancing'],
            'groups': ['trekking', 'cooking'],
            'interests': ['movies', 'sports'],
            'about': 'I am an actress',
            'imageUrl': generate_avatar_url()
        },
]

formatted_users =[
    {
        #"id": 1,
        "username": "paula_abdul",
        "email": "paula@hi5ive",
        "password_hash": "paula123",
        "first_name": "Paula",
        "last_name": "Abdul",
        "bio": "I am a singer and dancer",
        "profile_picture": generate_avatar_url(),
        "location": "New York"
    }
]
# CREATE Table Users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     username TEXT UNIQUE NOT NULL,
#     email TEXT UNIQUE NOT NULL,
#     password_hash TEXT NOT NULL,
#     first_name TEXT NOT NULL,
#     last_name TEXT NOT NULL,
#     bio TEXT,
#     profile_picture TEXT,
#     location TEXT
# );

@bp.route('/user/<int:user_id>')
def get_user(user_id):
    db = get_db()
    user = db.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
    # user = None
    # for user in users:
    #     if user['id'] == user_id:
    #         break
    db.close()

    user = dict(user) if user else None
    # print(user) #* diagnostic print to terminal
    if user:
        return make_response(jsonify(user), 200)
    else:
        return make_response(jsonify({'error': 'User not found'}), 404)

@bp.route('/users')
def get_users():
    return make_response(jsonify(users), 200)


