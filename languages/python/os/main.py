# coding: utf-8
import os

def main():


    file_path = '.'+os.sep+'main.py'
    dir_path = '.'

    if os.path.exists(file_path):
        print(file_path+' exist')


    if os.path.exists(dir_path):
        print(file_path+' exist')

    # Dir path of this file
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    

if __name__ == '__main__':
    main()
