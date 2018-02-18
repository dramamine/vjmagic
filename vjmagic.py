import rtmidi
import itertools
import time
import sys, os

# from vjmagic.interface import encodercontroller, encoders, graphics, banks, outpututils
# from vjmagic.routers.pushrouter import PushRouter
# from vjmagic.routers.resolumerouter import ResolumeRouter
from vjmagic.routers.fighter64 import Fighter64
from vjmagic.state import hardware
from vjmagic.config.midifighter import config
fighter64 = Fighter64()

hardware.load_map(config['buttons'])

# @TODO probs shouldnt hardcode this; move to bank
# from vjmagic.config.hypnodrome_alpha import config

# always flush stdout
# http://stackoverflow.com/questions/230751/how-to-flush-output-of-python-print
# sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

# encodercontroller.load_config(config)

# aol = PushRouter()
# print("push loaded.")

# res = ResolumeRouter()
# print("resolume loaded.")

# intro display
# def words():
#   outpututils.clear_display()

#   outpututils.set_display_line(0, '                       WELCAME TO HYPNODROME')
#   outpututils.set_display_bytes(2, map(lambda x: int(x), range(68)))
#   outpututils.set_display_bytes(3, map(lambda x: int(x), range(69,127)))

# words()

# for x in config['quadrants']:
#   graphics.load_quadrant(**x)
# graphics.start()
# banks.color_bank_buttons()

# could also try: signal, SIGINT. not working that well with Windows + Python2

while 1==1:
	try:
	  # graphics.loop()
	  pass
	except KeyboardInterrupt:
	  print("bye")
	  sys.exit(0)
