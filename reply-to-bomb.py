#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"
PORT = 20207

def main():
    while True:
        try:
            s = socket.socket()
            s.bind( (HOST,PORT) )

            s.listen(1)
            conn, addr = s.accept()
            print( "Connection from: " + str(addr) )

            while True:
                data = conn.recv(1024).decode()
                print ("from connected  user: " + str(data))

                data = "OK\n\n\n"
                print ("sending: " + data)
                conn.send(data.encode())

            conn.close()
        except Exception as e:
            try:
                print(e.message)
            except:
                continue

            print("Continuing")
            continue

if __name__ == '__main__':
    main()
