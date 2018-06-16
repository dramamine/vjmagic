# from push.listener import PushEventListener
from vjmagic import constants
import rtmidi
from vjmagic.routers.base import Router
from vjmagic.state import hardware
from time import sleep
from vjmagic.config.midifighter import config
# from vjmagic.state import hardware
# from vjmagic.interface import encodercontroller, encoders, banks, graphics, outpututils

rezzie = None
midiinput = None
midithru = None

color_offsets = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 
  -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

press_count = 0

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
  # [turn_off_light(x) for x in range(0, 16)]
  set_off_colors()
  # set_animation(15, constants.TWISTER_ANIMATION_RAINBOW)


def set_off_colors(offset = 0):
  for x in range(0, 16):
    if config['off_colors'][x] == 0:
      color = 0
    else: 
      color = max(min(config['off_colors'][x] + offset, 127), 1)
    set_off_color(x, color)

def handle_effect_press(fresh = False):
  global press_count
    
  if fresh:
    set_animation(15, constants.TWISTER_ANIMATION_RAINBOW)

  # magic to increment colors
  press_count = press_count + 1
  idx = press_count % len(color_offsets)
  set_off_colors(color_offsets[idx])

  # increment colors
  set_animation(0, 0)
  set_animation(1, 0)
  set_animation(2, 0)
  set_animation(3, 0)
  set_animation(4, 0)
  set_animation(5, 0)
  set_animation(6, 0)
  set_animation(7, 0)

def handle_effect_release():
  set_animation(15, 0)


def handler(event, data=None):
  evt = event[0]
  (status, data1, data2) = evt
  print("Twister", evt)

  # if status == constants.MIDI_NOTE_ON3:
  #   resolume.handle_button_press(data1)
  if status >= 176 and status <= 179:
    # forward everything to channel 4
    # (176 is channel 1, so 179 is channel 4)
    rezzie.thru([179, data1, data2])


    # the 4th knob is only active if the 3rd knob is.
    if data1 == 2:
      if data2 > 0:
        set_off_color(3, config['off_colors'][2])
      else:
        set_off_color(3, 0)

    # the 8th knob is only active if the 7th knob is.
    if data1 == 6:
      if data2 > 0:
        set_off_color(7, config['off_colors'][6])
      else:
        set_off_color(7, 0)

    # the secret reset code!
    if data1 == 11 and data2 == 127:
      print("secret code found")
      reset_all_values()


  # rezzie.thru([status, data1, data2])
    # cc = hardware.get_target_encoder(data1)
    # if cc >= 0:
    #   rezzie.thru([179, cc, data2])


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


def set_off_color(encoder, color):
  midithru.send_message([constants.FIGHTER_ENCODER_SWITCHES, encoder, color])

def set_animation(encoder, animation):
  midithru.send_message([constants.FIGHTER_ENCODER_ANIMATIONS, encoder, animation])


def reset_all_values():
  for x in range(0, 16):
    rezzie.thru([179, x, config['default_values'][x]])
    midithru.send_message([176, x, config['default_values'][x]])

  # gotta reset the knobs that depend on other knobs
  set_off_color(3, 0)
  set_off_color(7, 0)
  print("resetting all.", flush=True)
