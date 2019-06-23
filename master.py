import socket 
import select
from threading import Thread
import os
import urllib.request
import urllib.response
import sys
import shutil
import time
from tkinter import ttk
#######################################################################################################################
####################### GUI ###########################################################################################
#######################################################################################################################
import tkinter as tk # this is for python3
import tkinter.scrolledtext as st
import tkinter.filedialog as fd

urlVar = ""
def dirBox():
    global dpath
    text = fd.askdirectory(title = "Download Path")
    text = text + "/"
    print(text)
    dpath = str(text)

def hereWeGo():
    broadcast_send()

def start_client():
    root.destroy()
    from client import hereServe
 
class Application(tk.Frame):
    def smaster(self):               #enter code to trigger master mode
        print("\n\tWelcome to PDS Downloader.\nSearching for downloading clients\n\n")
        global urlVar
        urlVar = self.entry.get("1.0","end-1c")
        print(urlVar)
        hereWeGo()

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        # entry
        frame2 = tk.Frame(master = root)
        frame2.place(x=80,y=200)
        self.entry = tk.Text(master = frame2,width  = 45,height = 1)
        self.entry.pack()
        # button
        ok = tk.Button(root, text='Download',command=self.smaster)
        ok.place(x=570,y=200)
        # logging
        frame1 = tk.Frame(master = root)
        frame1.place(x=80,y=250)
        hello = "Insert a link and click download !"
        self.editArea = st.ScrolledText(master = frame1,wrap = tk.WORD,width  = 58,height = 5)
        self.editArea.pack()
        # Adding some text, to see if scroll is working as we expect it
        self.editArea.insert(tk.INSERT,hello)
    def insert(self,content):
        self.editArea.insert(tk.END,content)
        self.editArea.see(tk.END)
        self.editArea.update()
   
def display_about(self):                      #enter about details here
    print("Add about here")

def progressbar(filesize,client):
        RootWindow = tk.Tk() 
        RootWindow.title("FileTransfer Progress for Client "+str(client))
        RootWindow.geometry("500x100")
        RootWindow.resizable(0,0)
        print("frame creating\n")
        
        #FrameLink = tk.Frame(master=RootWindow)
        #FrameLink.pack_propagate(0) #Don't allow the widgets inside to determine the frame's width / height
        #FrameLink.pack(fill=tk.BOTH,padx=100,pady=100,ipady=30,ipadx=100) #Expand the frame to fill the root window
        x = tk.Label(master=RootWindow,text="Reciving part from client :"+str(client)).pack(side=tk.TOP)
        #image_logos = tk.PhotoImage(file="./logo.png")
        #label2 = tk.Label(master=RootWindow,image=image_logo).pack(side=tk.TOP)
        
        #var = tk.StringVar()
        #LabelLink = tk.Label( master=RootWindow, textvariable=var )
        #var.set("Reciving part from client :"+str(client))
        #LabelLink.pack(side=tk.TOP)
        #app.entry.destroy()
        print("prog hello")
        progress = ttk.Progressbar(master =RootWindow, orient="horizontal",length=350, mode="determinate")
        progress.place(x=80,y=50)
        progress["value"] = 0
        maxbytes = filesize
        progress["maximum"] = filesize
        print("progress hello")
        #RootWindow.mainloop()
        return progress
dpath = ""
newLength = 0
root = tk.Tk()
root.geometry("800x400")
root.title("PDS - Master")
img = tk.PhotoImage(file='./logo.png')
root.tk.call('wm', 'iconphoto', root._w, img)
x = tk.Label(root,text='Welcome to PDS App! Enjoy!').pack(side=tk.TOP,padx=10,pady=10)
image_logo = tk.PhotoImage(file="./logo.png")
label1 = tk.Label(image=image_logo)
label1.pack()
# class call
app = Application(master=root)
# menu
menu = tk.Menu(root)
root.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
# filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Download Path", command=dirBox)
filemenu.add_command(label="Go Client Mode", command=start_client)
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=display_about)



#######################################################################################################################
####################### GUI ENDS ######################################################################################
#######################################################################################################################


