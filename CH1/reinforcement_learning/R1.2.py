#returns true if k is even, false if not, not allowed to use *, /, //, or %
def is_even(k):
	return (not(k & 1));

print(is_even(20))
print(is_even(13))
	
