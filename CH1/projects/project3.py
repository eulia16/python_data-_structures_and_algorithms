#this is a change simulator, the first line of input is the amount of the item, and the second line of input is the amt of money given, raise an exception if the amt given is less than the total price of the item in question
#**important, this py script only runs on python 3.6 and higher, as it uses f-strings**
import math

def determine_valid_input(price, payment):
    if price <= 0 or payment <=0:
        raise Exception("You must enter positive integers!")
    if price > payment:
        raise Exception("You must pay more money than the item is worth!")

def get_change(price, payment):
    return float(payment) - float(price);

def determine_bills(change):
    dollaBills = {'100': 0, '20': 0,'10': 0,'5': 0,'1': 0,'.25': 0, '.1': 0, '.05': 0, '.1': 0}
    if(change > 0):
        counter = 0
        while change >= 100:
            change = change - 100
            counter = counter + 1
            dollaBills['100'] = counter
        counter = 0
        while change >= 20:
            change = change - 20
            counter = counter + 1
            dollaBills['20'] = counter
        counter = 0
        while change >= 10:
            change = change - 10
            counter = counter + 1
            dollaBills['10'] = counter
        counter = 0
        while change >= 5:
            change = change - 5
            counter = counter + 1
            dollaBills['5'] = counter
        counter = 0
        while change >= 1:
            change = change - 1
            counter = counter + 1
            dollaBills['1'] = counter
        counter = 0
        while change >= .25:
            change = change - .25
            counter = counter + 1
            dollaBills['.25'] = counter
        counter = 0
        while change >= .1:
            change = change - .1
            counter = counter + 1
            dollaBills['.1'] = counter
        counter = 0
        while change >= .05:
            change = change - .05
            counter = counter + 1
            dollaBills['.05'] = counter
        counter = 0
        while change >= .01:
            change = change - .01
            counter = counter + 1
            dollaBills['.01'] = counter
    return dollaBills;









price = float(input())
payment = float(input())
determine_valid_input(price, payment)
change = get_change(price, payment)
change_seperated = determine_bills(change)
for i, j in change_seperated.items():
    if j != 0:
        message = f'Bill Type: {i}, Amount: {j}' 
        print(message)
