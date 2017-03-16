

class Router:
  name = None
  listeners = []

  def __init__(self, name="Unnamed"):
    self.name = name
    return

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


  @staticmethod
  def find_port_index(midi, str):
    for idx, device in enumerate(midi.get_ports()):
      if str in device.lower():
        return idx
    return -1

