def make_skipper(n):
	"""
	>>> a = make_skipper(2)
	>>> a(5)
	1
	3
	5
	"""
	def skipper(x):
		for i in range(x+1):
			if i % n != 0:
				print(i)
	return skipper


def make_alternator(f, g):
	"""
	>>> a = make_alternator(lambda x: x * x, lambda x: x + 4)
	>>> a(5)
	1
	6
	9
	8
	25
	>>> b = make_alternator(lambda x: x * 2, lambda x: x + 2)
	>>> b(4)
	2
	4
	6
	6
	"""
	def alternator(x):
		for i in range(1, x+1):
			"""
			if i % 2 == 0:
				print(g(i))
			else:
				print(f(i))
			"""
			print(f(i)) if i % 2 == 1 else print(g(i))
	return alternator



def mario_number(level):
	if level == 1:
		return 1
	elif level % 10 == 0:
		return 0
	else:
		return mario_number(level // 10) + mario_number((level // 10) // 10)



def combine(n, f, result):
	if n == 0:
		return result
	else:
		return combine(n // 10, f, f(result, n % 10))