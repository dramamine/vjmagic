# from push.listener import PushEventListener
from vjmagic import constants
import rtmidi
from vjmagic.routers.base import Router
# from vjmagic.interface import encodercontroller, encoders, outpututils

# Route messages to and from Resolume
class Resolume(Router):
  encoders = None
  encoder_controller = None
  output = None

  subscriptions = []

  # TODO probably want singletons for this
  def __init__(self, ):
    Router.__init__(self, "resolume input")

    resolume_in_name = "resolume out"
    resin = rtmidi.MidiIn()
    portid = Router.find_port_index(resin, resolume_in_name)
    if portid >= 0:
        resin.open_port(portid)
        resin.set_callback(self.handler)
    else:
        print("didnt find ", resin, "how will I get updates from resolume?")


    # need this or it gets...garbage-collected?!?
    self.resin = resin

    vport = "python out"
    midithru = rtmidi.MidiOut()
    portid = self.find_port_index(midithru, vport)
    if portid >= 0:
        midithru.open_port(portid)
        print("found out port for python.")
    else:
        midithru.open_virtual_port(vport)
    self.midithru = midithru

  # this handler's probably in every router
  def handler(self, event, data=None):
    evt = event[0]
    (status, data1, data2) = evt
    # print(self.name, evt)

    for [substatus, subcallback] in self.subscriptions:
      if substatus == status:
        print("found a sub!")
        subcallback(evt)

    # # eater = False
    # # used to be a 'whitelist' of routers here, ex. 177 and 178 were whitelisted
    # if status == constants.STATUS_CH2:
    #   encoders.handle_resolume_updates(evt)
    # elif status == constants.STATUS_CH1:
    #   if data1 in constants.ENCODERS:
    #     encoders.handle_push_turns(evt)
    # elif status == constants.MIDI_NOTE_ON:
    #   # Resolume was misreporting knobs being touched... I did not like
    #   # encoders.handle_push_touches(evt)
    #   encodercontroller.check_for_category_change(evt)
    #   return

  def subscribe(self, status, callback):
    self.subscriptions.append([status, callback])

    # let's just send everything else through for now
    # outpututils.thru(evt)
  def thru(self, event):
    print("fwding this:", event, flush=True)
    self.midithru.send_message(event)