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
  def find_port_index(midi, str):
    for idx, device in enumerate(midi.get_ports()):
      if str in device.lower():
        return idx
    return -1

