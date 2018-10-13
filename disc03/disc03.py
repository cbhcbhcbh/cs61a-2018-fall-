def is_prime(n):
	"""
	>>> is_prime(7)
	True
	>>> is_prime(10)
	False
	>>> is_prime(1)
	False
	"""
	def prime_helper(index):
		if index == n:
			return True
		elif n % index == 0 or n == 1:
			return False
		else:
			return prime_helper(index + 1)
	return prime_helper(2)


def make_func_repeater(f, x):
	"""
	>>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
	>>> incr_1(2) # same as f(f(x))
	3
	>>> incr_1(5)
	6
	"""
	def repeat(n):
		if n == 0:
			return x
		else:
			return f(repeat(n-1))
	return repeat


"""
I want to go up a flight of stairs that has n steps.
I can either take 1 or 2 steps each time.
"""
def count_stair_ways(n):
	if n == 1:
		return 1
	elif n == 2:
		return 2
	else:
		return count_stair_ways(n-1) + count_stair_ways(n-2)


"""
We are able to take up to and including k steps at atime.
"""
def count_k(n, k):
	"""
	>>> count_k(3, 3)   # 3, 2 + 1, 1 + 2, 1 + 1 + 1
	4
	>>> count_k(4, 4)
	8
	>>> count_k(10, 3)
	274
	>>> count_k(300, 1) # Only one step at a time
	"""
	if n == 0:
		return 1
	elif n < 0:
		return 0
	else:
		total = 0
		i = 1
		while i <= k:
			total += count_k(n - i, k)
			i += 1
		return total




"""
Here's a part of the Pascal's triangle:

Column: 0   1   2   3   4   ...
Row  0: 1   
Row  1: 1   1
Row  2: 1   2   1
Row  3: 1   3   3   1
Row  4: 1   4   6   4   1
...
"""
def pascal(row, column):
	if row == 0:
		return 0
	elif column == 0:
		return 1
	else:
		return pascal(row - 1, column) + pascal(row - 1, column - 1)