#!/usr/bin/env python
# for client reply
import socket
class SendMsg:
    def send(self,address):
        TCP_IP = address
        TCP_PORT = 9001
        BUFFER_SIZE = 1024

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.43.51', TCP_PORT))
        msg="hello Sever i am client"
        s.send(msg.encode())
        s.close()
