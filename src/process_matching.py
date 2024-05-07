from datetime import datetime

from src.animation import initialize_atoms_for_animation
from src.path_finding import find_moves_for_the_given_assignment
from src.utils import get_optimal_matching, get_cost_matrix
from logger_config import setup_logger
logger = setup_logger(__name__)


def read_matrix(file_name):
	with open(file_name, 'r') as file:
		lines = file.readlines()
		matrix = [[int(val) for val in line.strip().split(',')] for line in lines]
	return matrix


def get_input_matrix():
	input_matrix = read_matrix("inputs/input_matrix.txt")
	target_matrix = read_matrix("inputs/target_matrix.txt")
	return input_matrix, target_matrix


def process_atom_rearrangement(animation_window, input_matrix, target_matrix):
	#Initialize the animation window
	atom_array = initialize_atoms_for_animation(input_matrix)

	#Perform the optimal matching
	matching_start_time = datetime.now().microsecond
	cost_matrix, misplaced_atoms, empty_sites = get_cost_matrix(input_matrix, target_matrix)
	misplaced_atom_index, empty_site_index = get_optimal_matching(cost_matrix)
	matching_end_time = datetime.now().microsecond
	logger.info(f"Time taken to find optimal matching: {matching_end_time - matching_start_time}")

	#Find Path and move the atoms
	for i in range(len(misplaced_atom_index)):
		start_coordinate = misplaced_atoms[misplaced_atom_index[i]]
		end_coordinate = empty_sites[empty_site_index[i]]
		logger.info(f"Optimal Assignment:: Index {i} :: {start_coordinate} -> {end_coordinate}")
		path = []
		find_moves_for_the_given_assignment(start_coordinate, end_coordinate, input_matrix, path, animation_window, atom_array)
		logger.info(f"Path: {path}")
