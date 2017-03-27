from vjmagic import constants
from vjmagic.interface import outpututils
import math, itertools

class Stuff:
  pass


ENCODERS = [71, 72, 73, 74, 75, 76, 77, 78, 79]

INCREMENT = 1
DECREMENT = 127
SENSITIVITY = 1

state = Stuff()
state.touched = [False] * 9
state.values = [0] * 9
state.active_knobs = 8
state.update_display = None
state.labels = []
state.display_mode = ''

# update the value of an encoder
#
# encoder {Int} The encoder ID (0-8)
# value {Int} The value (0-127)
def update_value(encoder, value):
  state.values[encoder] = value


def set_display_mode(mode, tolabels, active):
  print("set_display_mode called", mode, tolabels, active)
  state.active_knobs = active
  if mode == state.display_mode:
    return
  else:
    print(mode, "was not", state.display_mode)

  if mode == 'BASIC':
    print("switching to basic display")
    outpututils.clear_display_line(2)
    outpututils.clear_display_line(3)
    state.update_display = update_display_basic
    state.labels = tolabels
    print("switched. labels are now:", state.labels)
  elif mode == 'TOUCH':
    print("switching to touch display")
    # reset values bc it gets weird otherwise
    state.touched = [False] * 9
    state.update_display = update_display_touchy
  else:
    print("WTF wrong mode y'all")
    return "WTF"

  state.display_mode = mode
  # clear before we do anything...
  outpututils.clear_display()
  state.update_display()

# handle an event coming from the push
def handle_push_turns(event):
  (status, data1, data2) = event
  print("ok push turns is handled.", event)
  try:
    encoder = ENCODERS.index(data1)
  except ValueError:
    return None

  # splitting between increments and decrements
  if data2 < 64:
    new_cc = min(127, state.values[encoder] + (SENSITIVITY * data2) )
  else:
    new_cc = max(0, state.values[encoder] - (SENSITIVITY * (128 - data2) ) )

  print("updating encoder to ", new_cc, "on event:", event)
  # relay the new value from ch1 to ch2
  outpututils.thru([constants.STATUS_CH2, data1, new_cc])

  # we were updating the display here...
  # but now lets try waiting for updates from resolume instead.
  state.values[encoder] = new_cc
  state.update_display()

# ex. (144, 0, 127) means the first knob was touched
# ex. (144, 0, 0) means the first knob was untouched
def handle_push_touches(event):

  (status, data1, data2) = event
  if (data1 > 8):
    return
  state.touched[data1] = bool(data2)
  print("touched:", event)
  state.update_display()

# handle an event coming from resolume
def handle_resolume_updates(event):
  (status, data1, data2) = event
  try:
    encoder = ENCODERS.index(data1)
  except ValueError:
    print("couldnt find", data1)
    return None

  print "resolume sez: set encoder ", encoder, " with index", data1, " from ", state.values[encoder], " to ", data2
  state.values[encoder] = data2
  state.update_display()


## update the display using 'basic' mode
def update_display_basic():

  # val_bytes =
  encoders = map(encoder_text_to_bytes, state.values[:state.active_knobs])
  chained = list(itertools.chain.from_iterable(encoders))
  # sorry. adding blank spaces since width is 68, not 64

  for width in [56, 40, 24, 8]:
    if len(chained) > width:
      print("adding blank here:", width)
      chained[width:width] = [constants.TEXT_BLANK]

  print("chained:", chained)

  outpututils.set_display_bytes(0, chained)
  # annoying spacing
  # outstr = ''
  # ctr = 0
  # for val_string in val_strings:
  #   outstr = outstr + val_string
  #   if ctr % 2 == 0:
  #     outstr = outstr + " "
  #   ctr = ctr + 1

  # outpututils.set_display_line(0, outstr)

  # labels
  outpututils.set_display_cells(1,
    state.labels + [''] * (8 - len(state.labels)) # pad to 8 with empty strings
  )

# # load this func on start
# state.update_display = update_display_basic

# update the display using 'touch' mode
def update_display_touchy():
  val_cells = map(lambda x: 'x'*8 if x else ' '*8, state.touched[:state.active_knobs])
  outpututils.set_display_cells(0, val_cells)
  outpututils.set_display_cells(1, val_cells)
  outpututils.set_display_cells(2, val_cells)
  outpututils.set_display_cells(3, val_cells)

def encoder_text_to_bytes(x):
  print("encoder_text_to_bytes", x)
  # convert 128 to 16 levels.
  # adding 1 here allows both "all no" and "all solid" bars.
  level = int(round((1 + x) / 8))
  fullbars = int(math.floor(level / 2))

  bars = [constants.TEXT_SOLID_BARS] * fullbars
  mid_bars = level % 2
  print("lvl n fullbars:", level, fullbars, mid_bars)
  if mid_bars == 1:
    bars = bars + [constants.TEXT_MID_BARS]

  bars = bars + [constants.TEXT_NO_BARS] * (8 - len(bars))
  print(bars)
  return bars
