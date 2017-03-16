


import constants

class EncoderController:
  def __init__(self, encoder):
    self.encoder = encoder
    return
  def register_listeners(self, listener):
    listener.add_listener([constants.MIDI_NOTE_ON, None, None], self.check_for_encoder_change, True)

  def load_config(self, config):
    self.config = config
    print "loaded a config of length:", len(config)

  def check_for_encoder_change(self, event):
    (status, data1, data2) = event

    # we only want to look at the encoders we're tracking, ya know?
    # the 8x8 grid covers 36 to 99
    if data1 < 36 or data1 > 99:
      return

    for x in self.config:
      # print "my x is:", x

      (mode, label, keys) = x
      try:
        if keys.index(data1) >= 0:
          print "a grid button was pressed and was in this config:", data1, mode
          return self.encoder.set_display_mode(mode, label)
      except ValueError:
        pass

    return self.encoder.set_display_mode('BASIC',
      ['STR', 'MAG', 'INT', 'DEX', 'CON']
    )