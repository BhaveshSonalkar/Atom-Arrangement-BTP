import logging


def setup_logger(logger_name, log_file="log.txt"):
	# Create logger
	logger = logging.getLogger(str(logger_name))
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
