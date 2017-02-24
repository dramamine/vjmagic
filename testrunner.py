import unittest
from test.graphicsSpec import TestGraphics

runner = unittest.TextTestRunner()
runner.run(unittest.makeSuite(TestGraphics,'test'))

