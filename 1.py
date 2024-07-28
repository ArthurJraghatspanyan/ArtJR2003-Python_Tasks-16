# Write a recursive function to print numbers from 1 to 5.

def nums(n):
	if n > 0:
		nums(n - 1)
		print(n)

nums(5)
