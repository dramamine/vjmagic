import rtmidi
import itertools

from push.output import AbletonPush
from push.listener import PushEventListener
from push.encoders import Encoders
from push.graphics import Graphics
# from push.quadrantanimator import QuadrantAnimator
# from apscheduler.schedulers.background import BackgroundScheduler
# scheduler = BackgroundScheduler()
ableton_out = "Ableton Push:Ableton Push MIDI 2 24:1"
midiout = rtmidi.MidiOut()


midiinputs = [rtmidi.MidiIn()]

def find_port_index(midi, str):
  for idx, device in enumerate(midi.get_ports()):
    if str in device.lower():
      return idx
  return -1

# open any pushy inputs
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

resolume_in_name = "resolume out"
resin = rtmidi.MidiIn()
portid = find_port_index(resin, resolume_in_name)
if portid >= 0:
    resin.open_port(portid)
else:
    print "didnt find ", resin, "how will I get updates from resolume?"

res_listener = PushEventListener()
resin.set_callback(res_listener.router)

ableton_push_out_name = "midiout2"
portid = find_port_index(midiout, ableton_push_out_name)
if portid >= 0:
    midiout.open_port(portid)
else:
    print "didnt find ", ableton_push_out_name, "how will I send stuff to Push?"
    exit(1)

# for idx, device in enumerate(midiout.get_ports()):
#   print "considering device ", device
#   if "midiout2" in device.lower():
#     print "opening output port:", device
#     midiout.open_port(idx)
#     break

# note: rtmidi doesn't seem super happy about making virtual ports on Windows.
# use loopMidi to define your virtual port ahead of time.
vport = "python out"
midithru = rtmidi.MidiOut()
portid = find_port_index(midithru, vport)
if portid >= 0:
    midithru.open_port(portid)
else:
    midithru.open_virtual_port(vport)



ap = AbletonPush(midiout, midithru)
pel.load_output(ap)

# get those encoders happenin'
encoders = Encoders()
encoders.register_listeners(pel)
encoders.register_resolume_listener(res_listener)
encoders.load_output(ap)

graphics = Graphics(pel, ap)
graphics.loop()


# def note_sender(note):
#   note_tracker[note[1]] = 1
#   midiout.send_message(note)

# def everything_off():
#   for note in note_tracker.keys():
#     midiout.send_message([0x80, note, 0])

# def apply_color(color, list):
#   for note in list:
#     note_sender([0x90, note, color])



# def animate_quadrant(palette, quadrant):

def handle_midi_input(event, data=None):
  print event
  message, note, vel = event[0]
  if message == 0x90:
    print "yep this is a note on message"
  print note




def words():
  # ap.set_user_mode()

  # this clears out a line
  # ap.clearDisplay()

  ap.set_display_bytes(2, map(lambda x: int(x), range(68)))
  ap.set_display_bytes(3, map(lambda x: int(x), range(69,127)))

words()


# everything_off()
# midiout.send_message(note_off)

del midiout
