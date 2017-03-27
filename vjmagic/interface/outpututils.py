# Ableton Push Basic MIDI Implementation.pdf
# https://app.box.com/s/w900ll2tq3tj83raes2a
#
SYSEX_START = [240, 71, 127, 21]
SYSEX_TERM = [247]

from vjmagic import constants
import rtmidi
from vjmagic.routers.base import Router

ableton_push_out_name = "midiout2"
midiout = rtmidi.MidiOut()
portid = Router.find_port_index(midiout, ableton_push_out_name)
if portid >= 0:
    midiout.open_port(portid)
else:
    print("didnt find ", ableton_push_out_name, "how will I send stuff to Push?")
    # exit(1)

# note: rtmidi doesn't seem super happy about making virtual ports on Windows.
# use loopMidi to define your virtual port ahead of time.
vport = "python out"
midithru = rtmidi.MidiOut()
portid = Router.find_port_index(midithru, vport)
if portid >= 0:
    midithru.open_port(portid)
else:
    midithru.open_virtual_port(vport)


def clear_display_line(line):
  idx = 28 + line
  msg = SYSEX_START + [idx, 0, 0] + SYSEX_TERM
  midiout.send_message(msg)

def set_display_cells(line, cells):
  val_strings = map(lambda x: str(x).center(8), cells[:8])
  # annoying spacing
  outstr = ''
  ctr = 0
  for val_string in val_strings:
    outstr = outstr + val_string
    if ctr % 2 == 0:
      outstr = outstr + " "
    ctr = ctr + 1
  set_display_line(line, outstr)

def set_display_line(line, str):
  set_display_bytes(line, get_bytes(str))

def set_display_bytes(line, bytes):
  # pad to 68
  while len(bytes) < 68:
    bytes.append(32)
  msg = SYSEX_START + [(24 + line), 0, 69, 0] + bytes + SYSEX_TERM
  midiout.send_message(msg)

def clear_display():
  # TODO map
  for i in range(0,3):
    clear_display_line(i)

# true for user mode, false for live mode
def set_user_mode(user=True):
  msg = SYSEX_START + [98, 0, 1, int(user)] + SYSEX_TERM
  midiout.send_message(msg)

def get_bytes(str):
  bytes = []
  for c in str:
    bytes.append(int(c.encode('hex'), 16))
  return bytes

def thru(event):
    midithru.send_message(event)

def note_sender(note):
  # note_tracker[note[1]] = 1
  midiout.send_message(note)

def light_user_button(button):
  midiout.send_message([constants.PRESS_USER_BUTTON, button, 127])

def unlight_user_button(button):
  midiout.send_message([constants.PRESS_USER_BUTTON, button, 0])
