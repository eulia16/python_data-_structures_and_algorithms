#fucntion that takes an int n, and returns the sum of all the squares of all numvers less than n

def sumSquared(n):
	sum = 0
	for i in range(0, n): #can use n as range in exclusive with stop
		sum += i**2
	return sum;

print(sumSquared(3))
print(sumSquared(10))
print(sumSquared(27))	
