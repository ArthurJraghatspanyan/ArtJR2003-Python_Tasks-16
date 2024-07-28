def reverse_str(st):
	if len(st) <= 1:
		return st
	return reverse_str(st[1:]) + st[0]

x = reverse_str("em esrever")
print(x)
