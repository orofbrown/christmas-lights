import os, sys


CIRCLE_DICT = {
    'red': '\U0001f534',
    'yellow': '\U0001f7e0',
    'orange': '\U0001f7e1',
    'green': '\U0001f7e2',
    'blue': '\U0001f535',
    'purple': '\U0001f7e3',
    'brown': '\U0001f7e4',
    'white': '\U000026aa',
    'black': '\U000026ab'
}
HEX_TO_CIR = {
    '0x230074': 'black',
    '0xff0027': 'red',
    '0xb5001c': 'red',
    '0x220070': 'black',
    '0x542bb5': 'green',
    '0xeeeeee': 'white',  # gray
    '0x000000': 'black',
    '0xff4763': 'red',
    '0xffffff': 'white',
    '0xe02541': 'red',
    '0xd7d7d7': 'white',  # gray
    '0x3200a5': 'green',
    '0x373b39': 'brown',
    '0xffd154': 'yellow',
    '0xff54d1': 'yellow',
    '0xe300ad': 'orange'
}

def test_circle_color(c, idx):
    if idx % 10 == 0:
        print()

    h = hex(c) if c != 0 else '0x000000'
    literal = HEX_TO_CIR[h]
    cir = CIRCLE_DICT[literal]
    sys.stdout.write(cir)
