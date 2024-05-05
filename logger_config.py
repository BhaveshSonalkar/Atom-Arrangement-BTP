import logging


def setup_logger(log_file="log.txt"):
	# Create logger
	logger = logging.getLogger(__name__)
	logger.setLevel(logging.DEBUG)

	# Define formatter
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

	# Create console handler and set level to debug
	ch = logging.StreamHandler()
	ch.setLevel(logging.DEBUG)
	ch.setFormatter(formatter)

	# Create file handler and set level to debug
	fh = logging.FileHandler(log_file)
	fh.setLevel(logging.DEBUG)
	fh.setFormatter(formatter)

	# Add console handler to logger
	logger.addHandler(ch)
	logger.addHandler(fh)

	return logger


# Set up the logger
logger = setup_logger()
