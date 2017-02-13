# run from midi directory
# python -m unittest discover project_directory "*Spec.py"

import unittest
from push.graphics import graphics
class TestGraphics(unittest.TestCase):
	def test_coords_to_quadrant(self):
		g = new Graphics()
		res = g.coords_to_quadrant((0,0), (8,8))
		self.assertTrue(res)

if __name__ == '__main__':
    unittest.main()
