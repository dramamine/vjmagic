
import time
from quadrant import Quadrant
import constants

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
    oranges = [60, 61]
    selected = constants.COLOR_GREEN

    self.quadrants = [
      Quadrant(push, blues, selected, (0,0), (3,3)),
      Quadrant(push, blues, selected, (4,0), (7,3)),
      Quadrant(push, blues, selected, (0,4), (3,7)),
      Quadrant(push, oranges, selected, (4,4), (7,7)),
    ]
    return

  def loop(self):
    while(True):
      time.sleep(0.1)
      for quadrant in self.quadrants:
        quadrant.tick()

  def handle_note_in(self, event):
    print "got a note in message"
