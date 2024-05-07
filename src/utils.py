from .algorithms import hungarian_matching
from datetime import datetime
from logger_config import setup_logger
logger = setup_logger(__name__)


def manhattan_distance(point1, point2):
	return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def get_cost_matrix(input_matrix, target_matrix):
	try:
		misplaced_atoms = []
		empty_sites = []
		for i in range(len(input_matrix)):
			for j in range(len(input_matrix[0])):
				if input_matrix[i][j] == 1 and target_matrix[i][j] == 0:
					misplaced_atoms.append([i, j])
				if input_matrix[i][j] == 0 and target_matrix[i][j] == 1:
					empty_sites.append([i, j])
		
		cost_matrix = []
		for misplaced_atom in misplaced_atoms:
			row = []
			for empty_site in empty_sites:
				row.append(manhattan_distance(misplaced_atom, empty_site))
			cost_matrix.append(row)

		logger.info(f"Cost matrix successfully created: {cost_matrix}")
		return cost_matrix, misplaced_atoms, empty_sites
	except Exception as e:
		logger.warning(f"Failed to create cost matrix: {e}")
		return None

def get_optimal_matching(cost_matrix):
	try:
		# Run the Hungarian Algorithm
		row_index, column_index = hungarian_matching(cost_matrix)
		logger.info(f"Optimal matching successfully found")
		return row_index, column_index
	except Exception as e:
		logger.warning(f"Failed to solve matching problem: {e}")
		return None
