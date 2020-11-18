import unittest
import gameoflife as gol


class GOLTestCase(unittest.TestCase):
	def test_init_surface_size(self):
		surface = gol.init_surface(100, 200, 3)
		self.assertEqual(surface.get_width(), 100*3)
		self.assertEqual(surface.get_height(), 200*3)

	def test_init_surface_type(self):
		with self.assertRaises(TypeError):
			gol.init_surface("a", "b", None)


if __name__ == '__main__':
	unittest.main()
