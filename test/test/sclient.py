import Broadcast
import sendtcpmsg

address=Broadcast.broadcast_recive()
tcpaddress=str(address[0])
print(tcpaddress)
sendtcpmsg.send_tcp_message(tcpaddress)