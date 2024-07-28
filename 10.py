# Write a recursive function to check if a given string is a palindrome.

def palindrome(st):
	if not st:
		return True
	if st[:] != st[-1::-1]:
		return False
	return palindrome(st[-1:0:-1])

pd = palindrome("radar")
print(pd)
