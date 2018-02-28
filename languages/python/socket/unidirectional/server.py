# coding: utf-8

import socket
import os


def socket_server(socket_file="/tmp/python_unix_sockets_example"):
    """Socket UNIX server creation/connection (generator mode)"""
    # Clean
    if os.path.exists(socket_file):
        os.remove(socket_file)

    # Create socket UNIX DGRAM
    server = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    server.bind(socket_file)

    # Listen/connect to socket (generator mode)
    try:
        while True:
            datagram = server.recv(1024) # get datagram by generator
            if not datagram:
                break
            yield datagram.decode('utf-8')
    finally:
        # Close and clean the socket UNIX DGRAM
        server.close()
        os.remove(socket_file)


def main():
    """Entry point to start the socket server"""
    # Socket server
    for data in socket_server():
        if "DONE" == data:
            break # Server will shutdown gracefully
        else:
            print(data)

if __name__ == "__main__":
    main()