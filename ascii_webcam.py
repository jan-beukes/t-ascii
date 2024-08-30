import sys
import cv2
import ascii_art
import tkinter as tk
import time

root = tk.Tk()
root.minsize(120, 60)
root.maxsize(120, 60)
downscale = 0.2

if len(sys.argv) > 1:
    try:
        downscale = float(sys.argv[1])
    except TypeError:
        print("invalid args")
        
vid = cv2.VideoCapture(0)
#FPS
label = tk.Label(root, text="FPS: ")

while True:
    ret, frame = vid.read()
    begin = time.time()
    art = ascii_art.get_art(frame, downscale)
    ascii_art.output_art(art, 't')
    end = time.time()
    
    fps = int(1/(end-begin))
    
    label.config(text="FPS: " + str(fps))
    label.pack()
    root.update()
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    
vid.release()
cv2.destroyAllWindows()