def keep_ints(cond, n):
	"""Print out all integers 1..i..n where cond(i) is true

	>>> def is_evn(x):
	...		# Even numbers have remainder 0 when divided by 2.
	...		return x % 2 == 0
	>>> keep_ints(is_even, 5)
	2
	4
	"""
	i = 1
	while i <= n:
		if cond(i):
			print(i)
		i += 1

def keep_ints(n):
	"""Returns a function which takes one parameter cond and prints out 
	all integers 1..i..n where calling cond(i) returns True.

	>>> def is_evn(x):
	...		# Even numbers have remainder 0 when divided by 2.
	...		return x % 2 == 0
	>>> keep_ints(5)(is_even)
	2
	4
	"""
	def do_keep(cond):
		i = 1
		while i <= n:
			if cond(i):
				print(i)
			i += 1
	return do_keep

def multiply(m, n):
	"""
	>>> multiply(5, 3)
	15
	"""
	if n = 1:
		return m
	return multiply(m, n-1) + m

def countdown(n):
	"""
	>>> countdown(3)
	3
	2
	1
	"""
	if n <= 0:
		return Null
	print(n)
	countdown(n-1)

def 