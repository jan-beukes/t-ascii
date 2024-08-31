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
running = True
is_video = False
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
    global table; table = 1 - table

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
    
global vid 
vid = cv2.VideoCapture(cam_index)
vid.read()
if vid.read()[1] is None:
    print("Video stream not found")
    exit()
if is_video:
    fps_limit = vid.get(cv2.CAP_PROP_FPS)

# GUI SETTINGS
root.geometry(f"{120}x{180}+0+0")

root.resizable(False,False)
label = tk.Label(root, text="FPS: ")
t_button = tk.Button(root, text="Change", command=on_button)
scale = tk.Scale(root,variable=downscale, orient="horizontal", from_=0.01, to=1.0,resolution=0.01)
camera_lable = tk.Label(root, text="Camera")
camera_entry = tk.Entry(root)
camera_buton = tk.Button(root, text="Set", command=on_camera)
scale.set(downscale)

while running:
    ret, frame = vid.read()
    
    try:
        downscale = scale.get()
    except tk.TclError:
        exit()
        
    begin = time.time()
    art = ascii.get_art(frame, downscale, table)
    ascii.output_art(art, 't')
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
    root.update()
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break
vid.release()