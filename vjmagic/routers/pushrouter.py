# from push.listener import PushEventListener
from vjmagic import constants
import rtmidi
from vjmagic.routers.base import Router
from vjmagic.interface import outpututils, encoders, graphics, encodercontroller

class PushRouter(Router):
  encoder_controller = None

  # TODO probably want singletons for this
  def __init__(self, encoder_controller=None):
    Router.__init__(self, "push input")
    self.encoder_controller = encoder_controller
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
    print self.name, evt

    if status == constants.STATUS_CH1:
      encoders.handle_push_turns(evt)
      if data1 == constants.GRAPHICS_KNOB:
        graphics.handle_push_turns(evt)
      return
    elif status == constants.MIDI_NOTE_ON:
      # TODO consider moving this function to resolume side
      graphics.handle_note_in(evt)
      encodercontroller.check_for_category_change(evt)
      if data1 <= 10:
        encoders.handle_push_touches(evt)
        return
    elif status == constants.PRESS_USER_BUTTON:
      graphics.handle_user_button_presses(evt)






    outpututils.thru(event[0])

  # note ons are either:
  # - pressing colored buttons. route these through to Resolume
  # - touching knobs. send these to our encoders model
  def handle_note_ons(self, event, data=None):
    (status, data1, data2) = event
