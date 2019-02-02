#!/usr/bin/env python

import socket

def send_tcp_message(tcpaddress):
        TCP_IP = tcpaddress
        TCP_PORT = 9001
        BUFFER_SIZE = 1024
        msg=b"hello Sever i am client"
        print(TCP_IP,TCP_PORT)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP,TCP_PORT))
        s.send(msg.encode())
        s.close()
