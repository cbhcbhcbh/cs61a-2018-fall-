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