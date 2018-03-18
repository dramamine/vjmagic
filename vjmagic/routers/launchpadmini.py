# # from push.listener import PushEventListener
# from vjmagic import constants
# import rtmidi
# from vjmagic.routers.base import Router
# from vjmagic.state import hardware
# from time import sleep
# # from vjmagic.state import hardware
# # from vjmagic.interface import encodercontroller, encoders, banks, graphics, outpututils

# rezzie = None
# trying to run this directly through Resolume instead.

# midiinput = None
# midithru = None

# # constructor
# def init():
#   global midiinput, midithru
#   # setup inputs
#   midiinput = rtmidi.MidiIn()
#   port = Router.find_port_index(midiinput, "launchpad mini")
#   midiinput.open_port(port)
#   midiinput.set_callback(handler)

#   vport = "python out"
#   midithru = rtmidi.MidiOut()
#   portid = Router.find_port_index(midithru, "launchpad mini")
#   if portid >= 0:
#       midithru.open_port(portid)
#       print("found out port.")
#   else:
#       midithru.open_virtual_port(vport)

#   initialize_lights()
#   # turn_on_light(3)

# def use(res):
#   global rezzie
#   rezzie = res

# def initialize_lights():
#   [turn_off_light(x) for x in range(0, 16)]


# def handler(event, data=None):
#   evt = event[0]
#   (status, data1, data2) = evt
#   print("launchpad mini", evt)

#   # if status == constants.MIDI_NOTE_ON3:
#   #   resolume.handle_button_press(data1)
#   if status == 176:
#     cc = hardware.get_target_encoder(data1)
#     if cc >= 0:
#       rezzie.thru([179, cc, data2])

