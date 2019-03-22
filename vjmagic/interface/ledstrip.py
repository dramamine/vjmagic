from blinkstick import blinkstick
from collections import deque
import irsensor

def flatten(iterable):
    # flat lists... thx stackoverflow
    return [item for sublist in iterable for item in sublist]

stick = blinkstick.find_first()
led_count = 32

# note that you had to update the library to make this code work!
# File "C:\Python36\lib\site-packages\blinkstick\blinkstick.py", line 226, in _usb_ctrl_transfer
# - data = (c_ubyte * len(data_or_wLength))(*[c_ubyte(ord(c)) for c in data_or_wLength])
# + data = (c_ubyte * len(data_or_wLength))(*[c_ubyte(c) for c in data_or_wLength])

color_stack = deque()
for i in range(0, led_count):
        color_stack.append([100, 0, 0])

def convertValueToColor(value):
    reds = max(0, min( round(value/2), 255))
    greens = 255 - reds
    print(value, greens, reds)
    return [greens, reds, 0]

def cb(val):
    color_stack.appendleft( convertValueToColor(val) )
    led_data = flatten(color_stack)
    stick.set_led_data(0, led_data[0:96])

irsensor.sense_things(cb)
