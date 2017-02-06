import time
import rtmidi
import itertools
from random import shuffle
# from apscheduler.schedulers.background import BackgroundScheduler
# scheduler = BackgroundScheduler()
device_id = "Ableton Push:Ableton Push MIDI 2 24:1"

midiout = rtmidi.MidiOut()
midiin = rtmidi.MidiIn()

note_tracker = dict()
notes_toggled_by_user = dict()

# palette
blues = [41, 45]
oranges = [60, 61]
selected = 21

quadrant_ll = list(itertools.chain(
  range(36, 40),
  range(44, 48),
  range(52, 56),
  range(60, 64)
))

quadrant_lr = list(itertools.chain(
  range(40, 44),
  range(48, 52),
  range(56, 60),
  range(64, 68),
))

quadrant_ul = list(itertools.chain(
  range(68, 72),
  range(76, 80),
  range(84, 88),
  range(92, 96),
))

quadrant_ur = list(itertools.chain(
  range(72, 76),
  range(80, 84),
  range(88, 92),
  range(96, 100),
))

def note_sender(note):
  note_tracker[note[1]] = 1
  midiout.send_message(note)

def everything_off():
  for note in note_tracker.keys():
    midiout.send_message([0x80, note, 0])

def apply_color(color, list):
  for note in list:
    note_sender([0x90, note, color])

class QuadrantAnimator:
  exception = -1
  palette_iterator = 0
  stack = []

  def __init__(self, palette, quadrant):
    self.palette = palette
    self.quadrant = quadrant

    # color them initially
    apply_color(palette[0], quadrant)

  def tick(self):
    if not self.stack:
      print "initializing stack"
      self.palette_iterator = self.palette_iterator + 1 if self.palette_iterator + 1 < len(self.palette) else 0
      self.stack = list(self.quadrant)
      print self.stack
      print self.quadrant
      shuffle(self.stack)

    chips = self.stack.pop()
    if chips != self.exception:
      apply_color(self.palette[self.palette_iterator], [chips])

  def toggle(self, thing):
    apply_color(selected, [thing])
    self.exception = thing


# def animate_quadrant(palette, quadrant):

def handle_midi_input(event, data=None):
  print event
  message, note, vel = event[0]
  if message == 0x90:
    print "yep this is a note on message"
  print note


available_ports = midiout.get_ports()
push = available_ports.index(device_id)

if push >= 0:
    midiout.open_port(push)
    midiin.open_port(push)
    midiin.set_callback(handle_midi_input)
else:
    midiout.open_virtual_port("My virtual output")
    midiin.open_virtual_port("My virtual input")




# color_to_quadrant(blues[0], quadrant_ll)
# color_to_quadrant(blues[0], quadrant_lr)
# color_to_quadrant(blues[0], quadrant_ul)
# color_to_quadrant(oranges[0], quadrant_ur)

ll = QuadrantAnimator(blues, quadrant_ll)


# note_on = [0x90, 60, 112] # channel 1, middle C, velocity 112
# note_off = [0x80, 60, 0]
# midiout.send_message(note_on)

while(True):
  time.sleep(0.1)
  ll.tick()

everything_off()
# midiout.send_message(note_off)

del midiout
