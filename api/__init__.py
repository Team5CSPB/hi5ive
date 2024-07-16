from flask import Flask
import os

app = Flask(__name__)

@app.route('/user')
def get_user():
    return {'user': 'Paula Abdul'}

@app.route('/home')
def get_home():
    return b"Welcome home!"

@app.route('/sign_up')
def get_sign_up():
    
    return b"Sign up here!"