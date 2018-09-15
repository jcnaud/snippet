#!/usr/bin/env python
# coding:utf-8

from flask import Flask, request


import threading
import time

global_value = "voila"



def worker(global_value):
    time.sleep(5)
    global_value = "HAHAHA"

t = threading.Thread(target=worker,args=(global_value))
t.setDaemon(True)
t.start()


app = Flask(__name__)

@app.route('/')
def hello_world():
    return global_value
    #return 'Hello, World!'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "login POST"
    else:
        return "login GET"

if __name__ == "__main__":
    app.run(
        debug=False,
        host="127.0.0.1",
        port=5000
    )

    print(app)
