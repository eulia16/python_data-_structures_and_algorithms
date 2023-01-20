#function to take sequence of numbers and determines if all the numbers are different from each other(distinct)

#returns true if the numbers are distinct, and false if they are not
def distinct_num(numbers):
    map = {}#define a dictionary
    for num in numbers:
        if(num not in map.keys()):
            map[num] = 1
        else:
            return False;
    return True;

print(distinct_num([1,2,3,4,5,6,7,45,67,32,23]))
print(distinct_num([1,2,3,4,6,6,7,45,67,32,23]))
       
            
