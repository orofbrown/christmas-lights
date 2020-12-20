# Ohm's law: V = mA * R
# or: R = V / mA

from time import sleep
from gpiozero import LED

gpio14 = LED(14)
gpio18 = LED(18)

#gpio14.on()
#sleep(2)
#gpio14.off()

gpio18.on()
sleep(2)
gpio18.off()

