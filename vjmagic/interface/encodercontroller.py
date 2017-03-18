from vjmagic import constants
from vjmagic.interface import encoders

config = []

def load_config(myconfig):
  config = myconfig
  print "loaded a config of length:", len(myconfig)

def check_for_category_change(event):
  (status, data1, data2) = event

  # we only want to look at the encoders we're tracking, ya know?
  # the 8x8 grid covers 36 to 99
  if data1 < 36 or data1 > 99:
    return

  for x in config:
    # print "my x is:", x

    (mode, label, keys) = x
    try:
      if keys.index(data1) >= 0:
        print "a grid button was pressed and was in this config:", data1, mode
        return encoders.set_display_mode(mode, label)
    except ValueError:
      pass

  return encoders.set_display_mode('BASIC',
    ['STR', 'MAG', 'INT', 'DEX', 'CON']
  )