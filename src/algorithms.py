from scipy.optimize import linear_sum_assignment as hungarian_algorithm
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
