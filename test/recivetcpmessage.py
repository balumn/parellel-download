
import socket
from MasterThread import MasterThread
from SplitDownloader import * 
import select
import merge


class recive_tcp_message:
        def __init__(self,):
            self.BUFFER_SIZE = 1024
            self.list_of_param = []
            self.threads = []
            self.sequence = 0
        def tcp_listen(self,tcpsock):
            read_list = [tcpsock]
            tcpsock.listen(1)
            print ("Waiting for incoming connections...")
            #while True:
            try:
                readable, writable, errored = select.select(read_list, [], [],1)
                for s in readable:
                    if s is tcpsock:
                        (conn, (ip,port)) = tcpsock.accept()
                        msg=conn.recv(self.BUFFER_SIZE)
                        self.sequence = self.sequence+1
                        print(msg,self.sequence)
                        
                        print("Got connection from client ",self.sequence, (ip,port))
                        self.list_of_param.append([ip,port,conn,self.sequence])
                    else:
                        pass
                            
            except socket.timeout:
                    pass
        def tcp_thread(self):    
            for i in self.list_of_param:
                print(i)
            #code to pass url here
            #@TODO get url from user
            #url='https://www.w3.org/TR/PNG/iso_8859-1.txt'
            url='https://www.codesector.com/files/teracopy.exe'
            client_url=Start_split(url,self.sequence)
            #starting threads
            for i in range(self.sequence) :
                newthread = MasterThread(self.list_of_param[i],client_url[i])
                newthread.start()
                self.threads.append(newthread)
            #for t in self.threads:
                

            for t in self.threads:
                t.join()
            merge.merge(url,self.sequence)