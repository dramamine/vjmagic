import threading
import constants
from quadrant import Quadrant

def setInterval(func, time):
  e = threading.Event()
  while not e.wait(time):
    func()

class Graphics:
  def __init__(self, listener, push):
    # TODO
    self.listener = listener
    self.push = push

    listener.add_listener([constants.MIDI_NOTE_ON, None, None],
      self.handle_note_in, False)

    self.note_tracker = dict()
    self.notes_toggled_by_user = dict()


    # palette
    blues = [41, 45]
    dark_blues = [46, 47]
    oranges = [60, 61]
    selected = constants.COLOR_GREEN

    self.quadrants = [
      Quadrant(push, dark_blues, selected, (0,0), (3,3)),
      Quadrant(push, blues, selected, (4,0), (7,3)),
      Quadrant(push, blues, selected, (0,4), (3,7)),
      Quadrant(push, oranges, selected, (4,4), (7,7)),
    ]

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
    print "got a note in message"
