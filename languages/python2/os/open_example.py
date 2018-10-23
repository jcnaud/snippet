# coding: utf-8

#import os

def main():
    with open('text_example.txt', 'w') as f:
        f.write("This is a test text ")

    with open('text_example.txt', 'r') as f:
        text = f.read()

    print(text)

if __name__ == '__main__':
    main()
