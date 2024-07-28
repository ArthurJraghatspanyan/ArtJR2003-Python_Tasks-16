#Write a recursive function to find the sum of the digits of a given number.

def summary(n):
	if n == 0:
		return 0
	else:
		return n % 10 + summary(n // 10)

result = summary(3498)
print(result)
