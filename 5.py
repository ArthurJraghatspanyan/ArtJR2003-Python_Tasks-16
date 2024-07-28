# Write a recursive function to print all elements of a list.

def all_elements(ls):
	if not ls:
		return
	print(ls[0])
	print(ls[1:])

ls = [1, 2, 3, 4, 5]
print(ls)
