import random

def generate_matrix(rows, cols):
    matrix = [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]
    return matrix

def write_matrix(matrix, file_name):
    with open(file_name, 'w') as file:
        for row in matrix:
            file.write(",".join(map(str, row)) + "\n")

# Define the dimensions for the matrices
rows = cols = 50

# Generate input matrix
input_matrix = generate_matrix(rows, cols)

# Generate target matrix
target_matrix = generate_matrix(rows, cols)

# Write input matrix to file
write_matrix(input_matrix, 'inputs/input_matrix.txt')

# Write target matrix to file
write_matrix(target_matrix, 'inputs/target_matrix.txt')

print("Matrices written to files: input_matrix.txt and target_matrix.txt")