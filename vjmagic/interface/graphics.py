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

__PALETTES__ = [
  [[46, 47], [41, 45], [60, 61], constants.COLOR_GREEN],
  [[56, 57], [60, 61], [41, 45], constants.COLOR_GREEN]
]

palette_index = 0

# 2 3
# 0 1
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
    __QUADRANTS__[quad].unselect()
  except ValueError:
    pass

# fucking TODO. this will be fun
def handle_push_turns(evt):
  global palette_index
  (status, data1, data2) = evt
  print("graphics push turn:", evt)
  # increment for now
  palette_index = (palette_index + 1) % len(__PALETTES__)
  print("idx:")

  # basically hardcoded to 4 quadrants.. :shrug:
  __QUADRANTS__[0].update_palette( __PALETTES__[palette_index][0] )
  __QUADRANTS__[1].update_palette( __PALETTES__[palette_index][1] )
  __QUADRANTS__[2].update_palette( __PALETTES__[palette_index][1] )
  __QUADRANTS__[3].update_palette( __PALETTES__[palette_index][2] )

# start in a fun pattern. each quadrant is 4 cells ahead of the last.
for i in range(0,4):
  for _ in range(0, i):
    __QUADRANTS__[i].tick()
    __QUADRANTS__[i].tick()
    __QUADRANTS__[i].tick()
    __QUADRANTS__[i].tick()
