#!/usr/bin/env python
# for client reply
import socket
class SendMsg:
    def send(self,address):
        TCP_IP = 'localhost'
        TCP_PORT = 9001
        BUFFER_SIZE = 1024

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        addr=(TCP_IP, TCP_PORT)
        s.connect((TCP_IP, TCP_PORT))
        msg="hello Sever i am client"
        s.send(msg.encode())
        s.close()
