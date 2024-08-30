import cv2
import sys
import os

## CONSTANTS
darkness_table = " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
#darkness_table = " .',:;xlxokXdO0KN"
GRAYSCALE_FACTOR =  (0.299,0.587,0.114)
ASCII_FACTOR = (len(darkness_table)-1)/255 # factor to get ascii character from brightness
SQUISH_FACTOR = 0.5 # decrease height to better match original

# Create ascii array 
def get_art(image, downscale):
    width,height = image.shape[0],image.shape[1]
    art_width, art_height = int(downscale*height), int(downscale*width)
    art = [""]*art_height
    
    #loop through art array and select ascii from relative pixel
    for y in range(art_height):
        for x in range(art_width):
            c = image[int((1/downscale)*y)][int((1/downscale)*x)]
            grey = c[0]*GRAYSCALE_FACTOR[0] + c[1]*GRAYSCALE_FACTOR[1] + c[2]*GRAYSCALE_FACTOR[2]
            char = darkness_table[int(grey * ASCII_FACTOR)]
            art[y] += char
    return art       

def output_art(art, out_mode):
    art_height = len(art)
    with open("out.txt","w") as file: 
        squish = int(art_height * SQUISH_FACTOR)
        os.system("clear")
        if out_mode == 't': print('\n'.join((''.join(art[int(row/SQUISH_FACTOR)]) for row in range(squish))), end='')
        if out_mode == 'f': file.write('\n'.join((''.join(art[int(row/SQUISH_FACTOR)]) for row in range(squish))))
def main():
    downscale = 0.1
    # Get input
    try:
        image = cv2.imread((sys.argv[1]))
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
        
    art = get_art(image, downscale)
    output_art(art, out_mode)
    
if __name__ == "__main__": main()
    