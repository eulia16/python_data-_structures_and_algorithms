#program to take an int greater than 2 and return the number of times necessary to divide the number by 2 until it is < 2
import copy

def num_div_2(data):
    counter=0
    info = copy.deepcopy(data)
    while info >= 2:#while the number is still greater than or equal to 2, continue loop
        info = info/2
        counter += 1

    return counter;

print(num_div_2(4))
print(num_div_2(18))
print(num_div_2(207))

