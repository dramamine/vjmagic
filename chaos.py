import rtmidi
import itertools
import time, math
import sys, os
import random
import threading

from vjmagic.routers.resolumerouter import ResolumeRouter
from vjmagic import constants
from vjmagic.interface import outpututils

# always flush stdout
# http://stackoverflow.com/questions/230751/how-to-flush-output-of-python-print
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

def setInterval(func, time):
  e = threading.Event()
  while not e.wait(time):
    func()

all_keys = range(36,99)
layers = [
  [
    36, 37, 38, 39,
    44, 45, 46, 47,
    52, 53, 54, 55,
    60, 61, 62, 63
  ],
  [
    40, 41, 42, 43,
    48, 49, 50, 51,
    56, 57, 58, 59,
    64, 65, 66, 67
  ],
  [
    68, 69, 70, 71,
    76, 77, 78, 79,
    84, 85, 86, 87,
    92, 93, 94, 95,
  ],
  [
    72, 73, 74, 75,
    80, 81, 82, 83,
    88, 89, 90, 91,
    96, 97, 98, 99
  ]
]

last_layer = -1

for i in range(0,4):
    outpututils.thru([constants.STATUS_CH1, constants.BUTTON_QUANTIZE+i, 127])
    outpututils.thru([constants.STATUS_CH1, constants.BUTTON_QUANTIZE+i, 0])

print(all_keys)
def loop():
  global last_layer

  choice = random.choice(all_keys)
  outpututils.thru([constants.MIDI_NOTE_ON, choice, 127])

  layer = -1
  for i in range(0,4):
    if choice in layers[i]:
      layer = i
      break

  print('found layer', layer, 'for button:', choice)
  if last_layer >= 0 and layer != last_layer:
    print('kill last layer')
    outpututils.thru([constants.STATUS_CH1, constants.BUTTON_QUANTIZE + last_layer, 127])
    outpututils.thru([constants.STATUS_CH1, constants.BUTTON_QUANTIZE + last_layer, 0])
  last_layer = layer

# could also try: signal, SIGINT. not working that well with Windows + Python2
try:
  loop()
  setInterval(loop, 30)
except KeyboardInterrupt:
  outpututils.clear_display()
  print "bye"
  sys.exit(0)
