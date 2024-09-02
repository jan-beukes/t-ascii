import sys
import cv2
import os
import ascii
import tkinter as tk
import time

# global and stuff
root = tk.Tk()
global cam_index; cam_index = 0
global downscale; downscale = 0.2
global table; table = 0
cam_given = False
running = True
is_video = False
global clear; clear = False
fps_limit = 0

# Arguments
try:
    if len(sys.argv) > 1:
        arg_size = len(sys.argv) - 1
        args = sys.argv[1:]
        for i in range(0,arg_size,2):
            if args[i] == '-s': # Scale
                downscale = float(args[i+1])
            elif args[i] == '-t': # Table
                table = int(args[i+1])
            elif args[i] == '-c': # Camera
                cam_index = int(args[i+1])
                cam_given = True
            elif args[i] == '-v': # Video
                    cam_index = args[i+1]
                    if not os.path.isfile(cam_index):
                        print(f"Video {cam_index} not found")
                        exit()
                    is_video = True
            else:
                raise IndexError           
except FileNotFoundError:
    print(f"image {sys.argv[1]} not found")
    exit()
except (IndexError, TypeError) as e:
    print("Invalid arguments: ", e)
    exit()    
    
def on_button():
    global table; 
    if table < len(ascii.ASCII_TABLES) - 1:
        table += 1
    else:
        table = 0
    

def on_camera():
    global cam_index, vid
    try:
        cam_index = int(camera_entry.get())
        vid.release()
        vid = cv2.VideoCapture(cam_index) 
    except ValueError:
        running = False
        print(f"invalid index {camera_entry.get()}")
        exit()
def on_clear():
    global clear;
    clear = not clear
global vid 

if is_video:
    vid = cv2.VideoCapture(cam_index)
    vid.read()
    if vid.read()[1] is None:
        print("Video stream not found")
        exit()
    fps_limit = vid.get(cv2.CAP_PROP_FPS)
elif not cam_given:
    for i in range(4):
        vid = cv2.VideoCapture(i)
        if not vid.read()[0]:
            print(i, " not work")
            continue
        cam_index = i
        break
    else:
        print("Video stream not found")
        exit()
else:
    vid = cv2.VideoCapture(cam_index) 

# GUI SETTINGS
root.geometry(f"{120}x{220}+0+0")

root.resizable(False,False)
label = tk.Label(root, text="FPS: ")
t_button = tk.Button(root, text="Change", command=on_button)
scale = tk.Scale(root,variable=downscale, orient="horizontal", from_=0.01, to=1.0,resolution=0.01)
camera_lable = tk.Label(root, text="Camera")
camera_entry = tk.Entry(root)
camera_buton = tk.Button(root, text="Set", command=on_camera)
clear_button = tk.Button(root, text="Clear Mode", command=on_clear)
scale.set(downscale)

while running:
    ret, frame = vid.read()
    
    try:
        downscale = scale.get()
    except tk.TclError:
        exit()
        
    begin = time.time()
    art = ascii.get_art(frame, downscale, table)
    ascii.output_art(art, 't', clear)
    end = time.time()
    
    # fps cap for videos
    if is_video and (end-begin) < 1/fps_limit:
        time.sleep(1/fps_limit - (end-begin))
    fps = int(1/(time.time()-begin))
    label.config(text="FPS: " + str(fps))
    label.pack()
    t_button.pack()
    scale.pack()
    camera_lable.pack()
    camera_entry.pack()
    camera_buton.pack()
    clear_button.pack()
    root.update()
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break
vid.release()