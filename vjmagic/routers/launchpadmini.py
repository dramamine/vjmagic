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

active_mask = -1

# constructor
def init():
  global midiinput, midithru
  # setup inputs
  midiinput = rtmidi.MidiIn()
  port = Router.find_port_index(midiinput, "launchpad mini")
  midiinput.open_port(port)
  midiinput.set_callback(handler)

  # vport = "python out"
  midithru = rtmidi.MidiOut()
  portid = Router.find_port_index(midithru, "launchpad mini")
  if portid >= 0:
    midithru.open_port(portid) 
    print("found out port for launchpad.")
  else:
  	print("couldnt find launchpad output, how will my lights work??")
    # midithru.open_virtual_port(vport)

  # initialize_lights()
  # # turn_on_light(3)

def use(res):
  global rezzie
  rezzie = res

  # subscribing to channel 1 note on messages so we know what video
  # is active. resolume does some other stuff on ch1 which causes
  # weird light patterns, so don't listen to too much.
  rezzie.subscribe(constants.MIDI_NOTE_ON, rezzie_message)

def rezzie_message(evt):
  (status, data1, data2) = evt
  # print("rezzie msg", evt)	
  midithru.send_message(evt)

# def initialize_lights():
#   [turn_off_light(x) for x in range(0, 16)]


def handler(event, data=None):
  global active_mask
  evt = event[0]
  (status, data1, data2) = evt
  print("launchpad mini", evt)


  # should we turn the mask off?
  is_off_button = (data1 >= 48 and data1 <= 55)
  if ((data1 == active_mask or is_off_button) and data2 > 0):
  	print("updating active mask to -1")
  	active_mask = -1
  	# 16/cc121, i.e. the 1 button on the mini
  	rezzie.thru([176, 104, 127])
  	return

  # just forwarding everything through for now
  rezzie.thru(evt)

  if (data1 >= 0 and data1 <= 39  and data2 > 0):
  	print("setting active_mask to:", data1)
  	active_mask = data1

  # if status == constants.MIDI_NOTE_ON3:
  #   resolume.handle_button_press(data1)
  # if status == 176:
  #   cc = hardware.get_target_encoder(data1)
  #   if cc >= 0:
  #     rezzie.thru([179, cc, data2])

