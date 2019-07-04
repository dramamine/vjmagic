import rtmidi
import itertools
import time
import sys, os

# from vjmagic.interface import encodercontroller, encoders, graphics, banks, outpututils
# from vjmagic.routers.pushrouter import PushRouter
# from vjmagic.routers.resolumerouter import ResolumeRouter
from vjmagic.routers import twister
from vjmagic.routers import fighter64black
from vjmagic.routers import fighter64trl
from vjmagic.interface import thereminmanager
from vjmagic.state import hardware
from vjmagic.config.midifighter import config


# always flush stdout
# http://stackoverflow.com/questions/230751/how-to-flush-output-of-python-print

from vjmagic.routers.resolume import Resolume
resolume = Resolume()

twister.init()
twister.use(resolume)

fighter64black.init()
fighter64black.use(resolume)

fighter64trl.init()
fighter64trl.use(resolume)

# new style
thereminmanager.init(resolume)

if __name__ == '__main__':
  try:
    hardware.load_config(config)
  except:
    import sys
    print(sys.exc_info()[0])
  finally:
    print("Press Enter to continue ...")
    input()
