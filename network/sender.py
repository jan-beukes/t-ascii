import socket

ip = "146.232.65.152"

sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sender.bind(("", 9998))

message = input("Message: ")
sender.sendto(message.encode(), (ip,9999))

print("sent")