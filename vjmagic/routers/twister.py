# from push.listener import PushEventListener
from vjmagic import constants
import rtmidi
from vjmagic.routers.base import Router
from time import sleep
# from vjmagic.state import hardware
# from vjmagic.interface import encodercontroller, encoders, banks, graphics, outpututils

# Route messages from the Push (i.e. humans touching things)
class Twister(Router):
  # encoder_controller = None

  # constructor
  def __init__(self):
    Router.__init__(self, "Twister")
    # setup inputs
    midiinput = rtmidi.MidiIn()
    port = self.find_port_index(midiinput, "twister")
    midiinput.open_port(port)
    midiinput.set_callback(self.handler)
    self.midiinput = midiinput

    vport = "python out"
    midithru = rtmidi.MidiOut()
    portid = self.find_port_index(midithru, "twister")
    if portid >= 0:
        midithru.open_port(portid)
        print("found out port.")
    else:
        midithru.open_virtual_port(vport)
    self.midithru = midithru

    self.initialize_lights()
    self.turn_on_light(3)

  def initialize_lights(self):
    [self.turn_off_light(x) for x in range(0, 16)]




  # this handler's probably in every router
  def handler(self, event, data=None):
    evt = event[0]
    (status, data1, data2) = evt
    print(self.name, evt)

    # if status == constants.MIDI_NOTE_ON3:
    #   resolume.handle_button_press(data1)


  def turn_on_lights(self, layer, lights):
    print("got turn_on_lights call.", layer, lights)


  def turn_on_light(self, encoder):
    print("turning a light on")
    # sets rgbs to ON
    self.midithru.send_message([constants.FIGHTER_ENCODER_SWITCHES, encoder, 127])    
    # turn on encoder rings, value 0... @TODO we prob have initial value from rezzie
    self.midithru.send_message([constants.FIGHTER_ENCODERS, encoder, 0])    
    # turn up encoder brightness (65-94)
    self.midithru.send_message([constants.FIGHTER_ENCODER_ANIMATIONS, encoder, 94])

    # self.midithru.send_message([constants.MIDI_NOTE_ON, encoder, color])
    # self.midithru.send_message([constants.FIGHTER_ENCODER_SWITCHES, 0, 64])
    # self.midithru.send_message([constants.FIGHTER_ENCODER_SWITCHES, 1, 64])

    # # setting brightness
    # self.midithru.send_message([constants.FIGHTER_ENCODER_ANIMATIONS, 0, 17])
    # self.midithru.send_message([constants.FIGHTER_ENCODER_ANIMATIONS, 1, 27])

    # # setting indicator brightness
    # self.midithru.send_message([constants.FIGHTER_ENCODER_ANIMATIONS, 0, 65])
    # self.midithru.send_message([constants.FIGHTER_ENCODER_ANIMATIONS, 1, 95])

  def turn_off_light(self, encoder):
    print("turning off ", encoder)
    # self.midithru.send_message([constants.FIGHTER_ENCODER_SWITCHES, encoder, 64]) 
    # self.midithru.send_message([constants.FIGHTER_ENCODER_SWITCHES, encoder, 65])
    # turns on encoder rings??
    # self.midithru.send_message([constants.FIGHTER_ENCODERS, encoder, 127])
    # sets rgb to blue
    # self.midithru.send_message([constants.FIGHTER_ENCODER_SWITCHES, encoder, 17])
    # sets rgbs to ON
    # self.midithru.send_message([constants.FIGHTER_ENCODER_SWITCHES, encoder, 127])

    # sets rgbs to OFF
    self.midithru.send_message([constants.FIGHTER_ENCODER_SWITCHES, encoder, 0])

    # turn off encoder rings
    self.midithru.send_message([constants.FIGHTER_ENCODERS, encoder, 0])

    # turn down encoder brightness (65-94)
    self.midithru.send_message([constants.FIGHTER_ENCODER_ANIMATIONS, encoder, 65])