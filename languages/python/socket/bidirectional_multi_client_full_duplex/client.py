# coding: utf-8

import os
import socket
import threading
import time
import logging
import threading
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Client')


class Client(object):

    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host,port))
        self.size = 1024
        self.isstart = True
        #self.stop = threading.Event()

    def run(self):
        """run"""
        logger.info("run")
        try:
            t = threading.Thread(target=self.socket_listen)
            t.daemon = True # Daemonize thread
            t.start()
            #self.socket_listen()
            self.socket_send()
        finally:
            self.sock.close() # Close the socket

    def socket_listen(self):
        """socket_listen"""
        logger.info("socket_listen")
        try:
            try:
                while self.isstart:
                    data = self.sock.recv(self.size) # Wait client message
                    message_s = data.decode('utf-8')
                    print(message_s)
            except Exception as e:
                logging.exception("socket_listen : "+str(e))
        finally:
            self.sock.close()
            logging.info("Client disconnected")


    def socket_send(self):
        while self.isstart:
            time.sleep(0.5)
            message={
                'type': 'req',
                'mes': 'The client'}
            message_s = json.dumps(message)
            self.sock.send(message_s.encode('utf-8'))


def main():
    client = Client('',6543)
    client.run()

if __name__ == "__main__":
    main()


