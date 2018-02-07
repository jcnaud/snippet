#!/usr/bin/env python
# coding: utf-8

import os
import yaml
from schema import Schema, And, Use, Optional

def main():
    file_conf="file_conf.yml"

    # == Open configuration file ==
    with open(file_conf, "r") as f:
        conf_not_valided = yaml.load(f)

    dict_schema = {
        "users" : [
            {
                "name" : And(str, len),
                "age" : And(Use(int), lambda n: n >= 18),
                "state" : Use(str.lower)
            }
        ]
    }

    schema = Schema(dict_schema)
    conf_validated = schema.validate(conf_not_valided)

    print(conf_validated)

    print(" === End of this programme ===")    


if __name__ == "__main__":
    main()

