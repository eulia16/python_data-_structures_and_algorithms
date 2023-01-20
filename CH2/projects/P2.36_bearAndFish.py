'''Write a Python program to simulate an ecosystem containing two types
of creatures, bears and fish. The ecosystem consists of a river, which is
modeled as a relatively large list. Each element of the list should be a
Bear object, a Fish object, or None. In each time step, based on a random
process, each animal either attempts to move into an adjacent list location
or stay where it is. If two animals of the same type are about to collide in
the same cell, then they stay where they are, but they create a new instance
of that type of animal, which is placed in a random empty (i.e., previously
None) location in the list. If a bear and a fish collide, however, then the
fish dies (i.e., it disappears).'''

class Creature(object):
    '''Create an abstract class for which the fish and bears can inherit from, we'll not use the ABCMeta class cause im lazy, but can use that for strict inheritance'''
    def __init__(self, index):
        self.index = index #index of creature in the river
        
    def move(self):
        '''Method to move left or right'''  



class Bear(Creature):
    '''A type of creature that inherits from the Creature class'''



class Fish(Creature):
    '''A type of creature that inherits from the Creature class'''



class River(object):
    '''The environment in which the creatures will reside, allows creatures to move 1 index to right or left each turn(randomly)'''
   
