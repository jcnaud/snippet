# coding: utf-8

import os
import socket
import threading

class ThreadedServer(object):
    """
    Socket server where many client CLI can connect to use the OPC UA Client
    """
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Enable socket reutilisability, 
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Bind
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept() # Wait a new connection
            print("Client connected from {0}:{1}".format(address[0],address[1]))
            client.settimeout(60)
            # Put the new client connection in new thread
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        """
        Handle one client connection
        """
        size = 1024
        try:
            while True:
                data = client.recv(size) # Wait client message
                if data:
                    # Parse command
                    response = data
                    client.send(response)
                else:
                    print("Client disconnected from {0}:{1}".format(address[0],address[1]))
                    break
        finally:
            client.close()
            return False

def main():

    # Run server thread and listen on 0.0.0.0:6543
    ThreadedServer('',6543).listen()

if __name__ == "__main__":
    main()
