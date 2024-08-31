import socket

HEADERSIZE = 10
address = socket.gethostname()

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.connect((address,6996))

while True:
    
    full_msg = ''
    new_msg = True
    while True:
        msg = client.recv(32)
        if new_msg:
            msglen = int(msg[:HEADERSIZE])
            new_msg = False
            
        full_msg += msg.decode()
        
        if len(full_msg) - HEADERSIZE == msglen:
            print(full_msg[HEADERSIZE:])
            new_msg = True
            full_msg = ''
        