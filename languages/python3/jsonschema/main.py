#!/usr/bin/env python
# coding: utf-8

import os
import yaml
from jsonschema import validate

def main():
    file_conf="file_conf.yml"

    # == Open configuration file ==
    with open(file_conf, "r") as f:
        conf_not_valided = yaml.load(f)

    # schema
    schema = {
        "$schema": "http://json-schema.org/draft-06/schema#",
        "title": "Users list",
        "description": "List of users with description",
        "type" : "object",
        "properties" : {
            "users" : {
                "type" : "array",
                "items": {
                    "type": "object",
                    "properties" : {
                        "name" : {
                            "description": "Name of the user",
                            "type": "string"
                        },
                        "age" : {
                            "description": "Age of the user",
                            "type": "integer"
                        },
                        "state" : {
                            "description": "State of the user",
                            "type": "string"
                        }
                    },
                    "required": [ "name", "age" ],
                    "additionalProperties": False
                },
                "minItems": 1,
                "uniqueItems": True
            }
        },
        "required": [ "users" ],
        "additionalProperties": False
    }

    # If no exception is raised by validate(), the instance is valid.
    validate(conf_not_valided, schema)

    print("Conf is valid")

    print(" === End of this programme ===")    


if __name__ == "__main__":
    main()

