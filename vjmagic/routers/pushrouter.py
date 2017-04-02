# from push.listener import PushEventListener
from vjmagic import constants
import rtmidi
from vjmagic.routers.base import Router
from vjmagic.interface import encodercontroller, encoders, graphics, outpututils

# Route messages from the Push (i.e. humans touching things)
class PushRouter(Router):
  encoder_controller = None

  # constructor
  def __init__(self):
    Router.__init__(self, "push input")
    # setup inputs
    midiinputs = [rtmidi.MidiIn()]
    for idx, device in enumerate(midiinputs[0].get_ports()):
      if "ableton push" in device.lower():
        midiinputs[0].open_port(idx)
        midiinputs[0].set_callback(self.handler)

        midiinputs = [rtmidi.MidiIn()] + midiinputs

    # need this or it gets...garbage-collected?!?
    self.midiinputs = midiinputs


  # this handler's probably in every router
  def handler(self, event, data=None):
    evt = event[0]
    (status, data1, data2) = evt
    print(self.name, evt)

    if status == constants.STATUS_CH1:
      if data in encoders.ENCODERS:
          encoders.handle_push_turns(evt)
          return
      elif data1 == constants.GRAPHICS_KNOB:
        graphics.handle_push_turns(evt)
        return
      elif data1 in constants.LAYER_TOGGLE_BUTTONS:
        graphics.handle_user_button_presses(evt)
      # else, it's prob some other user button...
      # in that case, forward on to Res.
    elif status == constants.MIDI_NOTE_ON:
      # TODO consider moving this function to resolume side
      graphics.handle_note_in(evt)
      res = encodercontroller.check_for_category_change(evt)
      if data1 <= 10:
        encoders.handle_push_touches(evt)
    elif status == constants.PRESS_USER_BUTTON:
      graphics.handle_user_button_presses(evt)

    # forward everything onward by default
    outpututils.thru(event[0])
