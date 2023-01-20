#I will take the generic class code from an outside source and implement whatever method the problem wants me to, just less time consuming than retyping every class out again ans again


class ReversedSequenceIterator():
    """An iterator for any of Python's sequence types."""
    '''this is literally the same as the previous iterator class except it uses the  thing i always forget to call the string(iterable) in reverse order''' 
    def __init__(self,sequence):
        self._sequence = sequence[::-1]
        self._k = -1#incrementer
    def __next__(self):
        self._k += 1
        if(self._k < len(self._sequence)):
            return(self._sequence[self._k])
        else:
           raise StopIteration()
    
    def __iter__(self):
        return self;


          
    




V = ReversedSequenceIterator([1,8,3,6,10,5,12])
print (V.__next__())
print (V.__next__())
print (V.__next__())
print (V.__next__())
print (V.__next__())



