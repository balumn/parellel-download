#!/usr/bin/env python3

import socket
import traceback
import os
# import sendmsg

host = ''
port = 10100
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host,port))
while 1:
    try:
        message, address = s.recvfrom(port)
        print("Got data from", address)
        TCP_IP = 'localhost'
        TCP_PORT = 9001
        BUFFER_SIZE = 1024

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        addr=(TCP_IP, TCP_PORT)
        s.connect((TCP_IP, TCP_PORT))
        msg="hello Sever i am client"
        s.send(msg.encode())
        s.close()
    except (KeyboardInterrupt, SystemExit):      
        raise
    except:
        traceback.print_exc()
        break
s.close()