import socket
import select

HEADERSIZE = 10
PORT = 6996
IP = "127.0.0.1"

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((IP, PORT))
server.listen()

sockets_list = [server]
clients = {}
connected = False

def recieve_message(client_socket: socket.socket):
    try:
        message_header = client_socket.recv(HEADERSIZE)
        if not len(message_header):
            return False
        
        message_length = int(message_header.decode().strip())
        return {"header:": message_header, "data": client_socket.recv(message_length)}
    except:
        return False

while not connected:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
    
    for notified_socket in read_sockets:
        if notified_socket == server:
            client_socket, client_address = server.accept()
            
            user = recieve_message(client_socket)
            if user is False:
                continue
            
            sockets_list.append(client_socket)
            clients[client_socket] = user
            
            print(f"Accepted connection from {client_address[0]}:{client_address[1]} name:{user['data']}")
        else:
            message = recieve_message(notified_socket)
            
            if message is False:
                name = clients[notified_socket]['data'].decode()
                print(f"Closed connection from {name} ")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue
                
            user = clients[notified_socket]
            name = clients[notified_socket]['data'].decode()
            print(f"Recieved message from {name}")
                
    clientsocket, address = server.accept()
    print(f"connection from {address} established")
    clientsocket.send(msg.encode())