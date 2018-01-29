#!/bin/python
# coding: utf-8

import re

def main():
    regex = re.compile(r"^\s*the bad things\s*$", re.IGNORECASE)

    data="    THe BaD tHinGs    "
    result = regex.sub("the good things", data)
    print(result)

    print(" === End of this programme ===")   

if __name__ == "__main__":
    main()