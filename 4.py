# Write a recursive function to find the sum of the first N natural numbers.

def sum(N):
	if N == 1:
		return 1
	else:
		return N + sum(N - 1)

x = sum(13)
print(x)
