def new_line(st):
	if not st:
		return st
	return st[0] + "\n" + new_line(st[1:])

nl = new_line("hello world")
print(nl)
