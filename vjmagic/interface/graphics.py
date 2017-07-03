import threading
from vjmagic import constants
from vjmagic.interface.quadrant import Quadrant, apply_color
from time import sleep

__BANK_SWITCH_DELAY__ = 5.5
ticker_active = False

def setInterval(func, time):
  global ticker_active
  ticker_active = True
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

__NEW_PALETTES__ = [
  # [33, 41],
  # [37, 45],
  [60, 61],
  [69, 77],
  [82, 90],


  blues,
  oranges,
  [49, 53], # purples
  [45, 41], # blues
  [73, 74], # yelloes
  [92, 93], # pastels

  [120, 121], # reds
  [108, 109], # peachy
  [25, 24], # greens
  # [98, 99], # yellow/orange,

  [56, 57], # pinkurples
]

palette_index = 0

# 2 3
# 0 1
__QUADRANTS__ = []

def load_quadrant(palette, killer, kill_other_layer_on_select, keys, **kwargs):
  # print('load_quadrant called.', palette, killer, kill_other_layer_on_select)
  __QUADRANTS__.append( Quadrant(__NEW_PALETTES__[palette], palette, killer, kill_other_layer_on_select, selected, keys) )

def reset():
    global __QUADRANTS__, ticker_active
    apply_color(0, range(0, 128))
    __QUADRANTS__ = []
    ticker_active = False

    timer = threading.Timer(__BANK_SWITCH_DELAY__, set_ticker_active)
    timer.start()

def set_ticker_active():
  global ticker_active
  ticker_active = True

def loop():
  setInterval(tick_all, 0.14)


def tick_all():
  global ticker_active
  if not ticker_active:
    return
  map(lambda q: q.tick(), __QUADRANTS__)

def handle_note_in(evt):
  killers = map(lambda q: q.check_note(evt[1]), __QUADRANTS__)
  numbers = [e for e in killers if isinstance(e, int)]
  # print('KILLING THESE NUMBERS', numbers)
  # @TODO I think this is getting called "every time" which is too often.
  map(lambda n: __QUADRANTS__[n].unselect(True), numbers)

# check data1 and see if it matches our toggler.
def handle_user_button_presses(evt):
  killers = map(lambda q: q.check_user_button(evt[1]), __QUADRANTS__)


# update palettes
def handle_push_turns(evt):
  global palette_index
  (status, data1, data2) = evt
  # print("graphics push turn:", evt)
  # increment for now
  palette_index = (palette_index + 1) % len(__NEW_PALETTES__)
  # print("idx:")
  for q in __QUADRANTS__:
    updated_idx = (q.palette_id + palette_index) % len(__NEW_PALETTES__)
    q.update_palette(__NEW_PALETTES__[updated_idx])

def start():
    # start in a fun pattern. each quadrant is 4 cells ahead of the last.
    for i in range(0, len(__QUADRANTS__)):
      for _ in range(0, i):
        for _ in range(4):
          __QUADRANTS__[i].tick()
        # __QUADRANTS__[i].tick()
        # __QUADRANTS__[i].tick()
        # __QUADRANTS__[i].tick()
