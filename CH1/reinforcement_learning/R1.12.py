#implement own version of choice(data) fucntion using python's built in 
#randrange function
import random 

def my_choice(data):
   #random_number = random.randrandom(1, data)
    return random.randrange(1, data)

print(my_choice(5))
print(my_choice(100))
