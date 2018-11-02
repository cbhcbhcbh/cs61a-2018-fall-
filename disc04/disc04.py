def tree(label, branches=[]):
	for branch in branches:
		assert is_tree(branch)
	return [label] + list(branches)

def label(tree):
	return tree[0]

def branches(tree):
	return tree[1:]

def is_leaf(tree):
	return not branches(tree)

def tree_max(t):
	"""Return the maximum label in a tree.

	>>> t = tree(4, [tree(2, [tree(1)]), tree(10)])
	>>> tree_max(t)
	10
	"""
	return max([label(t)] + [tree_max(branches(t))])

def height(t):
	"""

	>>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
	>>> height(t)
	2
	"""
	if is_leaf(t):
		return 0
	return 1 + max([height(branch) for branch in branches(t)])

def square_tree(t):
	"""Return a tree with the squareof every element in t"""
	sq_branches = [square_tree(branch) for branch in branches(t)]
	return tree(label(t)**2, sq_branches)

def find_path(tree, x):
	"""
	>>> t = tree(2, [tree(3), tree(6, [tree(5), tree(11)])])
	>>> find_path(t, 5)
	[2, 7, 6, 5]
	>>> find_path(t, 10)   # returns None
	"""
	if label(tree) == x:
		return [label(tree)]
	for branch in branches(tree):
		path = find_path(branch, x)
		if path:
			return [label(tree)] + path

def prune(t, k):
	if k == 0:
		return tree(label(t), [])
	else:
		return tree(label(t), [prune(branch, k-1) for branch in branches(t)])

def hailstone_tree(n, h):
	"""Generates a tree of hailstone numbers that will
	   reach N, with height H.
	>>> hailstone_tree(1, 0)
	[1]
	>>> hailstone_tree(1, 4)
	[1, [2, [4, [8, [16]]]]]
	>>> hailstone_tree(8, 3)
	[8, [16, [32, [64]], [5, [10]]]]
	"""
	if h == 0:
		return tree(n)
	branches = [hailstone_tree(n * 2, h - 1)]
	if (n - 1) % 3 == 0 and ((n - 1) // 3) % 2 == 1 and (n - 1) // 3 > 1:
		branches += [hailstone_tree((n - 1) // 3, h - 1)]
	return tree(n, branches)