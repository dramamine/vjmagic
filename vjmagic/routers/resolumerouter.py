# from push.listener import PushEventListener
from import constants
import rtmidi
from midi.routers.base import Router

class ResolumeListener(Router):
  encoders = None
  encoder_controller = None
  output = None

  # TODO probably want singletons for this
  def __init__(self, encoders=None, encoder_controller=None, output=None):
    Router.__init__(self, "resolume input")
    self.encoders = encoders
    self.encoder_controller = encoder_controller
    self.output = output

    resolume_in_name = "resolume out"
    resin = rtmidi.MidiIn()
    portid = find_port_index(resin, resolume_in_name)
    if portid >= 0:
        resin.open_port(portid)
    else:
        print "didnt find ", resin, "how will I get updates from resolume?"



    # need this or it gets...garbage-collected?!?
    self.midiinputs = midiinputs

    # setup listeners
    # self.listeners.append()

  # this handler's probably in every router
  def handler(self, event, data=None):
    print "Resolume handler called"
    (status, data1, data2) = event[0]
    # TODO helpful for debugging
    print self.name, event[0]

    eater = False
    for [lstatus, ldata1, ldata2], cb, eat in self.listeners:
      if (lstatus == None or lstatus == status) and \
        (ldata1 == None or ldata1 == data1) and \
        (ldata2 == None or ldata2 == data2):

        # safer to ignore errors here; don't want to interrupt eating behavior
        try:
          cb(event[0])
        except Exception as e:
          print e

        # if one listener says eat it, then do that.
        eater = eater or eat

    # fwd any messages (that we didn't eat) onwards to the Push
    if not eater:
      print self.name, "sending it forward."
      self.output.thru(event[0])
