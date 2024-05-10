import os
import random


def generate_matrix(number_of_rows, number_of_columns):
	matrix = [[random.randint(0, 1) for _ in range(number_of_columns)] for _ in range(number_of_rows)]
	return matrix


def write_matrix(matrix, file_name):
	with open(file_name, 'w') as file:
		for row in matrix:
			file.write(",".join(map(str, row)) + "\n")


def generate_and_write_matrices(rows, cols):
	# Create the 'inputs' directory if it doesn't exist
	input_dir = 'inputs'
	if not os.path.exists(input_dir):
		os.makedirs(input_dir)

	# Generate input matrix
	input_matrix = generate_matrix(rows, cols)

	target_matrix = generate_matrix(rows, cols)

	# Write input matrix to file
	write_matrix(input_matrix, os.path.join(input_dir, 'input_matrix.txt'))
	write_matrix(target_matrix, os.path.join(input_dir, 'target_matrix.txt'))

	print("Matrices written to files: input_matrix.txt, target_matrix.txt")


# Example usage:
generate_and_write_matrices(20, 20)
