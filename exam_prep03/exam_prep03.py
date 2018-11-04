def complete(t, d, k):
	"""Return whether t is d-k-complete.

	>>> complete(Tree(1), 0, 5)
	True
	>>> u = Tree(1, [Tree(1), Tree(1), Tree(1)])
	>>> [ complete(u, 1, 3) , complete(u, 1, 2) , complete(u, 2, 3)]
	[True, False, False]
	>>> complete(Tree(1, [u, u, u]), 2, 3)
	True
	"""
	if not t.branches:
		return d == 0
	bs = [complete(branch, d-1, k) for branch in t.branches]
	return len(t.branches) == k and all(bs)

def closest(t):
	"""Return the smallest difference between an entry and the sum of the 
	entries of its branches.
	>>> t = Tree(8, [Tree(4), Tree(3)])
	>>> closest(t)  # |8 - (4 + 3)| = 1
	1
	>>> closest(Tree(5, [t]))  # Same minimum as t
	1
	>>> closest(Tree(10, [Tree(2), t]))  # |10 - (2 + 8)| = 0
	0
	>>> closest(Tree(3)) # |3 - 0| = 3
	3
	>>> closest(Tree(8, [Tree(3, [Tree(1, [Tree(5)])])]))  # |3 - 1| = 2
	2
	>>> sum([])
	0
	"""
	diff = abs(t.entry - sum([b.entry for b in t.branches]))
	return min([diff] + [closest(b) for b in t.branches])

def is_path(t, path):
	"""Return whether a given path exists in a tree, begining 
		at the root.

	>>> t = tree(1, [
			tree(2, [tree(4), tree(5)]),
			tree(3, [tree(6), tree(7)])
		])
	>>> is_path(t, [1, 2])
	True
	>>> is_path(t, [1, 2, 4])
	True
	>>> is_path(t, [2, 4])
	False
	"""
	if label(t) != path[0]:
		return False
	if len(path) == 1:
		return True
	return any([is_path(b, path[1:]) for b in branches(t)])