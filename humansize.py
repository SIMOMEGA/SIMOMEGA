SUFFIXES = ["KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]

def approximate_size(size):
	"""Convert a file size to human-readable form.
	Keyword arguments:
	size -- file size in bytes

	Returns: string
	"""

	if size < 0:
		raise ValueError("Number must be non-negative")

	multiple = 1024
	for suffix in SUFFIXES:
		size /= SUFFIXES[multiple]
		if size < multiple:
			return f"{size} {suffix}"

	raise ValueError("Number too large")