import rtmidi
import itertools
import time
import sys, os

# from vjmagic.interface import encodercontroller, encoders, graphics, banks, outpututils
# from vjmagic.routers.pushrouter import PushRouter
# from vjmagic.routers.resolumerouter import ResolumeRouter
from vjmagic.routers import twister
from vjmagic.routers.fighter64 import Fighter64
from vjmagic.state import hardware
from vjmagic.config.midifighter import config

from vjmagic.routers.resolume import Resolume
twister.init()
resolume = Resolume()
fighter64 = Fighter64()
twister.use(resolume)
fighter64.use(resolume)



if __name__ == '__main__':
  try:
    hardware.load_config({
      'buttons': {
        1: [3, [0, 1, 2, 3, 4, 5, 6, 7]]
      },
      'layers': {
        3: [12, 13, 14, 15, 8, 9, 10, 11]
      }
    })
    hardware.handle_button_press(1)
  except:
    import sys
    print(sys.exc_info()[0])
  finally:
    print("Press Enter to continue ...")
    input()