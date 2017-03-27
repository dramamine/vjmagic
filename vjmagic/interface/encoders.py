from vjmagic import constants
from vjmagic.interface import outpututils

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
state.display_mode = 'BASIC'


# class Encoders:
#   touched = [False] * 9
#   values = [0] * 9
#   active_knobs = 8
#   ableton_out = None
#   update_display = None
#   labels = []
#   display_mode = ''

#   #
#   def __init__(self):
#     self.update_display = self.update_display_basic
#     self.display_mode =
#     return

# register listeners for updates coming from the push
# listener {EventListener} the listener from "push out"
# def register_listeners(self, listener):
#   for x in ENCODERS:
#     listener.add_listener([constants.STATUS_CH1, x, None], self.handle_push_turns, True)

#   listener.add_listener([constants.MIDI_NOTE_ON, None, None], self.handle_push_touches, False)



# register listeners coming from resolume.
# listener {EventListener} the listener from "resolume out"
# def register_resolume_listener(self, listener):
#   listener.add_listener([constants.STATUS_CH2, None, None], self.handle_resolume_updates, True)

# load "ableton out" port
# def load_output(self, ableton_out):
#   ableton_out = ableton_out
#   update_display()

# update the value of an encoder
#
# encoder {Int} The encoder ID (0-8)
# value {Int} The value (0-127)
def update_value(encoder, value):
  state.values[encoder] = value


def set_display_mode(mode, tolabels):
  print "set_display_mode called", mode, tolabels
  if mode == state.display_mode:
    return
  else:
    print mode, "was not", state.display_mode

  if mode == 'BASIC':
    print "switching to basic display"
    outpututils.clear_display_line(2)
    outpututils.clear_display_line(3)
    state.update_display = update_display_basic
    state.labels = tolabels
    print "switched"
  elif mode == 'TOUCH':
    print "switching to touch display"
    # reset values bc it gets weird otherwise
    state.touched = [False] * 9
    state.update_display = update_display_touchy
  else:
    print "WTF wrong mode y'all"
    return "WTF"

  state.display_mode = mode
  # clear before we do anything...
  outpututils.clear_display()
  state.update_display()

# handle an event coming from the push
def handle_push_turns(event):
  (status, data1, data2) = event
  print "ok push turns is handled.", event
  try:
    encoder = ENCODERS.index(data1)
  except ValueError:
    return None

  # splitting between increments and decrements
  if data2 < 64:
    new_cc = min(127, state.values[encoder] + (SENSITIVITY * data2) )
  else:
    new_cc = max(0, state.values[encoder] - (SENSITIVITY * (128 - data2) ) )

  print "updating encoder to ", new_cc, "on event:", event
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
  print "touched:", event
  state.update_display()

# handle an event coming from resolume
def handle_resolume_updates(event):
  (status, data1, data2) = event
  try:
    encoder = ENCODERS.index(data1)
  except ValueError:
    print "couldnt find", data1
    return None

  print "resolume sez: set encoder ", encoder, " with index", data1, " from ", state.values[encoder], " to ", data2
  state.values[encoder] = data2
  state.update_display()


## update the display using 'basic' mode
def update_display_basic():
  # print "update display basic called"
  val_strings = map(lambda x: str(x).center(8), state.values[:state.active_knobs])
  # annoying spacing
  outstr = ''
  ctr = 0
  for val_string in val_strings:
    outstr = outstr + val_string
    if ctr % 2 == 0:
      outstr = outstr + " "
    ctr = ctr + 1

  outpututils.set_display_line(0, outstr)

  # labels
  outpututils.set_display_cells(1,
    state.labels + [''] * (8 - len(state.labels)) # pad to 8 with empty strings
  )

# load this func on start
state.update_display = update_display_basic

# update the display using 'touch' mode
def update_display_touchy():
  val_cells = map(lambda x: 'x'*8 if x else ' '*8, state.touched[:state.active_knobs])
  outpututils.set_display_cells(0, val_cells)
  outpututils.set_display_cells(1, val_cells)
  outpututils.set_display_cells(2, val_cells)
  outpututils.set_display_cells(3, val_cells)
