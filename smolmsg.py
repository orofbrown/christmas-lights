from sys import argv
from time import sleep
from board import D18
from neopixel import NeoPixel


def change(px, np, cl):
    for i in px:
        np[i] = cl
    

def main():
    color_list = [255, 0, 0]

    with open('%s.txt' % argv[1]) as f:
        pixels = f.read()
    
    np = NeoPixel(D18, 50)
    array = [int(i) for i in pixels.strip().split(' ')]
    change(array, np, color_list)

    while True:
        try:
            sleep(2)
            color_list = color_list[-1:] + color_list[:-1]
            change(array, np, color_list)
        except KeyboardInterrupt as ki:
            np.deinit()
            break

if __name__ == '__main__':
    main()

