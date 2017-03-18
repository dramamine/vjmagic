# run from midi directory
# python testrunner.py

import unittest
from push.encoders import Encoders
import push.constants
from push.encoder_controller import EncoderController

from push.output import AbletonPush

class TestEncoderController(unittest.TestCase):

  def test_default_case(self):
    mockEncoders = Encoders()
    self.assertTrue(mockEncoders.display_mode is 'BASIC')

    # should handle nothing changing from the default setting
    ec = EncoderController(mockEncoders)
    ec.check_for_encoder_change([push.constants.MIDI_NOTE_ON, 36, 1])
    self.assertTrue(mockEncoders.display_mode is 'BASIC')

    # should import a config
    mockConfig = [
      ['COOL', ['STR', 'MAG', 'INT', 'DEX', 'CON'], [72]]
    ]

    # gave up until I can learn how to mock
    # mockEncoders.display_mode = ''
    # mockEncoders.ableton_out = AbletonPush(None, None)
    # ec.load_config(mockConfig)
    # ec.check_for_encoder_change([push.constants.MIDI_NOTE_ON, 72, 1])
    # self.assertTrue(mockEncoders.display_mode is 'COOL')


if __name__ == '__main__':
  unittest.main()
