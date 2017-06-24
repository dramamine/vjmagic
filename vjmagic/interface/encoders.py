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
# state.active_clip = 0
state.active_effect_clip = 0
state.update_display = None
state.labels = []
state.display_mode = ''
state.display_name = ''

# update the value of an encoder
#
# encoder {Int} The encoder ID (0-8)
# value {Int} The value (0-127)
def update_value(encoder, value):
  state.values[encoder] = value

def get_display_mode():
  return state.display_mode

def set_display_mode(mode, tolabels, active, name = '', audio_reactive = False):
  print("set_display_mode called", mode, tolabels, active, audio_reactive)
  state.active_knobs = active
  if mode == state.display_mode and tolabels == state.labels:
    return
  else:
    print(mode, "was not", state.display_mode)

  if mode == 'BASIC':
    # print("switching to basic display")
    state.update_display = update_display_basic
  elif mode == 'TOUCH':
    # print("switching to touch display")
    # reset values bc it gets weird otherwise
    state.touched = [False] * 9
    state.update_display = update_display_touchy
  elif mode == 'CLIPS':
    state.update_display = update_display_clips
  else:
    print("WTF wrong mode y'all")
    return "WTF"

  if audio_reactive:
    tolabels += [''] * (7 - len(tolabels)) + ['REACTION']
    print "my labels:", tolabels
    state.active_knobs = 8

  state.display_mode = mode
  state.labels = tolabels
  state.display_name = name
  # clear before we do anything...
  outpututils.clear_display()
  state.update_display()

# handle an event coming from the push
def handle_push_turns(event):
  (status, data1, data2) = event
  if state.display_mode == 'CLIPS' and state.active_effect_clip > 0:
      outpututils.thru([constants.MIDI_NOTE_ON, state.active_effect_clip, 127])
      return

  try:
    encoder_idx = constants.ENCODERS.index(data1)
  except ValueError:
    print("Expected ENCODERS to have this value:", data1)
    return
  # print("ok push turns is handled.", event, state.values, encoder_idx)
  # splitting between increments and decrements
  if data2 < 64:
    new_cc = min(127, state.values[encoder_idx] + (SENSITIVITY * data2) )
  else:
    new_cc = max(0, state.values[encoder_idx] - (SENSITIVITY * (128 - data2) ) )

  # print("updating encoder to ", new_cc, "on event:", event)
  # relay the new value from ch1 to ch2
  outpututils.thru([constants.STATUS_CH2, data1, new_cc])

  # we were updating the display here...
  # but now lets try waiting for updates from resolume instead.
  state.values[encoder_idx] = new_cc
  state.update_display()

# ex. (144, 0, 127) means the first knob was touched
# ex. (144, 0, 0) means the first knob was untouched
def handle_push_touches(event):
  (status, data1, data2) = event
  if (data1 > 8):
    return False
  state.touched[data1] = bool(data2)
  # print("touched:", event)
  state.update_display()
  return reroute_push_touches(event)

def save_active_clip(event):
  (status, data1, data2) = event
  # WARNING, we are hardcoding where the effects could be right here!!
  # TODO TODO
  if data1 >= 68 and data1 <= 99:
    # print("new active:", data1)
    state.active_effect_clip = data1

def load_router(keys, data):
  state.router_keys = keys
  state.router_data = data

# depending on the display mode, sometimes we want to
# handle touches differently. this helps with complex
# mappings in Resolume.
# return True if we should eat the output
def reroute_push_touches(event):
  if state.display_mode == 'TOUCH':
    return timeline_routing(event)
  elif state.display_mode == 'CLIPS':
    return cuepoints_routing(event)
  elif state.display_mode == 'BASIC':
    print('encoders.py: eating this touch')
    return True
  return False

# came up with some fancy effects involving the Left-Right
# arrows on Timeline view. unfortunately, it's hard to
# specifically map them due to the way mapping works inside
# a clip. this crunches some numbers and sends them to the
# third channel on some "user buttons" values.
# return True if we should eat the output
def timeline_routing(event):
  (status, data1, data2) = event
  new_evt = [constants.MIDI_NOTE_ON2, data1, data2]
  print("converted to:", new_evt)
  outpututils.thru(new_evt)

# routing specific to being in 'clips' mode (i.e. video clips, no effects)
# routing these to channel 4, just to avoid interference.
# return True if we should eat the output
def cuepoints_routing(event):
  (status, data1, data2) = event
  # if data2 == 0:
  #   return True
  out = [constants.MIDI_NOTE_ON4, data1, data2]
  print("converting to:", out)
  outpututils.thru(out)
  return False

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
  encoders = map(encoder_text_to_bytes, state.values[:state.active_knobs])

  # removing encodings if there are no labels
  for index, item in enumerate(state.labels):
    if not item:
      encoders[index] = [constants.TEXT_BLANK] * 8

  chained = list(itertools.chain.from_iterable(encoders))
  # sorry. adding blank spaces since width is 68, not 64

  for width in [56, 40, 24, 8]:
    if len(chained) > width:
      # print("adding blank here:", width)
      chained[width:width] = [constants.TEXT_BLANK]

  outpututils.set_display_bytes(0, chained)
  # labels
  outpututils.set_display_cells(1,
    state.labels + [''] * (8 - len(state.labels)) # pad to 8 with empty strings
  )

  outpututils.clear_display_line(2)

  outpututils.set_display_line(3, state.display_name)


# # load this func on start
# state.update_display = update_display_basic

# update the display using 'touch' mode
def update_display_touchy():
  val_labels = map(lambda x, y: 'x'*8 if x else y, state.touched[:state.active_knobs], state.labels)
  outpututils.set_display_cells(0, val_labels)

  val_cells = map(lambda x: 'x'*8 if x else ' '*8, state.touched[:state.active_knobs])
  outpututils.set_display_cells(1, val_cells)
  outpututils.set_display_cells(2, val_cells)

  to_line = outpututils.cells_to_line(val_cells)
  with_name = state.display_name + to_line[len(state.display_name):len(to_line)]
  outpututils.set_display_line(3, with_name)

# update the display using 'clips' mode
# just add some labels... no interactions.
def update_display_clips():
  # labels
  val_labels = map(lambda x, y: 'x'*8 if x else y, state.touched[:state.active_knobs], state.labels)
  outpututils.set_display_cells(0, val_labels)

  val_cells = map(lambda x: 'x'*8 if x else ' '*8, state.touched[:state.active_knobs])
  outpututils.set_display_cells(1, val_cells)
  outpututils.set_display_cells(2, val_cells)

  to_line = outpututils.cells_to_line(val_cells)
  with_name = state.display_name + to_line[len(state.display_name):len(to_line)]
  outpututils.set_display_line(3, with_name)

def encoder_text_to_bytes(x):
  # convert 128 to 16 levels.
  # adding 1 here allows both "all no" and "all solid" bars.
  level = int(round((1 + x) / 8))
  fullbars = int(math.floor(level / 2))

  bars = [constants.TEXT_SOLID_BARS] * fullbars
  mid_bars = level % 2
  if mid_bars == 1:
    bars = bars + [constants.TEXT_MID_BARS]

  bars = bars + [constants.TEXT_NO_BARS] * (8 - len(bars))
  return bars
