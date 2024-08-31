import socket
import threading

reciever = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
reciever.bind(("",9999))

def recieve():
    while True:
        try:
            message,_ = reciever.recvfrom(1024)
            print(message.decode())
        except Exception:
            print("error recieving")
            
recieve()