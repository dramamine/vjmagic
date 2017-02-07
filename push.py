import time
import rtmidi
import itertools
from random import shuffle
from abletonpush import AbletonPush
from pusheventlistener import PushEventListener
# from apscheduler.schedulers.background import BackgroundScheduler
# scheduler = BackgroundScheduler()
ableton_out = "Ableton Push:Ableton Push MIDI 2 24:1"
midiout = rtmidi.MidiOut()


midiinputs = [rtmidi.MidiIn()]

pel = PushEventListener()
for idx, device in enumerate(midiinputs[0].get_ports()):
  print "considering device ", device
  if "ableton push" in device.lower():
    print "opening input port:", device
    midiinputs[0].open_port(idx)
    midiinputs[0].set_callback(pel.router)

    midiinputs = [rtmidi.MidiIn()] + midiinputs
    # pel.load_midiin(midiin)
    #midiin = rtmidi.MidiIn()
    # break



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
  range(60, 64),
  range(101, 105)
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
      self.palette_iterator = self.palette_iterator + 1 if self.palette_iterator + 1 < len(self.palette) else 0
      self.stack = list(self.quadrant)
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
push = available_ports.index(ableton_out)

if push >= 0:
    midiout.open_port(push)
    # midiin.open_port(push)
    # midiin.set_callback(handle_midi_input)
else:
    midiout.open_virtual_port("My virtual output")
    midiin.open_virtual_port("My virtual input")

ap = AbletonPush(midiout)
print "yep got an AP object"


# color_to_quadrant(blues[0], quadrant_ll)
# color_to_quadrant(blues[0], quadrant_lr)
# color_to_quadrant(blues[0], quadrant_ul)
# color_to_quadrant(oranges[0], quadrant_ur)

ll = QuadrantAnimator(blues, quadrant_ll)
lr = QuadrantAnimator(blues, quadrant_lr)
ul = QuadrantAnimator(blues, quadrant_ul)
ur = QuadrantAnimator(oranges, quadrant_ur)

def words():
  # ap.set_user_mode()

  # this clears out a line
  ap.clearDisplay()
  print ap.get_bytes("HELLO WORLD")

  ap.set_display_line(1, "HELLO WORLD")


  # midiout.send_message([240, 71, 127, 21, 24, 0, 69, 0,
  #   33,33,33,33,3,3,3,3,
  #   3,3,3,3,3,3,3,3,
  #   3,3,3,3,3,3,3,3,
  #   3,3,3,3,3,3,3,3,
  #   3,3,3,3,3,3,3,3,
  #   3,3,3,3,3,3,3,3,
  #   3,3,3,3,3,3,3,3,
  #   3,3,3,3,3,3,3,3,
  #   3,3,3,3,
  #   247
  # ])
  # midiout.send_message([240, 71, 127, 21, 30, 0, 0, 247])



# note_on = [0x90, 60, 112] # channel 1, middle C, velocity 112
# note_off = [0x80, 60, 0]
# midiout.send_message(note_on)

words()

while(True):
  time.sleep(0.1)
  ll.tick()
  lr.tick()
  ul.tick()
  ur.tick()

everything_off()
# midiout.send_message(note_off)

del midiout
