#!/usr/bin/env python
# coding: utf-8
import requests

class MyModule(object):
    def __init__(self):
        pass
    
    def format_message(self, message):
        return message+"_format"

    def get_url_code(self):
        r = requests.get('http://www.example.comdfgfdd/')
        return r.status_code