# from push.listener import PushEventListener
from vjmagic import constants
import rtmidi
from vjmagic.routers.base import Router
from vjmagic.state import resolume
# from vjmagic.interface import encodercontroller, encoders, banks, graphics, outpututils

# Route messages from the Push (i.e. humans touching things)
class Fighter64(Router):
  # encoder_controller = None

  # constructor
  def __init__(self):
    Router.__init__(self, "Midi Fighter 64")
    # setup inputs
    midiinput = rtmidi.MidiIn()
    port = self.find_port_index(midiinput, "midi fighter 64")
    midiinput.open_port(port)
    midiinput.set_callback(self.handler)
    # for idx, val in enumerate(midiinput.get_ports()):
    #   print("in port:", idx, val)

    # for idx, device in enumerate(midiinput.get_ports()):
    #   if "midi fighter 64" in device.lower():
    #     midiinput.open_port(idx)
    #     midiinput.set_callback(self.handler)

    #     # midiinputs = [rtmidi.MidiIn()] + midiinputs
    #     print("got my input")

    # need this or it gets...garbage-collected?!?
    self.midiinput = midiinput


  # this handler's probably in every router
  def handler(self, event, data=None):
    evt = event[0]
    (status, data1, data2) = evt
    print(self.name, evt)

    if status == constants.MIDI_NOTE_ON3:
      resolume.handle_button_press(data1)

    # if status == constants.STATUS_CH1:
    #   if data1 in constants.ENCODERS:
    #       encodercontroller.handle_push_turns(evt)
    #       encoders.handle_push_turns(evt)

    #       return
    #   elif data1 == constants.GRAPHICS_KNOB:
    #     graphics.handle_push_turns(evt)
    #     return
    #   elif data1 in constants.LAYER_TOGGLE_BUTTONS:
    #     graphics.handle_user_button_presses(evt)

    #   if data1 in constants.BANK_BUTTONS:
    #       banks.handle_presses(evt)
    #   elif data1 in constants.USER_BUTTONS_ROUTED_TO_CH3:
    #     outpututils.thru([constants.STATUS_CH3, data1, data2])
    #     return
    #   # else, it's prob some other user button...
    #   # in that case, forward on to Res.
    # elif status == constants.MIDI_NOTE_ON:
    #   # TODO consider moving this function to resolume side
    #   graphics.handle_note_in(evt)

    #   # print("yep checking for cagt change.", data1)
    #   encodercontroller.check_for_category_change(evt)
    #   encoders.save_active_clip(evt)

    #   if data1 <= 10:
    #     # these are definitely knob touches...
    #     # always eat these unless we're in 'touch' mode
    #     # if (encoders.get_display_mode() != "TOUCH"):
    #     #   print("not gonna route that.")
    #     #   return
    #     if encoders.handle_push_touches(evt):
    #       print("not gonna route that.")
    #       return
    #     # for some cases we want to route these differently...
    #     # if encoders.reroute_push_touches(evt):
    #     #   return
    # elif status == constants.PRESS_USER_BUTTON:
    #   graphics.handle_user_button_presses(evt)
    #   # mapping some user buttons to Ch 3, for fun

    # # forward everything onward by default
    # # print("getting routed.")
    # outpututils.thru(event[0])
