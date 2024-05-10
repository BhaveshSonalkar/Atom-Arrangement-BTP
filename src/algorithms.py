from scipy.optimize import linear_sum_assignment as hungarian_algorithm
import random
from logger_config import setup_logger
logger = setup_logger(__name__)

def hungarian_matching(cost_matrix):
	try:
		# Run the Hungarian Algorithm
		row_index, column_index = hungarian_algorithm(cost_matrix)
		return row_index, column_index
	except Exception as e:
		logger.error(f"Hungarian Matching:: Failed to solve matching problem: {e}")
		return None


def greedy_global_minimum_weight_selection(cost_matrix):
	# sort the cost matrix in ascending order wrt weight then select the corresponding indices
	row_index = []
	column_index = []
	weight_index = []
	for i in range(len(cost_matrix)):
		for j in range(len(cost_matrix[i])):
			weight_index.append((cost_matrix[i][j], i, j))
	weight_index.sort()
	visited_rows = set()
	visited_columns = set()
	for weight, i, j in weight_index:
		if i not in visited_rows and j not in visited_columns:
			row_index.append(i)
			column_index.append(j)
			visited_rows.add(i)
			visited_columns.add(j)

	return row_index, column_index
