import threading
from vjmagic import constants
from vjmagic.interface.quadrant import Quadrant, apply_color

SLOWEST_POSSIBLE_SPEED = 1.3
SPEED_INTERVAL = 0.01
running = False
tick_interval = 0.14
tick_speed_level = 35

# new threading strat
pill2kill = None
t = None


# set once and forget, use globals to make changes
def start_interval(func):
  global running, tick_interval
  e = threading.Event()
  running = True
  while running and not e.wait(tick_interval):
    func()

# in case we want
def pause_interval():
  global running
  running = False

def adjust_color_speed(evt):
  global tick_speed_level, SPEED_INTERVAL, SLOWEST_POSSIBLE_SPEED
  (status, data1, data2) = evt
  # turn data2 into an amount by which to adjust
  adjustment = min(128 - data2, data2)
  tick_speed_level = min(max(0, tick_speed_level + adjustment), 127)
  tick_interval = SLOWEST_POSSIBLE_SPEED - (tick_speed_level * SPEED_INTERVAL)
  print("updated color speed:", tick_speed_level, tick_interval)
  reset_timer()


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
    global __QUADRANTS__

    apply_color(0, range(0, 128))
    __QUADRANTS__ = []
    reset_timer()

def reset_timer():
  global __QUADRANTS__, pill2kill, t
  # pill2kill.set()
  # t.join()
  loop()

def loop():
  global pill2kill, t
  # start_interval(tick_all)
  pill2kill = threading.Event()
  t = threading.Thread(target=doit, args=(pill2kill, tick_all))
  t.start()
  doit(pill2kill, tick_all)

def doit(stop_event, func):
    while not stop_event.wait(1):
        func()
    print("Stopping as you wish.")


def tick_all():
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
  print("graphics push turn:", evt)
  # increment for now
  palette_index = (palette_index + 1) % len(__NEW_PALETTES__)
  print("idx:")
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
