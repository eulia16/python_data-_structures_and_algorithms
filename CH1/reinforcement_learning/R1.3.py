#function to return minimum and max of a tuple passed into it, can't use min and max built in python methods

def minmax(data):
	#data is a tuple being passed
	#can definitly optimize this but for rn im tired and will just do it a lazy way
	min = data[0]#assuming the tuple isn't empty
	for num in data:
		if(num < min):
			min = num
	max = data[0]
	for num in data:
		if(num > max):
			max = num

	return min, max;
data  = (1,2,3,4,5,6,7,4,2,3,4,6)
anotherData = (21,44,6432,67,2,244241,12,4)
print(minmax(data))
print(minmax(anotherData))
print(minmax((12,24,53,7888,345,212,45,1)))	
