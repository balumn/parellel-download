import socket
import time


def broadcast_recive():
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        client.bind(('', 37020))
        while True:
            data, addr = client.recvfrom(1024)
            print("received message: %s"%data)
            print("recived from :",addr)
            break
        return addr
def broadcast_send():
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # Set a timeout so the socket does not block
        # indefinitely when trying to receive data.
        server.settimeout(0.02)
        server.bind(("", 44444))
        message = b"your very important message"
        timeout = 20   # [seconds]
        timeout_start = time.time()
        while time.time() < timeout_start + timeout:
            server.sendto(message, ('<broadcast>', 37020))
            print("message sent!")
            time.sleep(1)