def broadcast_send():
        passin = "\nbrodcast messages sending!"
        app.insert(passin)
        rtm=recive_tcp_message()
        tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcpsock.bind(('', 9001))
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        server.settimeout(0.02)
        server.bind(("", 44444))
        message = b"broadcast from server"
        timeout = 20   # [seconds] #################################################################### Timeout
        timeout_start = time.time()
        while time.time() < timeout_start + timeout:
            server.sendto(message, ('<broadcast>', 37020))
            print("brodcast message sent!")
            #time.sleep(1)
            rtm.tcp_listen(tcpsock)
        if rtm.sequence != 0 :
            rtm.tcp_thread()
        else :
            print("Search failed no client devices found")
            app.insert("\nSearch failed no client devices found")  

class recive_tcp_message:
        def __init__(self,):
            self.BUFFER_SIZE = 1024
            self.list_of_param = []
            self.threads = []
            self.sequence = 0
        def tcp_listen(self,tcpsock):
            read_list = [tcpsock]
            tcpsock.listen(1)
            logArray = []
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
                        addr = list((ip,port))
                        print(addr)
                        print("Got connection from client ",self.sequence, addr)
                        log = "\nGot connection from client "+ str(addr[0]) + " on " + str(addr[1])
                        logArray.append(log)
                        self.list_of_param.append([ip,port,conn,self.sequence])
                    else:
                        pass
                for log in logArray:        
                    app.insert(log)
            except socket.timeout:
                    pass
        def tcp_thread(self):    
            for i in self.list_of_param:
                print(i)
            #code to pass url here
            #@TODO get url from user
            #url='https://www.w3.org/TR/PNG/iso_8859-1.txt'
            # url='https://www.codesector.com/files/teracopy.exe'
            #url=https://dl.google.com/go/go1.12.4.windows-amd64.msi
            url = urlVar
            start=time.time()
            client_url=Start_split(url,self.sequence)   #splitDownloader
            #starting threads
            for i in range(self.sequence) :
                newthread = MasterThread(self.list_of_param[i],client_url[i])
                newthread.start()
                self.threads.append(newthread)

            for t in self.threads:
                t.join()
            merge(url,self.sequence)
            end=time.time()
            print(end-start)


     

class MasterThread(Thread):
    

    def __init__(self,param,url): #recives a tuple param from listofparam and a list clientlist
        Thread.__init__(self)
        self.ip = param[0]
        self.port = param[1]
        self.sock = param[2]
        self.sequence = param[3]
        self.url = url[0]
        self.byte = url[1]
        print(" New thread started for "+self.ip+":"+str(self.port))
        app.insert(" \nNew thread started for "+self.ip+":"+str(self.port))
        app.insert("\nURL send to client waiting for client to download")
    def run(self):
         read_list = [self.sock]   
         
         print(self.url)
         self.sock.send(self.url.encode())
         print(self.byte)
         self.sock.send(self.byte.encode())
         def copyfileobj(fsrc, fdst, length):
            """copy data from file-like object fsrc to file-like object fdst"""
            print("obj hello")
            data = b''
            arr=str(self.byte).split('-')
            print(arr)
            up=int(arr[1])
            print(up)
            arr2=arr[0].split('=')
            print(arr2)
            low=int(arr2[1])
            print(low)
            contentlength=up-low
            print(contentlength)
            progress=progressbar(contentlength,self.sequence)
            global file
            while 1:
                try:
                    part = self.sock.recv(length)
                    #data += part
                    fdst.write(part)
                    file=fdst.tell()
                    progress["value"] = file
                    progress.update()
                    print(file)
                    if not part:
                        break
                    #raise ConnectionError
                    #progress.destroy()
           
                finally:
                    pass
                    #progress.destroy()
         #def recvall(sock):
         #   BUFF_SIZE = 4096 # 4 KiB
         #   data = b''
         #   while True:
         #       part = sock.recv(BUFF_SIZE)
         #       data += part
         #       if not part:
         #           break
         #   return data
         readable, writable, errored = select.select(read_list, [], [])   
         for s in readable:
             if s is self.sock:
                downloadPath = dpath
                file=0
                with self.sock as fsrc,open(downloadPath+str(self.sequence),"wb")as fdst:
                    print("recving..\n")
                    copyfileobj(fsrc,fdst,16*1024)
                #part=recvall(self.sock)
                # enikk folder venda
                # downloadFolder = "C://Project/parellel-download"
                # if not (os.path.isdir("C://Project/parellel-download")):
                #     os.makedirs("C://Project/parellel-download")
                # downloadpath = downloadFolder + "/" + "new_file"   
                #downloadPath = dpath
                #f=open(downloadPath+str(self.sequence),"wb")
                #print("data from client",self.sequence,"is received")
                #f.write(part)
                print("data from client",self.sequence,"is written to file")
                # app.insert("data from client" + str(self.sequence) + "is written to file")
                fdst.close()
                #print(part)

