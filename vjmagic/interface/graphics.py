import threading
from vjmagic import constants
from vjmagic.interface.quadrant import Quadrant

def setInterval(func, time):
  e = threading.Event()
  while not e.wait(time):
    func()

class Graphics:
  def __init__(self, listener, push):
    # TODO
    self.listener = listener
    self.push = push




    self.note_tracker = dict()
    self.notes_toggled_by_user = dict()


    # palette
    blues = [41, 45]
    dark_blues = [46, 47]
    oranges = [60, 61]
    selected = constants.COLOR_GREEN

    self.quadrants = [
      Quadrant(push, dark_blues, constants.BUTTON_QUANTIZE, selected,  (0,0), (3,3)),
      Quadrant(push, blues, constants.BUTTON_DOUBLE, selected, (4,0), (7,3)),
      Quadrant(push, blues, constants.BUTTON_DELETE, selected, (0,4), (3,7)),
      Quadrant(push, oranges, constants.BUTTON_UNDO, selected, (4,4), (7,7)),
    ]

    # listeners for glowy buttons being pressed
    listener.add_listener([constants.MIDI_NOTE_ON, None, None],
      self.handle_note_in, False)

    # listeners for the "layer toggle buttons"
    listener.add_listener([constants.PRESS_USER_BUTTON, constants.BUTTON_QUANTIZE, None],
      self.quadrants[0].unselect, False)
    listener.add_listener([constants.PRESS_USER_BUTTON, constants.BUTTON_DOUBLE, None],
      self.quadrants[1].unselect, False)
    listener.add_listener([constants.PRESS_USER_BUTTON, constants.BUTTON_DELETE, None],
      self.quadrants[2].unselect, False)
    listener.add_listener([constants.PRESS_USER_BUTTON, constants.BUTTON_UNDO, None],
      self.quadrants[3].unselect, False)

    # start in a fun pattern. each quadrant is 4 cells ahead of the last.
    for i in range(0,4):
      for _ in range(0, i):
        self.quadrants[i].tick()
        self.quadrants[i].tick()
        self.quadrants[i].tick()
        self.quadrants[i].tick()

    return

  def loop(self):
    setInterval(self.tick_all, 0.1)

  def tick_all(self):
    map(lambda q: q.tick(), self.quadrants)

  def handle_note_in(self, event):
    map(lambda q: q.check_note(event[1]), self.quadrants)
