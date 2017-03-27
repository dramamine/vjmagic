import rtmidi
import itertools
import time
import sys, os

from vjmagic.interface import encodercontroller, graphics, outpututils
from vjmagic.routers.pushrouter import PushRouter
from vjmagic.routers.resolumerouter import ResolumeRouter

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
  'mode': 'BASIC',
  'active': 5,
  'labels': ['STR', 'MAG', 'INT', 'DEX', 'CON'],
  'keys': [
    36, 37, 38, 39,
    44, 45, 46, 47,
    52, 53, 54, 55,
    60, 61, 62, 63
  ]
}]

encodercontroller.load_config(draft)

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
