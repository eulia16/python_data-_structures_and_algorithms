#fucntion that takes a positive integer n, and returns the sum of the squares of all the odd integers smaller than n

def sum_square_odd(n):
    odd_sum = 0
    for i in range(0, n):
        if((i & 1) == True):
            print(i)
            odd_sum += i**2
    print(odd_sum)
    return odd_sum;



print(sum_square_odd(20))
print(sum_square_odd(7))
