# Ableton Push Basic MIDI Implementation.pdf
# https://app.box.com/s/w900ll2tq3tj83raes2a
#
SYSEX_START = [240, 71, 127, 21]
SYSEX_TERM = [247]

class AbletonPush:
  # midiin = None
  midiout = None
  midithru = None
  def __init__(self, Output, Thru):
    # assume these are open
    # self.midiin = Input
    self.midiout = Output
    self.midithru = Thru

  def clearDisplayLine(self, line):
    idx = 28 + line
    msg = SYSEX_START + [idx, 0, 0] + SYSEX_TERM
    self.midiout.send_message(msg)

  def set_display_line(self, line, str):
    self.set_display_bytes(line, self.get_bytes(str))

  def set_display_bytes(self, line, bytes):
    # pad to 68
    while len(bytes) < 68:
      bytes.append(30)
    msg = SYSEX_START + [(24 + line), 0, 69, 0] + bytes + SYSEX_TERM
    self.midiout.send_message(msg)

  def clearDisplay(self):
    # TODO map
    for i in range(0,3):
      self.clearDisplayLine(i)

  # true for user mode, false for live mode
  def set_user_mode(self, user=True):
    msg = SYSEX_START + [98, 0, 1, int(user)] + SYSEX_TERM
    self.midiout.send_message(msg)

  def get_bytes(self, str):
    bytes = []
    for c in str:
      bytes.append(int(c.encode('hex'), 16))
    return bytes

  def thru(self, event):
      self.midithru.send_message(event)
