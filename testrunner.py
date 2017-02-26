import unittest
from test.graphicsSpec import TestGraphics
from test.quadrantSpec import TestQuadrant

runner = unittest.TextTestRunner()
runner.run(unittest.makeSuite(TestGraphics,'test'))
runner.run(unittest.makeSuite(TestQuadrant,'test'))

