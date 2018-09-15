# coding: utf-8

import socket
import os


def socket_client(socket_file="/tmp/python_unix_sockets_example"):
    if os.path.exists(socket_file):
        client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        client.connect(socket_file)
        print("Ctrl-C to quit.")
        print("Sending 'DONE' shuts down the server and quits.")
        while True:
            try:
                x = input("> ")
                if "" != x:
                    print("SEND:", x)
                    client.send(x.encode('utf-8'))
                    if "DONE" == x:
                        print("Shutting down.")
                        break
            except KeyboardInterrupt as k:
                print("Shutting down.")
                client.close()
                break
    else:
        print("Couldn't Connect!")
    print("Done")


def main():
    socket_client()

if __name__ == "__main__":
    main()