import sys
import cv2
import ascii_art

downscale = 0.2

if len(sys.argv) > 1:
    try:
        downscale = float(sys.argv[1])
    except TypeError:
        print("invalid args")
        
vid = cv2.VideoCapture(0)

while True:

    ret, frame = vid.read()
    
    art = ascii_art.get_art(frame, downscale)
    ascii_art.output_art(art, 't')
    
    cv2.imwrite('hello.png',frame)
    #cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    
vid.release()
cv2.destroyAllWindows()