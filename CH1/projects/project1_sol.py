import itertools
chars = ['c','a','d','t','o','g']
chars = ''.join(chars)
strgs = itertools.permutations(chars,6)
print(list(strgs))
