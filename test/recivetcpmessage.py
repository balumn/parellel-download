
import socket
from MasterThread import MasterThread
from SplitDownloader import * 

def recive_tcp_message():
        TCP_IP = ''
        TCP_PORT = 9001
        BUFFER_SIZE = 1024
        list_of_param = []
        threads = []
        sequence = 0

        tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcpsock.bind((TCP_IP, TCP_PORT))
        while True:
            tcpsock.listen(5)
            print ("Waiting for incoming connections...")
            (conn, (ip,port)) = tcpsock.accept()
            msg=conn.recv(BUFFER_SIZE)
            print(msg)
            sequence = sequence+1
            print('Got connection from ', (ip,port))
            list_of_param.append([ip,port,conn,sequence])
            break
            
        for i in list_of_param:
            print(i)
        #code to pass url here
        #@TODO get url from user
        url='https://www.w3.org/TR/PNG/iso_8859-1.txt'
        client_url=Start_split(url,sequence)
        #starting threads
        for i in range(sequence) :
            newthread = MasterThread(list_of_param[i],client_url[i])
            newthread.start()
            threads.append(newthread)
        
        for t in threads:
          t.join()