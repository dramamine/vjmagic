

class PushEventListener:
  inputs = []
  listeners = []
  ableton_out = None
  def __init__(self):
    return

  # def load_midiin(self, midiin):
  #   print "got my midiin object"
  #   midiin.set_callback(MidiInputHandler("porty"))
  #   self.inputs

  def load_output(self, ableton_out):
    self.ableton_out = ableton_out

  def input_handler(self, midistuff):
    print midistuff

  def add_listener(self, event, cb, eat=True):
    self.listeners.append([event, cb, eat])

  def router(self, event, data=None):
    (status, data1, data2) = event[0]
    # TODO helpful for debugging
    print event

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
      self.ableton_out.thru(event[0])
