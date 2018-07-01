import rtmidi
import itertools
import time
import sys, os

# from vjmagic.interface import encodercontroller, encoders, graphics, banks, outpututils
# from vjmagic.routers.pushrouter import PushRouter
# from vjmagic.routers.resolumerouter import ResolumeRouter
from vjmagic.routers import twister
from vjmagic.routers import fighter64
from vjmagic.routers import launchpadmini
from vjmagic.state import hardware
from vjmagic.config.midifighter import config


# always flush stdout
# http://stackoverflow.com/questions/230751/how-to-flush-output-of-python-print

from vjmagic.routers.resolume import Resolume
twister.init()
resolume = Resolume()
fighter64.init()
launchpadmini.init()
twister.use(resolume)
fighter64.use(resolume)
launchpadmini.use(resolume)

if __name__ == '__main__':
  try:
    hardware.load_config(config)
  except:
    import sys
    print(sys.exc_info()[0])
  finally:
    print("Press Enter to continue ...")
    input()