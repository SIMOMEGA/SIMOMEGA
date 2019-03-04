SUFFIXES = ["KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]

def approximate_size(size):
	if size < 0:
		raise ValueError("Number must be non-negative")

	multiple = 1024
	for suffix in SUFFIXES:
		size /= SUFFIXES[multiple]
		if size < multiple:
			return f"{size} {suffix}"
	raise ValueError("Number too large")