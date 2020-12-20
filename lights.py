import random
from sys import stdout
from time import sleep
import board
from neopixel import NeoPixel


LED_COUNT = 100
LED_PIN = board.D18
MATRIX_WIDTH = 10
MATRIX_HEIGHT = LED_COUNT // MATRIX_WIDTH
'''
NeoPixel color ordering is GRB
So these values are in that order
'''
RAINBOW = [
    '0x00ff00',
    '0x55ff00',
    '0xffff00',
    '0xff0000',
    '0xff00ff',
    '0x0000ff',
    '0x00ffff'
]

class LedStrand:
    def __init__(self):
        self.strand_matrix = []
        for i in range(MATRIX_HEIGHT):
            mult = i * 10
            odd_row = i % 2 == 1
            row = []
            for j in range(mult, MATRIX_WIDTH*(i+1)):
                num = LED_COUNT - 1 - j
                if odd_row:
                    row.insert(0, num)
                else:
                    row.append(num)
            self.strand_matrix = self.strand_matrix + row
        self.pixels = NeoPixel(LED_PIN, LED_COUNT, brightness=1.0)

    def color_pixels(self, idx, r, g, b):
        if idx < 0:
            self.pixels.fill([g, r, b])
        else:
            self.pixels[idx] = [g, r, b]

    def color_pixels_bulk(self, data):
        self.pixels[:] =  [data[i] for i in self.strand_matrix][:]
    
    def color_pixels_hex(self, rgb_hex):
        if rgb_hex == '0x123456':
            self.do_rainbow()
            return
        elif rgb_hex == '0x789123':
            self.do_rainbow_striped()
            return

        red = rgb_hex[2:4]
        green = rgb_hex[4:6]
        blue = rgb_hex[6:]

        color = '0x%s%s%s' % (green, red, blue)
        self.pixels.fill(int(color, 16))

    def do_rainbow(self):
        color_copy = list(RAINBOW)
        l = len(color_copy)
        try:
            while True:
                for i in range(LED_COUNT):
                    idx = i % l
                    self.pixels[i] = int(color_copy[idx], 16)
                random.shuffle(color_copy)
                sleep(1)
        except KeyboardInterrupt as ki:
            print()
            return

    def do_rainbow_striped(self):
        color_copy = list(RAINBOW)
        l = len(color_copy)
        try:
            while True:
                for i in range(MATRIX_HEIGHT):
                    start = i * MATRIX_WIDTH
                    end = start + MATRIX_WIDTH
                    idx = i % l
                    for j in range(start, end):
                        self.pixels[j] = int(color_copy[idx], 16)
                color_copy = color_copy[-1:] + color_copy[:-1]
                sleep(0.5)
        except KeyboardInterrupt as ki:
            print()
            return

    def get_hex_number(self, n):
        return hex(n) if n > 9 else '0x0%d' % n
    
    def turn_off(self):
        self.pixels.fill(0)

    def deinit(self):
        self.pixels.deinit()


def main():
    pass


if __name__ == '__main__':
    main()
