from time import time, time_ns


def time_ms() -> int:
	return round(time() * 1000)
