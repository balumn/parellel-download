import os.path
import sys
import shutil

#i=recive_tcp_message.sequence
def merge(url,seq):
    i=1
    buffer_size=8192
    downloadname =str(url.split('/')[-1])#gives proper filename
    downloadFolder = "c://project/parellel-download"
    downloadPath = downloadFolder + "/" + "new_file"
    fdst=open(downloadFolder+"/"+downloadname,"wb")
    while(i<=seq):
        if (os.path.isfile(downloadPath+str(i))): 
            fsrc=open(downloadPath+str(i),"rb")
            print("merging...file from client",i)
            shutil.copyfileobj(fsrc,fdst,buffer_size)
            #dt=g.read()
            #fn.write(dt)
            print("client ",i,"file merged")

            i=i+1
        else:
            print("file from client",i,"is missing program is exiting..." )
            sys.exit(0)
            break
    #fsrc.close()
    fdst.close()
    print("Hurray!!!  completed succesfully....")
#merge(3)