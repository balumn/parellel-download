import Broadcast
import sendtcpmsg
import time

address=Broadcast.broadcast_recive()
tcpaddress=str(address[0])
print(tcpaddress)
time.sleep(15)
sendtcpmsg.send_tcp_message(tcpaddress)