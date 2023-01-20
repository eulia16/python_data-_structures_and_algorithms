#function that takes sequence of integers and determines if there is a distinct pair of numbers in the sequence that are odd

def odd_product(data):
    for i in data:
        for k in data:
            if i != k:
                if(((i*k) & 1) == True):
                    return i, k; 
                #return True;
    return -1;#False;

print(odd_product([1,2,3,4,5,6]))
print(odd_product([2,4,6,8])) 
print(odd_product([2,4,6,7,8,9])) 

