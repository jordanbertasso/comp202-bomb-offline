#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"
PORT = 20207
OK_SIGNAL = b"OK\n\n\n"

def main():
    with socket.socket() as server:
        server.bind((HOST, PORT))
        server.listen(1)

        while True:
            client, addr = server.accept()
            print(f"Connection: {addr}")

            with client:
                data = client.recv(1024)
                print(f"Recieved: {data}")
                try:
                    print(f"@'''\n{data.decode()}\n'''@")
                except UnicodeDecodeError:
                    pass

                client.send(OK_SIGNAL)

            print()

if __name__ == '__main__':
    main()
