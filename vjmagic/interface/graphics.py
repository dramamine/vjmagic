import threading
from vjmagic import constants
from vjmagic.interface.quadrant import Quadrant

def setInterval(func, time):
  e = threading.Event()
  while not e.wait(time):
    func()

__NOTE_TRACKER__ = dict()
__NOTES_TOGGLED_BY_USER__ = dict()
blues = [41, 45]
dark_blues = [46, 47]
oranges = [60, 61]
selected = constants.COLOR_GREEN

__QUADRANTS__ = [
  Quadrant(dark_blues, constants.BUTTON_QUANTIZE, selected,  (0,0), (3,3)),
  Quadrant(blues, constants.BUTTON_DOUBLE, selected, (4,0), (7,3)),
  Quadrant(blues, constants.BUTTON_DELETE, selected, (0,4), (3,7)),
  Quadrant(oranges, constants.BUTTON_UNDO, selected, (4,4), (7,7)),
]


def loop():
  setInterval(tick_all, 0.1)

def tick_all():
  map(lambda q: q.tick(), __QUADRANTS__)

def handle_note_in(event):
  map(lambda q: q.check_note(event[1]), __QUADRANTS__)

def handle_user_button_presses(evt):
  (status, data1, data2) = evt
  try:
    quad = constants.LAYER_TOGGLE_BUTTONS.index(data1)
    print "found LAYER_TOGGLE_BUTTONS => quad", quad
    __QUADRANTS__[quad].unselect
  except ValueError:
    pass

# fucking TODO. this will be fun
def handle_push_turns(evt):
  (status, data1, data2) = evt



# start in a fun pattern. each quadrant is 4 cells ahead of the last.
for i in range(0,4):
  for _ in range(0, i):
    __QUADRANTS__[i].tick()
    __QUADRANTS__[i].tick()
    __QUADRANTS__[i].tick()
    __QUADRANTS__[i].tick()


# class Graphics:
#   def __init__(self, listener):
#     # TODO
#     self.listener = listener

#     self.note_tracker = dict()
#     self.notes_toggled_by_user = dict()


#     # listeners for glowy buttons being pressed
#     listener.add_listener([constants.MIDI_NOTE_ON, None, None],
#       self.handle_note_in, False)

#     # listeners for the "layer toggle buttons"
#     # listener.add_listener([constants.PRESS_USER_BUTTON, constants.BUTTON_QUANTIZE, None],
#     #   self.quadrants[0].unselect, False)
#     # listener.add_listener([constants.PRESS_USER_BUTTON, constants.BUTTON_DOUBLE, None],
#     #   self.quadrants[1].unselect, False)
#     # listener.add_listener([constants.PRESS_USER_BUTTON, constants.BUTTON_DELETE, None],
#     #   self.quadrants[2].unselect, False)
#     # listener.add_listener([constants.PRESS_USER_BUTTON, constants.BUTTON_UNDO, None],
#     #   self.quadrants[3].unselect, False)




