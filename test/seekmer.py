import os
def create(size):
    downloadFolder = "C://Project/parellel-download"
    if not (os.path.isdir("C://Project/parellel-download")):
        os.makedirs("C://Project/parellel-download")
	#downloadPath = downloadFolder + "/" + "new_file"
    fn=open(downloadFolder+"/"+"final","wb")
    fn.write(b"\0" * size)
    fn.close()


def replace(offset,data):
    downloadFolder = "C://Project/parellel-download"
    fn=open(downloadFolder+"/"+"final","r+b")
    fn.seek(offset)
    fn.write(data)
    print("from file seek:",data)
    fn.close()
#create(44400)



