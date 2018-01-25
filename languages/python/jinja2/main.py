#!/usr/bin/env python
# coding: utf-8

import os
from jinja2 import Template


def main():
    file_template="file.conf.j2"

    # == Open template file ==
    with open(file_template) as file:  
        data = file.read()

    template = Template(data)

    context = {
        'user' : 'myUser',
        'IPs' : [
            '192.168.0.1', '192.168.0.2'
        ]
    }

    file_conf = template.render(context)
    
    print(file_conf)

    print(" === End of this programme ===")    


if __name__ == "__main__":
    main()

