import socket
import sys
import ascii
import cv2
import time
import os

# User opions
PACKET_SIZE = 20000
ip = "129.151.163.251"
downscale = 0.1
cam_index = 0
packet_rate = 24


sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sender.connect((ip, 80))
except:
    print("server offline please try again later")
    exit()
print(sender.recv(PACKET_SIZE).decode())

# personal setings
if len(sys.argv) == 3:
    if sys.argv[1] == "-s":
        downscale = min(float(sys.argv[2]), 0.5)
    elif sys.argv[1] == "-c":
        cam_index = int(sys.argv[2])
    else:
        print("No")

def output(art):
    height = len(art)
    return('\n'.join((art[row] for row in range(height)))) + "\n"

vid = cv2.VideoCapture(cam_index)

last_packet = time.time()
while True:
    begin = time.time()
    # Send
    
    delay = (1/packet_rate) - (time.time() - last_packet)
    if delay > 0:
        time.sleep(delay)
    ret, frame = vid.read()
    art = ascii.get_art(frame, downscale, 0)
    msg = output(art)
    end = time.time()
    sender.send(msg.encode())
    last_packet = time.time()

    # Recieve
    print(sender.recv(PACKET_SIZE).decode())
    