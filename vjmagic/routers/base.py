# Abstract class for routers
class Router:
  name = None
  listeners = []

  def __init__(self, name="Unnamed"):
    self.name = name
    return

  # this handler's probably in every router
  def handler(self, event, data=None):
    print("you should overwrite the handler for this:", self.name)

  @staticmethod
  def find_port_index(midi, str, skip=False):
    for idx, device in enumerate(midi.get_ports()):
      if str in device.lower():
        if skip:
          print("skipped one.")
          skip = False
        else:
          return idx
    return -1
