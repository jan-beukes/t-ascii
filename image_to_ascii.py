import picture
import sys
from color import Color

## CONSTANTS
darkness_table = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
downscale = 0.1
GRAYSCALE_FACTOR =  (0.299,0.587,0.114)
ASCII_FACTOR = (len(darkness_table)-1)/255
SQUISH_FACTOR = 0.6

## Get input
try:
    image = picture.Picture(sys.argv[1])
    if len(sys.argv) > 2:
        if sys.argv[2] == '-s':
            downscale = float(sys.argv[3])
        else:
            raise IndexError
            
    out_mode = input('Output [t] for terminal [f] for file: ')
    if out_mode.lower() not in ['t','f']:
        exit()
except FileNotFoundError:
    print(f"image {sys.argv[1]} not found")
    exit()
except IndexError:
    print("Invalid args")
    exit()
   
# Create ascii array   
art_height, art_width = int(downscale*image.height()), int(downscale*image.width())
art = [""]*art_height
image2 = picture.Picture(art_width,art_height)

#loop through art array and select ascii from relative pixel
for y in range(art_height):
    for x in range(art_width):
        c = image.get(int((1/downscale)*x),int((1/downscale)*y))
        grey = c.getRed()*GRAYSCALE_FACTOR[0] + c.getGreen()*GRAYSCALE_FACTOR[1] + c.getBlue()*GRAYSCALE_FACTOR[2]
        grey = int(grey/3)
        c = Color(grey,grey,grey)
        image2.set(x,y,c)
        char = darkness_table[int((255-grey) * ASCII_FACTOR)]
        art[y] += char
    art[y] += "\n"
image2.save("out.png")        

with open("out.txt","w") as file:
    
    squish = int(art_height * SQUISH_FACTOR)
    for row in range(squish):
        if out_mode.lower() == 'f': file.write(art[int(row/SQUISH_FACTOR)])
        if out_mode.lower() == 't': print(art[int(row/SQUISH_FACTOR)],end="")