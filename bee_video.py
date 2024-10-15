import sys
import cv2
from video import gui2, ascii
import time

fps_limit = 30.1

try:
    vid = cv2.VideoCapture("video/rick2.webm")
except cv2.error:
    vid = cv2.VideoCapture(0)

def play(scale):
    gui2.init_gui(scale)
    running = True
    while running:
        begin = time.time()
        ret, frame = vid.read()
        art = ascii.get_art(frame, scale)
        gui2.render_frame(art, begin)

        # FPS for video
        end = time.time()
        frame_time = end-begin
        if frame_time < 1/fps_limit:
            time.sleep(1/fps_limit - frame_time)
        
        
    vid.release()

if __name__ == "__main__":
    # Arguments
    scale = 80
    if len(sys.argv) > 1:
        if sys.argv[1] == '-s': # Scale
            scale = int(sys.argv[2])
            
    play(scale)
