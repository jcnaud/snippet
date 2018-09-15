# coding: utf-8
import traceback
import sys
import json


def operation():
    a = 'a'
    try:
        result = 1/0
    except Exception as e:

        # Direct print
        # traceback.print_exc()

        # # All in string
        # var = traceback.format_exc()
        # print(var)

        # # Manual
        # t, v, tb = sys.exc_info()
        # print(t.__name__) # <type> to str
        # print(v)          # str message
        # traceback.print_tb(tb)  # tb object

        # Extraction
        t, v, tb = sys.exc_info()
        #print(traceback.extract_tb(tb))

        # Print de la stack actuel
        #traceback.print_stack()
        #print(traceback.extract_stack())

        st = traceback.extract_stack()
        print(traceback.format_list(st))
        print("  locals  ")
        print(locals())
        print("  globals  ")
        print("===========")
        print(globals())


if __name__ == '__main__':
    operation()
