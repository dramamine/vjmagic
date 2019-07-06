from blinkstick import blinkstick
from collections import deque
# import irsensor
import numpy as np

arduino_min = 100
arduino_max = 450
blinkstick_max = 180 # up to 255, but that is very bright.
multiplier = (arduino_max - arduino_min) / blinkstick_max

# turn array of arrays into single array
def flatten(iterable):
    # flat lists... thx stackoverflow
    return [item for sublist in iterable for item in sublist]

# single blinkstick
stick = blinkstick.find_first()

# number of leds to color. these are at the END of the strip (farthest from USB)
led_count = 8
# number of values needed for the whole stick
stick_length = 32


# note that you had to update the library to make this code work!
# File "C:\Python36\lib\site-packages\blinkstick\blinkstick.py", line 226, in _usb_ctrl_transfer
# - data = (c_ubyte * len(data_or_wLength))(*[c_ubyte(ord(c)) for c in data_or_wLength])
# + data = (c_ubyte * len(data_or_wLength))(*[c_ubyte(c) for c in data_or_wLength])

color_stack = deque()
for i in range(0, led_count):
        color_stack.append([100, 0, 0])

def convertValueToColor(value):
    print("raw val:", value)
    reds = max(0, min(round((value-arduino_min)/multiplier), blinkstick_max))
    greens = blinkstick_max - reds
    # print(value, greens, reds)
    return [greens, reds, 0]

def cb(val):
    color = convertValueToColor(val)
    led_data = flatten([[0,0,0]*(stick_length-led_count), np.tile(color, led_count)])
    print(led_data)
    stick.set_led_data(0, led_data)

# use a queue to show changes over time
def cb_chain(val):
    color_stack.appendleft( convertValueToColor(val) )
    led_data = flatten(color_stack)
    stick.set_led_data(0, led_data[0:stick_length])

to_black = [0,0,0] * stick_length
def blackout():
    print('blackin out')
    stick.set_led_data(0, to_black)

if __name__ == "__main__":
    import irsensor
    irsensor.toggle_ears(True)
    irsensor.sense_things(cb)
