# coding: utf-8

def job(q_parent, q_self):

    while True:
        print("run job")
        message = q_self.get()
        res = "job : "+str(message)
        q_parent.put(res) 