import cv2
import sys
import os

## CONSTANTS
ASCII_TABLES = (" .',:;xlxokXdO0KN"," .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$")
GRAYSCALE_FACTOR =  (0.299,0.587,0.114)
SQUISH_FACTOR = 0.5 # decrease height to better match original

# Create ascii array 
def get_art(image, downscale, t):
    width,height = image.shape[0],image.shape[1]
    art_width, art_height = int(downscale*height), int(downscale*width)
    art = [""]*art_height
    
    #loop through art array and select ascii from relative pixel
    for y in range(art_height):
        for x in range(art_width):
            c = image[int((1/downscale)*y)][int((1/downscale)*x)]
            grey = c[0]*GRAYSCALE_FACTOR[0] + c[1]*GRAYSCALE_FACTOR[1] + c[2]*GRAYSCALE_FACTOR[2]
            char = ASCII_TABLES[t][int(grey * (len(ASCII_TABLES[t])-1)/255)] # grey value * factor to get correct ascii character from brightness
            art[y] += char
    return art       

def output_art(art, out_mode):
    art_height = len(art)
    with open("out.txt","w") as file: 
        squish = int(art_height * SQUISH_FACTOR)
        #os.system("clear")
        if out_mode == 't': print('\n'.join((''.join(art[int(row/SQUISH_FACTOR)]) for row in range(squish))), end='')
        if out_mode == 'f': file.write('\n'.join((''.join(art[int(row/SQUISH_FACTOR)]) for row in range(squish))))
def main():
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
    output_art(art, out_mode)
    
if __name__ == "__main__": main()
    