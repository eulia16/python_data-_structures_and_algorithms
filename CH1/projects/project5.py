#this is the last project in Ch1 I will do, I wanna move on and I think I've done enough problems, this program takes in a list of words(a long string) seperated by whitespace and splits that strings and outputs how many times each string occurs in the list

list_o_strings = "hello i am the name of hello world yo this is this is is is is is oy yo mo how min noy yes no maybe"

splitted = list_o_strings.split()
#print(splitted)
my_dict = {}
for string in splitted:
    if string in my_dict:
        my_dict[string] = my_dict[string] + 1
    else:
        my_dict[string] = 1

print(my_dict) 

