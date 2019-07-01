# from push.listener import PushEventListener
from vjmagic import constants
import rtmidi
from vjmagic.routers.base import Router
from vjmagic.state import hardware
from time import sleep
# from vjmagic.state import hardware
# from vjmagic.interface import encodercontroller, encoders, banks, graphics, outpututils

rezzie = None

midiinput = None
midithru = None

active_clip = -1
active_mask = -1

clip_colors = [9, 77, 78, 80, 82, 95, 16, 96, 32, 105, 107, 113, 52, 121]
clip_color_idx = 0
active_clip_color = 122

mask_color_idx = 4

def is_clip(data1):
  return data1 in range(68, 100) or data1 in [39, 43, 47, 51, 55, 59, 63, 67]

def is_mask(data1):
  return data1 in [36, 37, 40, 41,  44, 45, 48, 49,
            52, 53, 56, 57, 60, 61, 64, 65
            ]
def is_off_button(data1):
  return data1 in [38, 42, 46, 50, 54, 58, 62, 66]

# constructor
def init(skip=False):
  global midiinput, midithru
  # setup inputs
  midiinput = rtmidi.MidiIn()
  port = Router.find_port_index(midiinput, "midi fighter 64", skip)
  midiinput.open_port(port)
  midiinput.set_callback(handler)

  # vport = "python out"
  midithru = rtmidi.MidiOut()
  portid = Router.find_port_index(midithru, "midi fighter 64", skip)
  if portid >= 0:
    midithru.open_port(portid) 
    print("found out port for mf64-white.")
  else:
    print("couldnt find mf64-white output, how will my lights work??")
    # midithru.open_virtual_port(vport)

  # initialize_lights()
  cycle_colors()

def use(res):
  global rezzie
  rezzie = res

  # subscribing to channel 1 note on messages so we know what video
  # is active. resolume does some other stuff on ch1 which causes
  # weird light patterns, so don't listen to too much.
  rezzie.subscribe(constants.MIDI_NOTE_ON6, rezzie_message)
  rezzie.subscribe(constants.MIDI_NOTE_OFF6, rezzie_message)

def rezzie_message(evt):
  global active_clip, active_mask
  (status, data1, data2) = evt
  print("rezzie msg to mf64-white", evt, flush=True)  

  if data2 == 32:
    # it's no longer active
    color = 0
    if is_clip(data1):
      color = clip_colors[clip_color_idx]
      active_clip = -1
    elif is_mask(data1):
      color = clip_colors[mask_color_idx]
      active_mask = -1

    midithru.send_message([status, data1, color])
  elif data2 == 95:
    # it is now active
    midithru.send_message([status, data1, active_clip_color])
    if is_clip(data1):
      active_clip = data1
      print("set active clip:", active_clip, flush=True)
    elif is_mask(data1):
      active_mask = data1


def handler(event, data=None):
  global active_mask
  evt = event[0]
  (status, data1, data2) = evt
  print("midi fighter 64 white:", evt)

  # should we turn the mask off?
  if (status == constants.MIDI_NOTE_ON6 and (data1 == active_mask or is_off_button(data1)) and data2 > 0):
    print("updating active mask to -1")
    active_mask = -1
    # 16/cc121, i.e. the 1 button on the mini
    rezzie.thru([status, 127, 127])
    rezzie.thru([status, 127, 0])
    cycle_colors()
    return

  # just forwarding everything through for now
  rezzie.thru(evt)

def cycle_colors():
  global clip_color_idx, mask_color_idx
  clip_color_idx = (clip_color_idx + 1) % len(clip_colors)
  mask_color_idx = (mask_color_idx + 2) % len(clip_colors)

  if (clip_color_idx == mask_color_idx):
    mask_color_idx = (mask_color_idx + 1) % len(clip_colors)

  clip_color = clip_colors[clip_color_idx]
  mask_color = clip_colors[mask_color_idx]

  print("using clip and mask:", clip_color, mask_color, flush=True)

  important_datas = range(36,100)
  for data1 in important_datas:
    if (data1 == active_clip or data1 == active_mask):
      print("skipping active clip", data1, flush=True)
      continue

    if is_clip(data1):
      midithru.send_message([constants.MIDI_NOTE_ON6, data1, clip_color])
    elif is_mask(data1):
      midithru.send_message([constants.MIDI_NOTE_ON6, data1, mask_color])
