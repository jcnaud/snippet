# coding: utf-8

class Singleton(object):
    """Singleton desing pattern"""
    _instances = {}
    def __new__(class_, *args, **kwargs):
        if class_ not in class_._instances:
            print("New one")
            class_._instances[class_] = super(Singleton, class_).__new__(class_, *args, **kwargs)
            class_._instances[class_].token = None
        else:
            print("Existe")
        return class_._instances[class_]

class ServiceAuth(Singleton):
    def __init__(self):
        print("token = "+str(self.token))

    def getToken(self):
        if not self.token:
            self.requestNewToken()
        return self.token

    def requestNewToken(self):
        self.token = "TTOOKKEENN"

def main ():

    #authservice = ServiceAuth().getToken()
    print(ServiceAuth().getToken())
    print(ServiceAuth().getToken())
    print(ServiceAuth().getToken())
    print(ServiceAuth().getToken())

if __name__ == '__main__':
    main()
