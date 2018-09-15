# coding: utf-8

def cli(q_parent, q_self):
    while True:
        print("run cli")
        message = q_self.get()
        res = "cli : "+str(message)
        q_parent.put(res)