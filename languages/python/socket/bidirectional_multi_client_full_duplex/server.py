# coding: utf-8

import os
import socket
import threading
import time
import logging
import threading, _thread

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Server')


class Server(object):
    """Socket server"""
    def __init__(self, host, port):
        self.size = 1024
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Enable socket reutilisability, 
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Bind
        self.sock.bind((self.host, self.port))

    def run(self):
        self.socket_listen()

    def socket_listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept() # Wait a new connection
            logger.info("Client connected from {0}:{1}".format(address[0],address[1]))
            client.settimeout(60)
            # Put the new client connection in new thread
            t = threading.Thread(target = self.oneClient,args = (client,address))
            t.daemon = True # Daemonize thread
            t.start()

    def oneClient(self, client, address):
        """
        Handle one client connection
        """
        try:
            t = threading.Thread(target = self.listenFromClient,args = (client,address))
            t.daemon = True # Daemonize thread
            t.start()
            
            self.sendToClient(client, address)
        finally:
            client.close()

    def listenFromClient(self, client, address):
        try:
            while True:
                data = client.recv(self.size) # Wait client message
                if data:
                    message = data.decode('utf-8')
                    print(message)
        except Exception as e:
            logging.exception("socket_listen : "+str(e))


    def sendToClient(self, client, address):
        try:
            while True:
                time.sleep(5)
                x="server keep alive"
                client.send(x.encode('utf-8'))
        except Exception as e:
            logger.exception("Client connexion crash : "+str(e))


def main():
    server = Server('',6543)
    server.run()


if __name__ == "__main__":
    main()
