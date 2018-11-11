def add_this_many(x, el, lst):
	"""Add el to the end of lst the number of times x occurs 
	in lst.
	>>> lst = [1, 2, 4, 2, 1]
	>>> add_this_many(1, 5, lst)
	>>> lst
	[1, 2, 4, 2, 1, 5, 5]
	>>> add_this_many(2, 2, lst)
	>>> lst
	[1, 2, 4, 2, 1, 5, 5, 2, 2]
	"""
	count = 0
	for elem in lst:
		if elem == x:
			count += 1
	while count > 0:
		lst.append(el)
		count -= 1

def bathtub(n):
	"""
	>>> annihilator = bathtub(500) # the force awakens...
	>>> kylo_ren = annihilator(10)
	>>> kylo_ren()
	490 rubber duckies left
	>>> rey = annihilator(-20)
	>>> rey()
	510 rubber duckies left
	>>> kylo_ren()
	500 rubber duckies left
	"""
	def ducky_annihilator(rate):
		def ducky():
			nonlocal n
			# nonlocal n, rate
			n = n - rate
			print(str(n) + " rubber duckies left")
		return ducky
	return ducky_annihilator

def weird_gen(x):
	if x % 2 == 0:
		yield x * 2
	else:
		yield x
		yield from weird_gen(x - 1)

def gen_all_items(lst):
	"""
	>>> nums = [[1, 2], [3, 4], [[5, 6]]]
	>>> num_iters = [iter(l) for l in nums]
	>>> list(gen_all_items(num_iters))
	[1, 2, 3, 4, [5, 6]]
	"""
	for it in lst:
		yield from it