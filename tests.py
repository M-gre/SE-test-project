import unittest
import gameoflife as gol

class GOLTestCase(unittest.TestCase):
	def test_init_surface_size(self):
		try:	#travis fails because the docker container has no video device to display the surface
			surface = gol.init_surface(100, 200, 3)
			self.assertEqual(100 * 3, surface.get_width())
			self.assertEqual(200 * 3, surface.get_height())
		except gol.pygame.error:
			pass

	def test_init_surface_type(self):
		try:  # travis fails because the docker container has no video device to display the surface
			with self.assertRaises(TypeError):
				gol.init_surface("a", "b", None)
		except gol.pygame.error:
			pass
	def test_init_gameboard_size(self):
		gameboard = gol.init_gameboard(100, 200)
		self.assertEqual((200, 100), gameboard.shape)


if __name__ == '__main__':
	unittest.main()