class HeadRequest(urllib.request.Request):
    def get_method(self):
        return "HEAD"

def n_division(client_count,contentlength):
    lis=[]
    segmentSize=int(contentlength/client_count)
    top=segmentSize
    s='bytes=0-'+str(segmentSize)
    lis.append(s)
    for i in range(client_count-1):
        newTop=top+segmentSize
        s='bytes='+str(top+1)+"-"+str(newTop)
        lis.append(s)
        top=newTop
    return lis
def Start_split(url,client_count):
        url = url
        client_count = client_count
        writepath = 'file.txt'
        mode = 'ab' if os.path.exists(writepath) else 'wb+'
        req = HeadRequest(url)
        response = urllib.request.urlopen(req)
        response.close()
        print("Fileinfo ==>")
        print(response.info())
        strRes = str(response.info())
        contentlength=int(response.getheader("Content-Length"))
        global newLength
        newLength = contentlength
        print("N-Division requests")
        print("\tNo. of clients:",client_count)
        print("\tFileSize in bytes:",contentlength)
        # logging
        app.insert("\nN-Division requests")
        app.insert("\n\tNo. of clients:" + str(client_count))
        app.insert("\n\tFileSize in bytes:" + str(contentlength))
        #seekmer.create(contentlength)
        #print("sample file of content length created")
        urlRangeList = n_division(client_count,contentlength)
        for a in urlRangeList:
            print(a)
            app.insert("\n" + a)
        requests = []
        for x in urlRangeList:
            ss = "urllib.request.Request(" + url + ", headers={'Range':" + x + "})"
            requests.append(ss)
        # pass urlRangeList[i] to the clients_list[i]
        for i in range(client_count):
            clients = [[url,xx] for xx in urlRangeList]

        for test in clients:
            print (test)


        print("done")
        return clients

def merge(url,seq):
    i=1
    buffer_size=8192
    downloadname =str(url.split('/')[-1])
    # downloadFolder = "c://project/parellel-download"
    # downloadPath = downloadFolder + "/" + "new_file"
    downloadPath = dpath
    print(dpath)
    fdst=open(dpath + downloadname,"wb")
    flag=False
    while(i<=seq):
        if (os.path.isfile(downloadPath+str(i))): 
            fsrc=open(downloadPath+str(i),"rb")
            print("merging...file from client",i)
            app.insert("\nmerging...file from client "+ str(i))
            shutil.copyfileobj(fsrc,fdst,buffer_size)
            #dt=g.read()
            #fn.write(dt)
            print("client ",i,"file merged")
            app.insert("\nclient "+str(i)+" file merged")
            flag=True
            i=i+1
        else:
            flag=False
            print("file from client",i,"is missing program is exiting..." )
            app.insert("file from client "+str(i)+" is missing program is exiting...")
            sys.exit(0)
            break
    #fsrc.close()
    len2=fdst.tell()
    fdst.close()
    len3=newLength-len2
    if flag and (len3<20) :  
        print("Hurray!!!  completed succesfully....")
        app.insert("\nHurray!!!  completed succesfully....")
    else:
        print("OP")

app.mainloop()
root.destroy()