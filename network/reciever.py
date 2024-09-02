import socket
import threading

reciever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
reciever.bind(("129.151.163.251",80))
reciever.listen()

print("waiting for connectiion...")
while True:
    client, address = reciever.accept()
    print(address, ": " + client.recv(1024).decode())
        
