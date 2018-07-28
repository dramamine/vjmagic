import rtmidi
import itertools
import time
import sys, os

# from vjmagic.interface import encodercontroller, encoders, graphics, banks, outpututils
# from vjmagic.routers.pushrouter import PushRouter
# from vjmagic.routers.resolumerouter import ResolumeRouter
from vjmagic.routers import apc40
from vjmagic.state import hardware
# from vjmagic.config.midifighter import config
from vjmagic.config.apc40 import config


# always flush stdout
# http://stackoverflow.com/questions/230751/how-to-flush-output-of-python-print

from vjmagic.routers.resolume import Resolume
apc40.init()
resolume = Resolume()
apc40.use(resolume)

if __name__ == '__main__':
  try:
    hardware.load_config(config)
  except:
    import sys
    print(sys.exc_info()[0])
  finally:
    print("Press Enter to continue ...")
    input()
    