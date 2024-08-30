import sys
import cv2
import ascii_art
import tkinter as tk
import time

root = tk.Tk()
root.minsize(120, 60)
root.maxsize(120, 60)

downscale = 0.2
table = 0

try:
    
    if len(sys.argv) > 1:
        arg_size = len(sys.argv) - 1
        args = sys.argv[1:]
        for i in range(0,arg_size,2):
            if args[i] == '-s':
                downscale = float(args[i+1])
            elif args[i] == '-t':
                table = int(args[i+1])
            else:
                raise IndexError
            
except FileNotFoundError:
    print(f"image {sys.argv[1]} not found")
    exit()
except (IndexError, TypeError) as e:
    print("Invalid arguments: ", e)
    exit()
        
vid = cv2.VideoCapture(0)
#FPS
label = tk.Label(root, text="FPS: ")

while True:
    ret, frame = vid.read()
    begin = time.time()
    art = ascii_art.get_art(frame, downscale, table)
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