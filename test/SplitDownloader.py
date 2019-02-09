import urllib.request
import urllib.response
import os

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
        
        print(" N-Division requests")
        print("\tNo. of clients:",client_count)
        print("\tFileSize in bytes:",contentlength)
        urlRangeList = n_division(client_count,contentlength)
        for a in urlRangeList:
            print(a)
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


# USAGE of requests on client side
# a='bytes=0-4967'
# req = urllib.request.Request(url, headers={'Range':x})
# data = urllib.request.urlopen(req).read()
# print(data)

# INTEGRATION
# for x in urlRangeList:
#     ss =urllib.request.Request(url, headers={'Range':x})
#     data = urllib.request.urlopen(ss).read()
#     requests.append(data)
#     with open(writepath,mode) as f:
#         f.write(data)
# for a in requests:
#     print(a)