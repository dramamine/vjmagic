import unittest
from test.graphicsSpec import TestGraphics
from test.quadrantSpec import TestQuadrant
from test.encoder_controllerSpec import TestEncoderController

runner = unittest.TextTestRunner()
runner.run(unittest.makeSuite(TestGraphics,'test'))
runner.run(unittest.makeSuite(TestQuadrant,'test'))
runner.run(unittest.makeSuite(TestEncoderController,'test'))

