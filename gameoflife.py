import numpy as np
import pygame


def init_surface(dim_x: int, dim_y: int, cellsize: int) -> pygame.surface:
	pygame.init()
	pygame.display.set_caption("John Conway's Game of Life")
	return pygame.display.set_mode((dim_x * cellsize, dim_y * cellsize))


def init_gameboard(dim_x: int, dim_y: int) -> np.ndarray:
	gameboard = np.zeros((dim_y, dim_x))
	return gameboard


if __name__ == '__main__':
	pass
