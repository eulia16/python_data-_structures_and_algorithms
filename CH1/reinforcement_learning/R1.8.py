#function that takes string s w length n, and uses negative numbers for indexing

def string_thing(s):
    length = len(s)
    k = -5
    print(s[k] == s[length + k])
    k= -6
    print(s[k] == s[length + k])
    k = -length
    print(s[k] == s[length + k])
#not really sure what the question is even asking, but i guess the solution os you can find the index of the list for any value -len(s)<=k<0 if you add the len(s) to k and use that as an index
string_thing("Hello brah, how're you")
     
