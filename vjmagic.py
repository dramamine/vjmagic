import rtmidi
import itertools
import time
import sys, os

from vjmagic.interface import encodercontroller, encoders, graphics, outpututils
from vjmagic.routers.pushrouter import PushRouter
from vjmagic.routers.resolumerouter import ResolumeRouter
from vjmagic.config.hypnodrome import config

# always flush stdout
# http://stackoverflow.com/questions/230751/how-to-flush-output-of-python-print
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

draft = [{
  'mode': 'TOUCH',
  'active': 8,
  'labels': None,
  'keys': [
    72, 73, 74, 75,
    80, 81, 82, 83,
    88, 89, 90, 91,
    96, 97, 98, 99
  ]
}, {
  'mode': 'CLIPS',
  'active': 6,
  'labels': ['intro', 'verse', 'chorus', 'bridge', 'break', 'outro'],
  'keys': [
    36, 37, 38, 39,
    44, 45, 46, 47,
    52, 53, 54, 55,
    60, 61, 62, 63
  ]
}, {
  'mode': 'BASIC',
  'active': 6,
  'labels': ['STR', 'MAG', 'INT', 'DEX', 'CON', 'LCK'],
  'keys': [
    68, 69, 70, 71,
    76, 77, 78, 79,
    84, 85, 86, 87,
    92, 93, 94, 95
  ]
}, {
  'mode': 'CLIPS',
  'active': 6,
  'labels': ['intro', 'verse', 'chorus', 'bridge', 'break', 'outro'],
  'keys': [
    40, 41, 42, 43,
    48, 49, 50, 51,
    56, 57, 58, 59,
    64, 65, 66, 67
  ]
}]

encodercontroller.load_config(config)

aol = PushRouter()
print("push loaded.")

res = ResolumeRouter()
print("resolume loaded.")

# intro display
def words():
  outpututils.clear_display()

  outpututils.set_display_line(0, '                       WELCAME TO HYPNODROME')
  outpututils.set_display_bytes(2, map(lambda x: int(x), range(68)))
  outpututils.set_display_bytes(3, map(lambda x: int(x), range(69,127)))

words()

# could also try: signal, SIGINT. not working that well with Windows + Python2
try:
  graphics.loop()
except KeyboardInterrupt:
  outpututils.clear_display()
  print "bye"
  sys.exit(0)
