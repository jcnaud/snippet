#!/bin/python
# coding: utf-8

import re

def main():
    print(" === Mono ligne and Mono research === ")  

    res = re.fullmatch("abcdecfc", "abcdecfc") # Match 
    print(res)
    res = re.fullmatch("abcdecf", "abcdecfc") # Not match because need to match totaly
    print(res)
    res = re.match("a", "abcdef")     # Match
    print(res)
    res = re.match("c", "abcdef")     # Not match because implicitly start at the begining of the string
    print(res)
    res = re.search("c", "abcdef")    # Match
    print(res)
    res = re.search("^c", "abcdef")   # Not Match
    print(res)
    res = re.search("^a", "abcdef")   # Match with group
    print(res)
    print(res.group(0)) # Display matching


    print(" === Multi ligne and Mono research === ")

    res = re.match('X', 'A\nB\nX', re.MULTILINE)    # No match because implicitly start at the begining of the string (not the ligne)
    print(res)
    res = re.search('^X', 'A\nB\nX', re.MULTILINE)  # Match because ^ specify the begining of the ligne
    print(res)


    print(" === Mono ligne and Multi research === ")  

    res = re.search("c", "abcdecfc")    # Match Just the first
    print(res)
    res = re.findall("c", "abcdecfc")   # Match all and put in <list>
    print(res)    
    res = re.finditer("c", "abcdecfc")  # Match all with yield (generator)
    print(res) 
    for m in res:
        print("    "+str(m))


    print(" === Multi ligne and Multi research === ")

    res = re.search('^X', 'A\nB\nX\nX\nX', re.MULTILINE)  # Match Just the first
    print(res)
    res = re.findall('^X', 'A\nB\nX\nX\nX', re.MULTILINE)  # Match all and put in <list>
    print(res)
    res = re.finditer('^X', 'A\nB\nX3\nX5\nX6', re.MULTILINE)  # Match all with yield (generator)
    print(res) 
    for m in res:
        print("    "+str(m))


    print(" === Groupindex example === ")
    res = re.finditer(r"(?P<name>^X)", 'A\nB\nX\nX\nX', re.MULTILINE)  # Match with groupindex
    print(res)
    for m in res:
        print("    "+str(m.group("name"))) # Display matching


    print(" === End of this programme ===")   

if __name__ == "__main__":
    main()