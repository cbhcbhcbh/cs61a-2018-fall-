def f(it):
	it.append(it[1]())

def b(it):
	def steps():
		nonlocal it
		it = fit[0]
		return fit.pop()

fit = [1, [2]]
bit = [fit, b(fit[1])]
f(bit)


def adder(x, y):
	"""Adds y into x for lists of digits x and y representing positive numbers.

	>>> a = [3, 4, 5]
	>>> adder(a, [5, 5]) # 345 + 55 = 400
	[4, 0, 0]
	>>> adder(a, [8, 3, 4]) # 400 + 834 = 1234
	[1, 2, 3, 4]
	>>> adder(a, [3, 3, 3, 3, 3]) # 1234 + 33333 = 34567
	[3, 4, 5, 6, 7]
	"""
	carry, i = 0, len(x)-1
	for d in reversed([0] + y):
		if i == -1:
			x.insert(0, 0)
			i = 0
		d = carry + x[i] + d
		carry, x[i], i = d // 10, d % 10, i-1
	if x[0] == 0:
		x.remove(0)
	return x


def bits(nums):
	"""A set of nums represented as a function that takes 'entry', 0, or 1.

	>>> t = bits([4, 5]) # Contains 4 and 5, but not 2
	>>> t(0)(0)(1)('entry') # 4 = 0 * pow(2, 0) + 0 * pow(2, 1) + 1 * pow(2, 2)
	True
	>>> t(0)(1)('entry') # 2 = 0 * pow(2, 0) + 1 * pow(2, 1)
	False
	>>> t(1)(0)(1)('entry') # 5 = 1 * pow(2, 0) + 0 * pow(2, 1) + 1 * pow(2, 2)
	True
	"""
	def branch(last):
		if last == 'entry':
			return 0 in nums
		return bits([k // 2 for k in nums if k % 2 == last])
	return branch

def int_set(contents):
	"""Return a function that represents a set of non-negative integers.

	>>> (int_set([1, 2])(1), int_set([1, 2])(3)) # 1 in [1, 2] but 3 is not
	(True, False)
	>>> s = int_set([1, 3, 4, 7, 9])
	>>> [s(k) for k in range(10)]
	[False, True, False, True, True, False, False, True, False, True]
	"""
	index = bits(contents)
	def contains(n):
		t = index
		while n:
			last, n = n % 2, n // 2
			t = t(last)
		return t('entry')
	return contains


def naturals():
	i = 1
	while True:
		yield i
		i += 1

def filter(iterable, fn):
	"""
	>>> is_even = lambda x: x % 2 == 0
	>>> list(filter(range(5), is_even))
	[0, 2, 4]

	>>> all_odd = (2 * y - 1 for y in range(5)) # Generator object
	>>> list(filter(range(5), is_even))
	[]

	>>> s = filter(naturals(), is_even)
	>>> next(s)
	2
	>>> next(s)
	4
	"""
	for elem in iterable:
		if fn(elem):
			yield elem


def ensure_consistency(fn):
	"""Returns a function that calls fn on its argument, return fn's 
	return value, and returns None if fn's return value is different 
	from any of its previous return values for those same argument. 
	Also returns None if more than 20 calls are made.

	>>> def consistent(x):
	>>> 	return x
	>>> lst = [1, 2, 3]
	>>> def inconsistent(x):
	>>> 	return x + lst.pop()
	>>> 
	>>> a = ensure_consistency(consistent)
	>>> a(5)
	5
	>>> a(5)
	5
	>>> a(6)
	6
	>>> a(6)
	6
	>>> b = ensure_consistency(inconsistent)
	>>> b(5)
	8
	>>> b(5)
	None
	>>> b(6)
	7
	"""
	n = 0
	z = {}
	def helper(x):
		nonlocal n
		n += 1
		if n > 20:
			return None
		val = fn(x)
		if x not in z:
			z[x] = [val]
		if z[x] == [val]:
			return val
		else:
			z[x] = None
			return None
	return helper