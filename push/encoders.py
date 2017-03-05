


import constants

ENCODERS = [71, 72, 73, 74, 75, 76, 77, 78, 79]

INCREMENT = 1
DECREMENT = 127

SENSITIVITY = 1

class Encoders:
  touched = [False] * 9
  values = [0] * 9
  active_knobs = 8
  ableton_out = None
  update_display = None
  labels = []

  #
  def __init__(self):
    self.update_display = self.update_display_basic
    return

  # register listeners for updates coming from the push
  # listener {EventListener} the listener from "push out"
  def register_listeners(self, listener):
    for x in ENCODERS:
      listener.add_listener([constants.STATUS_CH1, x, None], self.handle_push_turns, True)

    listener.add_listener([constants.MIDI_NOTE_ON, None, None], self.handle_push_touches, False)

  # register listeners coming from resolume.
  # listener {EventListener} the listener from "resolume out"
  def register_resolume_listener(self, listener):
    listener.add_listener([constants.STATUS_CH2, None, None], self.handle_resolume_updates, True)

  # load "ableton out" port
  def load_output(self, ableton_out):
    self.ableton_out = ableton_out
    self.update_display()

  # update the value of an encoder
  #
  # encoder {Int} The encoder ID (0-8)
  # value {Int} The value (0-127)
  def update_value(self, encoder, value):
    self.values[encoder] = value


  def set_display_mode(self, mode, labels):
    self.ableton_out.clear_display()
    if mode == 'BASIC':
      self.update_display = self.update_display_basic
      self.labels = labels
    elif mode == 'TOUCH':
      self.update_display = self.update_display_touchy
    else:
      print "WTF wrong mode y'all"
      return "WTF"

    # set labels
    self.update_display

  # handle an event coming from the push
  def handle_push_turns(self, event):
    (status, data1, data2) = event
    try:
        encoder = ENCODERS.index(data1)
    except ValueError:
        return None

    # splitting between increments and decrements
    if data2 < 64:
        new_cc = min(127, self.values[encoder] + (SENSITIVITY * data2) )
    else:
        new_cc = max(0, self.values[encoder] - (SENSITIVITY * (128 - data2) ) )

    print "updating encoder to ", new_cc, "on event:", event
    # relay the new value from ch1 to ch2
    self.ableton_out.thru([STATUS_CH2, data1, new_cc])

    # we were updating the display here...
    # but now lets try waiting for updates from resolume instead.
    # self.values[encoder] = new_cc
    # self.update_display()

  # ex. (144, 0, 127) means the first knob was touched
  # ex. (144, 0, 0) means the first knob was untouched
  def handle_push_touches(self, event):
    (status, data1, data2) = event
    if (data1 > 8):
      return
    self.touched[data1] = bool(data2)
    self.update_display()




  # handle an event coming from resolume
  def handle_resolume_updates(self, event):
    (status, data1, data2) = event
    try:
      encoder = ENCODERS.index(data1)
    except ValueError:
      return None

    print "resolume sez: set encoder ", encoder, " with index", data1, " from ", self.values[encoder], " to ", data2
    self.values[encoder] = data2
    self.update_display()

  def update_display_basic(self):
    val_strings = map(lambda x: str(x).center(8), self.values[:self.active_knobs])
    # annoying spacing
    outstr = ''
    ctr = 0
    for val_string in val_strings:
      outstr = outstr + val_string
      if ctr % 2 == 0:
        outstr = outstr + " "
      ctr = ctr + 1

    self.ableton_out.set_display_line(0, outstr)

    # labels
    self.ableton_out.set_display_cells(1,
      self.labels + [''] * (8 - len(self.labels)) # pad to 8 with empty strings
    )

  def update_display_touchy(self):
    val_cells = map(lambda x: 'x'*8 if x else ' '*8, self.touched[:self.active_knobs])
    print "here are my cell vals:", val_cells
    self.ableton_out.set_display_cells(0, val_cells)
    self.ableton_out.set_display_cells(1, val_cells)
    self.ableton_out.set_display_cells(2, val_cells)
    self.ableton_out.set_display_cells(3, val_cells)
