
import socket

def recive_tcp_message():
        TCP_IP = ''
        TCP_PORT = 9001
        BUFFER_SIZE = 1024

        tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcpsock.bind((TCP_IP, TCP_PORT))
        while True:
            tcpsock.listen(5)
            print ("Waiting for incoming connections...")
            (conn, (ip,port)) = tcpsock.accept()
            msg=conn.recv(BUFFER_SIZE)
            print ('Got connection from ', (ip,port))
            print(msg)