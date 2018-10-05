# If statements and Boolean Operators
def wears_jacket(temp, raining):
	"""
	>>> wears_jacket(90, False)
	False
	>>> wears_jacket(40, False)
	True
	>>> wears_jacket(100, True)
	True
	"""
	if temp < 60 or raining:
		return True
	else:
		return False

def wears_jacket(temp, raining):
	return temp < 60 or raining


# While loops
def is_prime(n):
	"""
	>>> is_prime(10)
	False
	>>> is_prime(7)
	True
	"""
	k, a = 1, 0
	while n >= k:
		if n % k == 0:
			a += 1
			if a > 2:
				return False
		k += 1
	return True

# Alternative answer
def is_prime(n):
	if n == 1:
		return False
	k = 2
	while k < n:
		if n % k == 0:
			return False
		k += 1
	return True

