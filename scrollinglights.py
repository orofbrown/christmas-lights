# http://www.aoakley.com/articles/2015-11-18-raspberry-pi-christmas-led-matrix.php
#!/usr/bin/python3

import time
import board
from sys import argv
from testlights import test_circle_color
from lights import LedStrand
from imagehandler import ImageHandler


WHITE = 0xFFFFFF
RED = 0xFF0000
GREEN = 0x00FF00
BLUE = 0x0000FF

LED_COUNT = 100
LED_PIN = board.D18
MATRIX_WIDTH = 10
MATRIX_HEIGHT = LED_COUNT // MATRIX_WIDTH
SPEED = 0.1


def get_hex_number(n):
    return hex(n) if n > 9 else '0x0%d' % n


def main():
    # Open the image file given as the command line parameter
    image_handler = ImageHandler(argv[1], matrix_height=MATRIX_HEIGHT, matrix_width=MATRIX_WIDTH)
    # If the image height doesn't match the matrix, resize it
    img_copy = image_handler.resize() if image_handler.height() != MATRIX_HEIGHT else image_handler.copy()
    # If the input is a very small portrait image, then no amount of resizing will save us
    if image_handler.width() < MATRIX_WIDTH:
        raise Exception(
            "Picture is too narrow. Must be at least %d pixels wide" % MATRIX_WIDTH
        )
    
    image_handler.reformat_for_loop(img_copy)

    strand = LedStrand()

    try:
        while True:
            # Loop through the image widthways
            for i in range(0, image_handler.width() - MATRIX_WIDTH):
                image_handler.show(i, strand)
                time.sleep(SPEED)

    except (KeyboardInterrupt, SystemExit, KeyError):
        strand.pixels.deinit()
        print("\nStopped")

if __name__ == '__main__':
    main()
