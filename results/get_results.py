import csv

from generate_input import generate_and_write_matrices
from src.animation import initialize_pygame
from src.process_matching import get_input_matrix, process_atom_rearrangement
from logger_config import setup_logger
logger = setup_logger(__name__)

def run_algorithm_and_get_results(algorithm_name):
	try:
		# Open CSV file in append mode
		with open('steps_log.csv', mode='a', newline='') as file:
			writer = csv.writer(file)

			# Write header if the file is empty
			if file.tell() == 0:
				writer.writerow(['algorithm', 'grid size', 'steps', 'time taken for matching(in microseconds'])

			for i in range(1, 50):
				total_steps = 0
				time_time = 0
				for j in range(10):
					generate_and_write_matrices(i, i)
					input_matrix, target_matrix = get_input_matrix()
					animation_window = initialize_pygame(len(input_matrix), len(input_matrix[0]))
					no_of_steps, time_taken_for_matching = process_atom_rearrangement(animation_window, input_matrix, target_matrix)
					total_steps += no_of_steps
					time_time += time_taken_for_matching
				no_of_steps = total_steps / 10
				time_taken_for_matching = time_time / 10
				# Write iteration number and number of steps to CSV file
				writer.writerow([algorithm_name, i, no_of_steps, time_taken_for_matching])
	except Exception as e:
		logger.error(f"Error occurred while running the algorithm: {e}")