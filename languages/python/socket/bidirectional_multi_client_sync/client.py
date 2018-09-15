# coding: utf-8

import os
import socket
import threading

def socket_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect(('',6543))
    while True:
        x = input("> ")
        if "" != x:
            sock.send(x.encode('utf-8'))
            reponse = sock.recv(1024).decode('utf-8')
            print("response: {}".format(reponse))

def main():
    socket_client()

if __name__ == "__main__":
    main()


