from vjmagic import constants
from vjmagic.interface import encoders

CONFIG = []

def load_config(myconfig):
  global CONFIG # @TODO why do I need this?
  CONFIG = myconfig

def check_for_category_change(event):
  (status, data1, data2) = event
  # we only want to look at the encoders we're tracking, ya know?
  # the 8x8 grid covers 36 to 99
  if data1 < 36 or data1 > 99:
    return

  for x in CONFIG:
    keys = x['keys']
    mode = x['mode']
    labels = x['labels']
    active = x['active']
    try:
      if keys.index(data1) >= 0:
        return encoders.set_display_mode(mode, labels, active)
    except ValueError:
      pass

  # print "reverting to default config"
  return encoders.set_display_mode('BASIC',
    ['STR', 'MAG', 'INT', 'DEX', 'CON']
  )