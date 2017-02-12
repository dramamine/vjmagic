

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

  def add_listener(self, event, cb):
      self.listeners.append([event, cb])

  def router(self, event, data=None):
    # TODO don't really need all these var names here
    (status, data1, data2) = event[0]
    # TODO this is nice!
    # print event
    for [lstatus, ldata1, ldata2], cb in self.listeners:
        if (lstatus == None or lstatus == status) and \
          (ldata1 == None or ldata1 == data1) and \
          (ldata2 == None or ldata2 == data2):
          cb(event[0]) # TODO hope we don't need anything beyond this!
