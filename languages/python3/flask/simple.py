#!/usr/bin/env python
# coding:utf-8

from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/geterror/<int:error_id>')
def geterror():
    response = jsonify({'message':'you have the error %d' % error_id})
    return response, error_id

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "login POST"
    else:
        return "login GET"
