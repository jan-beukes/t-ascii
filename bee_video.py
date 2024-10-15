import sys
import cv2
import gui
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
fps_limit = 30

# Arguments
scale = 80
if len(sys.argv) > 1:
    if sys.argv[1] == '-s': # Scale
        scale = int(sys.argv[2])


global vid 
vid = cv2.VideoCapture("badapple.webm")

gui.init_gui(scale)
while running:
    begin = time.time()
    ret, frame = vid.read()
    art = ascii.get_art(frame, scale)
    gui.render_frame(art)
    end = time.time()
    frame_time = end-begin
    if frame_time < 1/fps_limit:
        time.sleep(1/fps_limit - frame_time)

vid.release()