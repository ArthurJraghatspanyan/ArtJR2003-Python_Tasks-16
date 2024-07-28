# Write a recursive function to print numbers from 5 to 1.

def nums(n):
	if n > 0:
		print(n)
		nums(n - 1)

nums(5)
