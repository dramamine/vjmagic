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

# constructor
def init():
  global midiinput, midithru
  # setup inputs
  midiinput = rtmidi.MidiIn()
  port = Router.find_port_index(midiinput, "twister")
  midiinput.open_port(port)
  midiinput.set_callback(handler)

  vport = "python out"
  midithru = rtmidi.MidiOut()
  portid = Router.find_port_index(midithru, "twister")
  if portid >= 0:
      midithru.open_port(portid)
      print("found out port.")
  else:
      midithru.open_virtual_port(vport)

  initialize_lights()
  # turn_on_light(3)

def use(res):
  global rezzie
  rezzie = res

def initialize_lights():
  [turn_off_light(x) for x in range(0, 16)]


def handler(event, data=None):
  evt = event[0]
  (status, data1, data2) = evt
  print("Twister", evt)

  # if status == constants.MIDI_NOTE_ON3:
  #   resolume.handle_button_press(data1)
  if status == 176:
    cc = hardware.get_target_encoder(data1)
    if cc >= 0:
      rezzie.thru([179, cc, data2])


def turn_on_light(encoder):
  print("turning a light on")
  # sets rgbs to ON
  midithru.send_message([constants.FIGHTER_ENCODER_SWITCHES, encoder, 127])    
  # turn on encoder rings, value 0... @TODO we prob have initial value from rezzie
  midithru.send_message([constants.FIGHTER_ENCODERS, encoder, 0])    
  # turn up encoder brightness (65-94)
  midithru.send_message([constants.FIGHTER_ENCODER_ANIMATIONS, encoder, 94])

  # midithru.send_message([constants.MIDI_NOTE_ON, encoder, color])
  # midithru.send_message([constants.FIGHTER_ENCODER_SWITCHES, 0, 64])
  # midithru.send_message([constants.FIGHTER_ENCODER_SWITCHES, 1, 64])

  # # setting brightness
  # midithru.send_message([constants.FIGHTER_ENCODER_ANIMATIONS, 0, 17])
  # midithru.send_message([constants.FIGHTER_ENCODER_ANIMATIONS, 1, 27])

  # # setting indicator brightness
  # midithru.send_message([constants.FIGHTER_ENCODER_ANIMATIONS, 0, 65])
  # midithru.send_message([constants.FIGHTER_ENCODER_ANIMATIONS, 1, 95])

def turn_off_light(encoder):
  print("turning off ", encoder)
  # midithru.send_message([constants.FIGHTER_ENCODER_SWITCHES, encoder, 64]) 
  # midithru.send_message([constants.FIGHTER_ENCODER_SWITCHES, encoder, 65])
  # turns on encoder rings??
  # midithru.send_message([constants.FIGHTER_ENCODERS, encoder, 127])
  # sets rgb to blue
  # midithru.send_message([constants.FIGHTER_ENCODER_SWITCHES, encoder, 17])
  # sets rgbs to ON
  # midithru.send_message([constants.FIGHTER_ENCODER_SWITCHES, encoder, 127])

  # sets rgbs to OFF
  midithru.send_message([constants.FIGHTER_ENCODER_SWITCHES, encoder, 0])

  # turn off encoder rings
  midithru.send_message([constants.FIGHTER_ENCODERS, encoder, 0])

  # turn down encoder brightness (65-94)
  midithru.send_message([constants.FIGHTER_ENCODER_ANIMATIONS, encoder, 65])