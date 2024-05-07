from src.animation import initialize_pygame, wait_for_pygame_to_end
from src.process_matching import process_atom_rearrangement

def main():
	animation_window = initialize_pygame()
	process_atom_rearrangement(animation_window)
	wait_for_pygame_to_end()


if __name__ == "__main__":
	main()
