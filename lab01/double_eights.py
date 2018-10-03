def double_eights(n):
	"""Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
	a = 0
	while n != 0:
		b = n % 10
		if b == 8:
			a += 1
		n = n // 10
	if a == 2:
		return True
	else:
		return False

# alternative answer
def double_eights(n):
	prev_eight = False
    while n > 0:
        last_digit = n % 10
        if last_digit == 8 and prev_eight:
            return True
        elif last_digit == 8:
            prev_eight = True
        else:
            prev_eight = False
        n = n // 10
    return False