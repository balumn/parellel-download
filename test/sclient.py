import Broadcast
import sendtcpmsg
import time

def call():
    address=Broadcast.broadcast_recive()
    tcpaddress=str(address[0])
    print(tcpaddress)
    time.sleep(15)
    sendtcpmsg.send_tcp_message(tcpaddress)
    return address, tcpaddress

#(address, tcpaddress) = call()
#address, tcpaddress = call()