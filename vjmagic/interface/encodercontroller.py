from vjmagic import constants
from vjmagic.interface import encoders

CONFIG = []

def load_config(myconfig):
  global CONFIG
  CONFIG = myconfig
  # print "loaded a config of length:", len(myconfig), len(CONFIG)

def check_for_category_change(event):
  (status, data1, data2) = event
  # print "check_for_category_change:", event
  # we only want to look at the encoders we're tracking, ya know?
  # the 8x8 grid covers 36 to 99
  if data1 < 36 or data1 > 99:
    return
  # print "checking config...", CONFIG
  for x in CONFIG:
    # print "my x is:", x, "for data1:", data1

    (mode, label, keys) = x
    try:
      if keys.index(data1) >= 0:
        # print "a grid button was pressed and was in this config:", data1, mode
        return encoders.set_display_mode(mode, label)
    except ValueError:
      pass

  # print "reverting to default config"
  return encoders.set_display_mode('BASIC',
    ['STR', 'MAG', 'INT', 'DEX', 'CON']
  )