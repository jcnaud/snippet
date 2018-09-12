"""
Created on February 2018
@author: Jean-Charles Naud
"""

# coding: utf-8


class MyModule(object):
    """
    MyModule test
    """

    def __init__(self):
        """
        Init
        """
        pass
    
    def format_message(self, message):
        """
        Function formating the message

        :Example:

        >>> mm = MyModule()
        >>> mm.format_message("message")
        'message_format'

        """

        return message+"_format"

def _test():
    """
    Test
    """
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()


# python mymodule.py
# python mymodule.py -v

# python
# from mymodule import MyModule
# help(MyModule)
# print(MyModule.__doc__)
# print(MyModule.format_message.__doc__)
