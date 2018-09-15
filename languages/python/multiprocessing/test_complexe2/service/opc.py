# coding: utf-8
from multiprocessing import Process
import logging

class Opc(Process):
    def __init__(self, q_parent, q_self):
        super(Opc, self).__init__()
        self.q = {}
        self.q["parent"] = q_parent
        self.q["self"] = q_self

    def run(self):
        """Main multiprocess routine"""
        while True:
            try:
                message = self.q["self"].get()
                self.handler(message)
            except Exception as e:
                logging.error(e)

    def handler(self, message):
        """Message handler"""
        try:
            m_type = message["type"]
            if m_type == "cmd":
                self.command(message)
            elif m_type == "req":
                self.request(message)
            elif m_type == "rep":
                self.reponse(message)
            else:
                assert False, "message type non supporté : %s " % m_type
        except Exception as e:
            logging.error(e)

    def command(self, message):
        """Commande message"""
        res = "opc : "+str(message)
        self.q["parent"].put(res)

    def request(self, message):
        """request message"""
        res = "opc : "+str(message)
        self.q["parent"].put(res)

    def reponse(self, message):
        """reponse message"""
        print("réponse bien reçu")
