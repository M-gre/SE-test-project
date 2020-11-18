import unittest



class GOLTestCase(unittest.TestCase):
	def test_init_surface_size(self):
		surface = gol.init_surface(100, 200, 3)
		self.assertEqual(100 * 3, surface.get_width())
		self.assertEqual(200 * 3, surface.get_height())

	def test_init_surface_type(self):
		with self.assertRaises(TypeError):
			gol.init_surface("a", "b", None)

	def test_init_gameboard_size(self):
		gameboard = gol.init_gameboard(100, 200)
		self.assertEqual((200, 100), gameboard.shape)


if __name__ == '__main__':
	unittest.main()
