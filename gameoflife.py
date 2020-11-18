import numpy as np
import pygame

colour_about_to_die = (200, 200, 225)
colour_alive = (255, 255, 215)
colour_background = (10, 10, 40)
colour_grid = (30, 30, 60)


def init_surface(dim_x: int, dim_y: int, cell_size: int) -> pygame.surface:
	pygame.init()
	pygame.display.set_caption("John Conway's Game of Life")
	return pygame.display.set_mode((dim_x * cell_size, dim_y * cell_size))


def init_gameboard(dim_x: int, dim_y: int, pattern: np.ndarray = None) -> np.ndarray:
	gameboard = np.zeros((dim_y, dim_x))
	if pattern is not None:
		if pattern.shape[0] > gameboard.shape[0] or pattern.shape[1] > gameboard.shape[1]:
			raise IndexError
		gameboard[0: pattern.shape[0], 0:pattern.shape[1]] = pattern
	return gameboard


def update(current_gameboard: np.ndarray, cell_size: int = None, surface: pygame.surface = None) -> np.ndarray:
	next_gameboard = np.zeros((current_gameboard.shape[0], current_gameboard.shape[1]))
	surface_available = True if surface is not None else False

	for r, c in np.ndindex(current_gameboard.shape):
		# Count Number of Neighbours that are alive for every cell
		num_alive = np.sum(current_gameboard[r - 1:r + 2, c - 1:c + 2]) - current_gameboard[r, c]

		if current_gameboard[r, c] == 1 and num_alive < 2 or num_alive > 3:
			col = colour_about_to_die
		elif (current_gameboard[r, c] == 1 and 2 <= num_alive <= 3) or (
				current_gameboard[r, c] == 0 and num_alive == 3):
			next_gameboard[r, c] = 1
			col = colour_alive

		if surface_available:  # if surface is available draw cells
			col = col if current_gameboard[r, c] == 1 else colour_background
			pygame.draw.rect(surface, col, (c * cell_size, r * cell_size, cell_size - 1, cell_size - 1))
	return next_gameboard


if __name__ == '__main__':
	# TODO: arguments for size
	# TODO: specific patterns as arguments
	# TODO: random gameboard

	dim_x = 50
	dim_y = 50
	cell_size = 10

	surface = init_surface(dim_x, dim_x, cell_size)
	pattern = np.array([[0, 1, 0, 1, 0, 1, 0],
						[1, 0, 1, 0, 1, 0, 1],
						[0, 1, 0, 1, 0, 1, 0],
						[1, 0, 1, 0, 1, 0, 1],
						[0, 1, 0, 1, 0, 1, 0]
						])
	gameboard = init_gameboard(dim_x, dim_y, pattern)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		surface.fill(colour_grid)
		gameboard = update(gameboard, cell_size, surface)
		pygame.display.update()
