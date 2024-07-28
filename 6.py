# Write a recursive function to find the length of a list.

def length_of_list(ls):
	if not ls:
		return 0
	else:
		return 1 + length_of_list(ls[1:])

x = length_of_list([1, 2, 3, 4, 5])
print(x)
