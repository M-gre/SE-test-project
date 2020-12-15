import unittest
import gameoflife as gol


class GOLTestCase(unittest.TestCase):
	def test_init_surface_size(self):
		try:  # travis fails because the build worker has no video device to display the surface
			surface = gol.init_surface(100, 200, 3)
			self.assertEqual(100 * 3, surface.get_width())
			self.assertEqual(200 * 3, surface.get_height())
		except gol.pygame.error:
			pass

	def test_init_surface_type(self):
		try:  # travis fails because the build worker has no video device to display the surface
			with self.assertRaises(TypeError):
				gol.init_surface("a", "b", None)
		except gol.pygame.error:
			pass

	def test_init_gameboard_size(self):
		gameboard = gol.init_gameboard(100, 200)
		self.assertEqual((200, 100), gameboard.shape)

	def test_init_gameboard_fails(self):
		pattern = gol.np.array([[0, 1, 0],
								[1, 0, 1],
								[0, 1, 0]
								])
		with self.assertRaises(IndexError):
			gol.init_gameboard(2, 5, pattern)

	def test_init_gameboard_pattern(self):
		pattern = gol.np.array([[0, 1, 0],
								[1, 0, 1],
								[0, 1, 0]
								])
		gameboard = gol.init_gameboard(3, 3, pattern)
		self.assertTrue((pattern == gameboard).all())

	def test_update_size(self):
		pattern = gol.np.array([[0, 1, 0],
								[1, 0, 1],
								[0, 1, 0]
								])
		next_pattern = gol.np.array([[0, 0, 0],
									 [0, 0, 1],
									 [0, 1, 0]
									 ])
		gameboard = gol.init_gameboard(3, 3, pattern)
		updated_gameboard = gol.update(gameboard)
		self.assertTrue((next_pattern == updated_gameboard).all())

	def test_set_random_pattern(self):
		col = 5
		row = 10
		result = gol.set_random_pattern(col, row)
		self.assertEqual(col, result.shape[0])
		self.assertEqual(row, result.shape[1])


if __name__ == '__main__':
	unittest.main()
