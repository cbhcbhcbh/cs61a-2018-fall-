# example 1
def horse(mask):
	horse = mask
	def mask(horse):
		return horse
	return horse(mask)

mask = lambda horse: horse(2)

horse(mask)



# example 2
y = "y"
h = y
def y(y):
	h = "h"
	if y == h:
		return y + 'i'
	y = lambda y: y(h)
	return lambda h: y(h)
y = y(y)(y)


# example 3
def the(donald):
	return donald + 5

def clin(ton):
	def the(race):
		return donald + 6
	def ton(ga):
		donald = ga-1
		return the(4)-3
	return ton

donald, duck = 2, clin(the)
duck = duck(8)
"""
调用clin(the)发展到ton(ga)时，返回一个the(4)，这个the(4)是clin(ton)下的the(race)而不是the(donald)。
"""
