import rtmidi
import itertools
import time
import sys, os

# from vjmagic.interface import encodercontroller, encoders, graphics, banks, outpututils
# from vjmagic.routers.pushrouter import PushRouter
# from vjmagic.routers.resolumerouter import ResolumeRouter
from vjmagic.routers.twister import Twister
from vjmagic.state import hardware
from vjmagic.config.midifighter import config
twister = Twister()

hardware.load_map(config['buttons'])

while 1==1:
  try:
    # graphics.loop()
    pass
  except KeyboardInterrupt:
    print("bye")
    sys.exit(0)
