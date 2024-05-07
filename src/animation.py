import pygame
import sys
from logger_config import setup_logger
logger = setup_logger(__name__)

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ATOM_COLOR = (255, 0, 0)  # Red

#define cell width and height
CELL_WIDTH = 50
CELL_HEIGHT = 50

class Atom:
	def __init__(self, row, col):
		self.row = row
		self.col = col
		self.x = col * CELL_WIDTH + CELL_WIDTH // 2
		self.y = row * CELL_HEIGHT + CELL_HEIGHT // 2
		self.is_moving = False
		self.radius = 10

	def draw(self, window):
		pygame.draw.circle(window, ATOM_COLOR, (int(self.x), int(self.y)), self.radius)


def move_atom_animation(window, atom_array, source_coordinate, target_coordinate):
	try:
		no_of_steps = 100
		atom_to_move = None
		for _ in range(no_of_steps):
			window.fill(BLACK)
			for atom in atom_array:
				if atom.row == source_coordinate[0] and atom.col == source_coordinate[1]:
					atom_to_move = atom
					atom.x += (target_coordinate[1] - source_coordinate[1]) * CELL_WIDTH / no_of_steps
					atom.y += (target_coordinate[0] - source_coordinate[0]) * CELL_HEIGHT / no_of_steps
				atom.draw(window)
			pygame.display.update()
			pygame.time.delay(1)
		atom_to_move.row = target_coordinate[0]
		atom_to_move.col = target_coordinate[1]
	except Exception as e:
		logger.error(f"Failed to move atom animation: {e}")
		return None

def initialize_atoms_for_animation(input_matrix):
	try:
		atom_array = []
		for row in range(len(input_matrix)):
			for col in range(len(input_matrix[0])):
				if input_matrix[row][col] == 1:
					atom = Atom(row, col)
					atom_array.append(atom)
		return atom_array
	except Exception as e:
		logger.error(f"Failed to initialize atoms for animation: {e}")
		return None


def initialize_pygame(grid_size_row, grid_size_col):
	try:
		pygame.init()
		window = pygame.display.set_mode((grid_size_row * CELL_HEIGHT, grid_size_col * CELL_WIDTH))
		pygame.display.set_caption("Atom Animation")
		window.fill(BLACK)
		return window
	except Exception as e:
		logger.error(f"Failed to initialize pygame: {e}")
		return None


def wait_for_pygame_to_end():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()