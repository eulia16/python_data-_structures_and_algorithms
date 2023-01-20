#this is the first project, we must write a program that outputs all possible strings formed by using the characters 'c','a', 't', 'd', 'o', and 'g' exactly once
from itertools import permutations

def list_all(data):
    print([s for s in permutations(data)])

list_all('catdog')
