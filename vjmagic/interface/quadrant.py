from vjmagic import constants
from vjmagic.interface import outpututils
import itertools
from random import shuffle

class Quadrant:
  exception = -1
  palette_iterator = 0
  stack = []

  def __init__(self, palette, toggler, selected, coord_a, coord_b):
    self.palette = palette
    self.selected = selected
    self.toggler = toggler

    # list of all notes in this quadrant
    self.quadrant = coords_to_quadrant(coord_a, coord_b)

    # color them initially
    apply_color(palette[0], self.quadrant)

  def update_palette(self, palette):
    self.palette = palette

  def tick(self):
    if not self.stack:
      self.palette_iterator = self.palette_iterator + 1 if self.palette_iterator + 1 < len(self.palette) else 0
      self.stack = list(self.quadrant)
      shuffle(self.stack)

    chips = self.stack.pop()
    if chips != self.exception:
      apply_color(self.palette[self.palette_iterator], [chips])

  def toggle(self, thing):
    # turn currently active one off.
    if (self.exception > 0):
      apply_color(self.palette[0], [self.exception])

    # save for furure reference
    self.exception = thing

    # make sure our toggler button is on.
    outpututils.light_user_button(self.toggler)

    # actually color the damn thing
    apply_color(self.selected, [thing])

  def unselect(self):
    if self.exception >= 0:
      apply_color(self.palette[0], [self.exception])
    outpututils.unlight_user_button(self.toggler)
    self.exception = -1

  def check_note(self, note):
    if note in self.quadrant:
      self.toggle(note)

def apply_color(color, buttons):
  for note in buttons:
    outpututils.note_sender([constants.MIDI_NOTE_ON, note, color])

# (0,0), (3,3) gives you the lower left quadrant
# (0,0), (7,7) gives you the whole thing
# 0,0 is midi 36
# 7,7 is midi 99
def coords_to_quadrant(coord_a, coord_b):
  (xa, ya) = coord_a
  (xb, yb) = coord_b

  width = xb - xa + 1

  ranges = list()
  for y_iterator in range(ya, yb + 1):
    point = 36 + (y_iterator * 8) + xa
    ranges.append(range(
      point, point + width
    ))

  return list(itertools.chain.from_iterable(ranges))
