from sys import argv
from time import sleep
from PIL import Image
from lights import LedStrand


class ImageHandler:
    def __init__(self, filename, matrix_height=10, matrix_width=10):
        self.img = Image.open(filename).convert("RGB")
        self.matrix_height = matrix_height
        self.matrix_width = matrix_width
    
    def height(self):
        return self.img.size[1]

    def width(self):
        return self.img.size[0]

    def resize(self):
        return self.img.resize(
            (self.matrix_width, self.matrix_height),
            Image.BICUBIC,
        )

    def show(self, idx, strand):
        img_rect = self.crop(idx)
        pixel_color_tuples = [[g,r,b] for [r,g,b] in list(img_rect.getdata())]
        # pixel_color_tuples.reverse()

        # update_matr = []
        # for i in range(self.matrix_height):
        #     mult = i * 10
        #     odd_row = i % 2 != 0
        #     row = []
        #     for j in range(mult, self.matrix_width*(i+1)):
        #         num = (self.matrix_height * self.matrix_width) - 1 - j
        #         if not odd_row:
        #             row.insert(0, num)
        #         else:
        #             row.append(num)
        #     update_matr = update_matr + row

        # for j in range(len(pixel_color_tuples)):
        strand.color_pixels_bulk(pixel_color_tuples)

    def copy(self):
        return self.img.copy()

    def reformat_for_loop(self, copy):
        '''
        Add a copy of the start of the image, to the end of the image,
        so that it loops smoothly at the end of the image
        '''
        img = Image.new("RGB", (copy.size[0], copy.size[1]))
        img.putdata(copy.getdata())
        # img.paste(copy, (0, 0, copy.size[0], copy.size[1]))
        # img.paste(
        #     copy.crop((0, 0, self.matrix_width, self.matrix_height)),
        #     (copy.size[0], 0, copy.size[0] + self.matrix_width, self.matrix_height),
        # )
        self.img = img
    
    def crop(self, left_side):
        side_coords = left_side, 0, left_side + self.matrix_width, self.matrix_height
        return self.img.crop(side_coords)


if __name__ == '__main__':
    strand = LedStrand()
    ih = ImageHandler(argv[1])

    # img_copy = ih.resize() if ih.height() != ih.matrix_height else ih.copy()
    # img_copy = ih.copy()
    # ih.reformat_for_loop(img_copy)
    ih.show(0, strand)

    # print(list(ih.img.getdata()))

    sleep(5)
    strand.deinit()

