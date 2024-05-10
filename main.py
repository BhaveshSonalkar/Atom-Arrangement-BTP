from analysis_and_results.get_results import run_algorithm_and_get_results
from src.animation import initialize_pygame, wait_for_pygame_to_end
from src.process_matching import process_atom_rearrangement, get_input_matrix


def main():
	input_matrix, target_matrix = get_input_matrix()
	animation_window = initialize_pygame(len(input_matrix), len(input_matrix[0]))
	process_atom_rearrangement(animation_window, input_matrix, target_matrix)
	wait_for_pygame_to_end()


if __name__ == "__main__":
	main()
