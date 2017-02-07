

class PushEventListener:
  inputs = []
  def __init__(self):
    return

  def load_midiin(self, midiin):
    print "got my midiin object"
    midiin.set_callback(MidiInputHandler("porty"))
    self.inputs

  def input_handler(self, midistuff):
    print midistuff

  def router(self, event, data=None):
    print event
