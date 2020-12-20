import sys
from lights import LedStrand
from imagehandler import ImageHandler
import readline

color_dict = {
    'red': '0xff0000',
    'orange': '0xff5500',
    'yellow': '0xffff00',
    'green': '0x00ff00',
    'cyan': '0x00ffff',
    'blue': '0x0000ff',
    'purple': '0x880088',
    'black': '0x000000',
    'white': '0xffffff',
    'rainbow': '0x123456',
    'rainbow2': '0x789123',
    'peach': '0xff6666',
    'gray': '0x444444'
}

STRAND = LedStrand()

def show(img_name):
    try:
        img_path = '%s.png' % img_name
        ih = ImageHandler(img_path)
        ih.show(0, STRAND)

        print('Done!')
    except (KeyError, FileNotFoundError): 
        if not img_name or img_name == 0:
            print('You forgot to tell me which picture to show!')
        else:
            print('I can\'t find that picture. Try another one!')
    except Exception as ex:
        raise ex


def color(c):
    try:
        new_color = color_dict[c]
        print('Making all lights turn %s...' % c)
        STRAND.color_pixels_hex(new_color)
        print('Done!')
    except KeyError as ke:
        if not c or c == 0:
            print('You forgot to tell me what color!')
        else:
            print('What color is %s? Try another one!' % c)


def end(code):
    STRAND.turn_off()
    print('Bye!')
    sys.exit(code)


cmd_dict = {
    'show': show,
    'color': color,
    'exit': end
}

def main():
    print('commands:')
    print('  color [color name]')
    print('  show [picture name]')
    while True:
        try:
            x = input('> ')
            parts = x.split(' ')

            cmd = cmd_dict[parts[0]]
            arg = parts[1] if len(parts) > 1 else 0
            cmd(arg)
        except KeyboardInterrupt as ki:
            print('\nStopping!')
            end(0)
        except KeyError as ke:
            print('Whoops, I don\'t  know that command!')
        except IndexError as ie:
            err_dict = {
                'show': 'You forgot to tell me what picture to show. Try again!',
                'color': 'You forgot to tell me what color to change to. Try again!'
            }
            print(err_dict[cmd])
        except Exception as ex:
            raise ex

if __name__ == '__main__':
    main()

