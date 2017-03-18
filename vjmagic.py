import rtmidi
import itertools
import time
import sys, os

# import push
# import routers

from vjmagic.interface import outpututils
from vjmagic.interface.listener import PushEventListener
# from vjmagic.interface.encoders import Encoders
from vjmagic.interface.encoder_controller import EncoderController
from vjmagic.interface.graphics import Graphics

from vjmagic.routers.pushrouter import PushRouter
from vjmagic.routers.resolumerouter import ResolumeRouter

# always flush stdout
# http://stackoverflow.com/questions/230751/how-to-flush-output-of-python-print
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

midiout = rtmidi.MidiOut()
# midiinputs = [rtmidi.MidiIn()]

def find_port_index(midi, str):
  for idx, device in enumerate(midi.get_ports()):
    if str in device.lower():
      return idx
  return -1

# open any pushy inputs
pel = PushEventListener()
# for idx, device in enumerate(midiinputs[0].get_ports()):
#   print "considering device ", device
#   if "ableton push" in device.lower():
#     print "opening input port:", device
#     midiinputs[0].open_port(idx)
#     midiinputs[0].set_callback(pel.router)

#     midiinputs = [rtmidi.MidiIn()] + midiinputs
#     # pel.load_midiin(midiin)
#     #midiin = rtmidi.MidiIn()
#     # break




# resolume_in_name = "resolume out"
# resin = rtmidi.MidiIn()
# portid = find_port_index(resin, resolume_in_name)
# if portid >= 0:
#     resin.open_port(portid)
# else:
#     print "didnt find ", resin, "how will I get updates from resolume?"

# eating stuff like 'note on', since Resolume relays those, but Push already told us.
# however, we want to send CCs on because those should be in sync with Resolume.
# res_listener = PushEventListener()
# res_listener.add_whitelist([177, None, None])
# res_listener.add_whitelist([178, None, None])
# resin.set_callback(res_listener.silent_router)


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



# ap = AbletonPush(midiout, midithru)
outpututils.midiout = midiout
outpututils.midithru = midithru

#
pel.load_output(outpututils)

# get those encoders happenin'
# encoders = Encoders()
# encoders.register_listeners(pel)
# encoders.register_resolume_listener(res_listener)
# encoders.load_output(outpututils)

# ec = EncoderController(encoders)
# ec.register_listeners(pel)
#
draft = [
  ['TOUCH', None, [
    72, 73, 74, 75,
    80, 81, 82, 83,
    88, 89, 90, 91,
    96, 97, 98, 99]],
  ['BASIC', ['STR', 'MAG', 'INT', 'DEX', 'CON'], range(36,39)]
]

# ec.load_config(draft)

aol = PushRouter()
print "aol loaded"

res = ResolumeRouter()
print "res loaded"

def words():
  # ap.set_user_mode()

  # this clears out a line
  # ap.clearDisplay()

  outpututils.set_display_bytes(2, map(lambda x: int(x), range(68)))
  outpututils.set_display_bytes(3, map(lambda x: int(x), range(69,127)))

words()

graphics = Graphics(pel, outpututils)
graphics.loop()


# everything_off()
# midiout.send_message(note_off)

# del midiout
