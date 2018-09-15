
#!/usr/bin/env python
# coding:utf-8
from __future__ import unicode_literals

import threading
import time

import multiprocessing

import gunicorn.app.base

from gunicorn.six import iteritems


from flask import Flask, request
app = Flask(__name__)



global_value = 'Hello, World !'


#@app.route('/')
def hello_world():
    return global_value

# Without decorator
app.route('/')(hello_world)

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


class StandaloneApplication(gunicorn.app.base.BaseApplication):

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(StandaloneApplication, self).__init__()

    def load_config(self):
        config = dict([(key, value) for key, value in iteritems(self.options)
                       if key in self.cfg.settings and value is not None])
        for key, value in iteritems(config):
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


def worker(sa):
    time.sleep(3)
    print('worker')
    global global_value
    global_value = "HAHAHA"
    global sa
    sa.reload()
    print('sa reload')


if __name__ == '__main__':
    options = {
        'bind': '%s:%s' % ('127.0.0.1', '5000'),
        'workers': 2,
        'reload' : True
    }

    print('before : '+global_value)


    sa = StandaloneApplication(app, options)
    print(str(sa.__dict__))
    import inspect
    import json

    inspect.getmembers(gunicorn.app.base.BaseApplication)


    t = threading.Thread(target=worker,args=(sa,))
    t.setDaemon(True)
    t.start()

    #time.sleep(5)
    print('after : '+global_value)
    sa.run() # Blocking step

reload
