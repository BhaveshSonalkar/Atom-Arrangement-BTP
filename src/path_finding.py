from src.animation import move_atom_animation
from logger_config import setup_logger
logger = setup_logger(__name__)

def make_moves(path, grid):
	pass

def find_moves_for_the_given_assignment(start_coordinate, end_coordinate, grid, path, animation_window, atom_array):
	try:
		direction = None
		current_row = start_coordinate[0]
		current_col = start_coordinate[1]

		if current_row < end_coordinate[0]:
			direction = [1, 0]
		elif current_row > end_coordinate[0]:
			direction = [-1, 0]
		elif current_col < end_coordinate[1]:
			direction = [0, 1]
		elif current_col > end_coordinate[1]:
			direction = [0, -1]
		else:
			return

		next_row = current_row + direction[0]
		next_col = current_col + direction[1]

		if grid[next_row][next_col] == 0:
			grid[next_row][next_col] = 1
			grid[current_row][current_col] = 0
			path.append([[current_row, current_col], [next_row, next_col]])
			move_atom_animation(animation_window, atom_array, [current_row, current_col], [next_row, next_col])
			find_moves_for_the_given_assignment([next_row, next_col], end_coordinate, grid, path, animation_window, atom_array)
			return
		else:
			find_moves_for_the_given_assignment([next_row, next_col], end_coordinate, grid, path, animation_window, atom_array)
			path.append([[current_row, current_col], [next_row, next_col]])
			grid[next_row][next_col] = 1
			grid[current_row][current_col] = 0
			move_atom_animation(animation_window, atom_array, [current_row, current_col], [next_row, next_col])
			return
	except Exception as e:
		logger.error(f"Failed to move atom from start to end: {e}")
		return None