import Broadcast
import sendtcpmsg
import time

address=Broadcast.broadcast_recive()
tcpaddress=str(address[0])
print(tcpaddress)

sendtcpmsg.send_tcp_message(tcpaddress)