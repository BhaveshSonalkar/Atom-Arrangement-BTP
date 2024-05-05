from logger_config import logger

def make_moves(path, grid):
	pass

def move_atom_from_start_to_end(start_coordinate, end_coordinate, grid, path):
	try:
		direction = None
		current_x = start_coordinate[0]
		current_y = start_coordinate[1]

		if current_x < end_coordinate[0]:
			direction = [1, 0]
		elif current_x > end_coordinate[0]:
			direction = [-1, 0]
		elif current_y < end_coordinate[1]:
			direction = [0, 1]
		elif current_y > end_coordinate[1]:
			direction = [0, -1]
		else:
			return

		next_x = current_x + direction[0]
		next_y = current_y + direction[1]

		if grid[next_x][next_y] == 0:
			grid[next_x][next_y] = 1
			grid[current_x][current_y] = 0
			path.append([[current_x, current_y], [next_x, next_y]])
			move_atom_from_start_to_end([next_x, next_y], end_coordinate, grid, path)
		else:
			move_atom_from_start_to_end([next_x, next_y], end_coordinate, grid, path)
			path.append([[current_x, current_y], [next_x, next_y]])
			grid[next_x][next_y] = 1
			grid[current_x][current_y] = 0
	except Exception as e:
		logger.error(f"Failed to move atom from start to end: {e}")
		return None