# run from midi directory
# python testrunner.py
#
import unittest
from push.quadrant import Quadrant
class TestQuadrant(unittest.TestCase):

  def test_coords_to_quadrant(self):
    res = Quadrant.coords_to_quadrant((0,0), (3,3))
    self.assertTrue(36 in res)
    self.assertTrue(39 in res)
    self.assertTrue(40 not in res)

    self.assertTrue(60 in res)
    self.assertTrue(63 in res)
    self.assertTrue(64 not in res)

    res = Quadrant.coords_to_quadrant((0,0), (7,7))
    # lower left
    self.assertTrue(36 in res)
    self.assertTrue(43 in res)
    self.assertTrue(44 in res)

    # upper right
    self.assertTrue(99 in res)
    self.assertTrue(100 not in res)


if __name__ == '__main__':
  unittest.main()
