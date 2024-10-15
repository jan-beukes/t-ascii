import cv2
import sys
import numpy as np
import os

## CONSTANTS
ASCII_TABLES = "dfs "
GRAYSCALE_WEIGHTS =  np.array((0.299,0.587,0.114))
SQUISH_FACTOR = 1 # decrease height to better match original
global windows; windows = False

# Create ascii array 
def get_art(image, scale):
    try:
        image = cv2.resize(image, (int(scale), int(scale)))
    except cv2.error:
        print("ඞ")
        exit()
    width,height = image.shape[1], image.shape[0]
    art = [""]*height
    
    #loop through art array and select ascii from relative pixel
    grey = np.dot(image,GRAYSCALE_WEIGHTS)
    for y in range(height):
        for x in range(width):
            char = ASCII_TABLES[int(grey[y][x] * (len(ASCII_TABLES)-1)/255)] # grey value * factor to get correct ascii character from brightness
            art[y] += char
    return art       

def output_art(art, out_mode, clear=False):
    height = len(art)
    if out_mode == 'f': 
        with open("out.txt","w") as file: 
            file.write('\n'.join((''.join(art[row]) for row in range(height))))
            return
    if clear:
        if windows:
            os.system("cls")
        else:
            os.system("clear")
    if out_mode == 't': 
        print('\n'.join((art[row] for row in range(height))), end='')
        print("")       
        
def get_frame(art):
    height = len(art)
    return '\n'.join(art[row] for row in range(height))
        
        
def main():
    if os.name == 'nt':
        global windows; windows == True
    downscale = 0.1
    table = 0
    # Get input
    try:
        image = cv2.imread(sys.argv[1])
        if len(sys.argv) > 2:
            arg_size = len(sys.argv) - 2
            args = sys.argv[2:]
            for i in range(0,arg_size,2):
                if args[i] == '-s':
                    downscale = float(args[i+1])
                elif args[i] == '-t':
                    table = int(args[i+1])
                else:
                    raise IndexError
                    
        out_mode = input('Output [t] for terminal [f] for file: ')
        if out_mode.lower() not in ['t','f']:
            exit()
    except FileNotFoundError:
        print(f"image {sys.argv[1]} not found")
        exit()
    except (IndexError, TypeError) as e:
        print("Invalid arguments: ", e)
        exit()
        
    art = get_art(image, downscale, table)
    
if __name__ == "__main__": main()
    