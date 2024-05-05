from datetime import datetime

from logger_config import logger
from src.path_finding import move_atom_from_start_to_end
from src.utils import get_optimal_matching, get_cost_matrix


def read_matrix(file_name):
	with open(file_name, 'r') as file:
		lines = file.readlines()
		matrix = [[int(val) for val in line.strip().split(',')] for line in lines]
	return matrix


def process_atom_rearrangement():
	start_time = datetime.now().microsecond
	input_matrix = read_matrix("inputs/input_matrix.txt")
	target_matrix = read_matrix("inputs/target_matrix.txt")

	matching_start_time = datetime.now().microsecond

	cost_matrix, misplaced_atoms, empty_sites = get_cost_matrix(input_matrix, target_matrix)
	misplaced_atom_index, empty_site_index = get_optimal_matching(cost_matrix)

	matching_end_time = datetime.now().microsecond
	logger.info(f"Time taken to find optimal matching: {matching_end_time - matching_start_time}")

	optimal_move_start_time = datetime.now().microsecond
	for i in range(len(misplaced_atom_index)):
		logger.info(f"Optimal Assignment:: Row {misplaced_atom_index[i]} -> Column {empty_site_index[i]}")
		start_coordinate = misplaced_atoms[misplaced_atom_index[i]]
		end_coordinate = empty_sites[empty_site_index[i]]
		path = []
		move_atom_from_start_to_end(start_coordinate, end_coordinate, input_matrix, path)
		logger.info(f"Path: {path}")

	optimal_move_end_time = datetime.now().microsecond
	logger.info(f"Time taken to make optimal moves: {optimal_move_end_time - optimal_move_start_time}")

	end_time = datetime.now().microsecond
	logger.info(f"Total Time taken by process_atom_rearrangement: {end_time - start_time}")
