def count_digits(n):
	"""
	>>> count_digits(42)
	2
	>>> count_digits(12345678)
	8
	>>> count_digits(1)
	1
	"""
	count = 0
	while n > 0:
		count += 1
		n = n // 10
	return count

def count_matches(n, m):
	"""
	>>>count_matches(10, 30)
	1
	>>>count_matches(12345, 23456)
	0
	>>>count_matches(212121, 321321)
	2
	>>>count_matches(101, 11) # only one's place matches
	1
	>>>count_matches(101, 10) # noplace matches
	0
	"""
	matches = 0
	while n > 0 and m > 0:
		if n % 10 == m % 10:
			matches += 1
		n, m = n // 10, m // 10
	return matches