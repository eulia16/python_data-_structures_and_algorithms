#i accidentally deleted the class n shit i made so i stole this dudes code cause i didnt want it to seem like i skipped a question
class Vector():
    """Represent a Vector in Multi-Dimensional Space"""
    
    def __init__(self,d):
        """Initializes a d-dimensional vector"""
        self._coords = [0]*d
        
    def __len__(self):
        """Returns the dimension of the vector"""
        return (len(self._coords))
    
    def __getitem__(self,j):
        """Returns the jth co-ordinate of a vector"""
        return (self._coords[j])
    
    def __setitem__(self,j,val):
        """Assigns a value to jth location of a vector"""
        self._coords[j] = val
        
    def __add__(self,other):
        """Returns the sum of two vectors"""
        
        if (len(other)!=len(self)):
            raise ValueError("dimensions must match")
        result = Vector(len(self))
        for g in range(len(self)):
            result[g] = other[g] + self[g]
        return result
    
    def __mul__(self,entity):
        """
        Runtime check if entity is a vector or a scalar
        """
        product=0
        result_mul=[0]*len(self)
        if isinstance(entity,Vector):
            if (len(entity)!=len(self)):
                raise ValueError('The dimension must match')
            else:
                for g in range(len(self)):
                    product+=(self.__getitem__(g)*entity.__getitem__(g))
            return (product)
        
        elif(isinstance(entity,(int,float))):
            for h in range(len(self)):
                result_mul[h]=self[h]*entity
            return (result_mul)
    
    def __eq__(self,other):
        """Returns the boolean value if equal/not equal"""
        return (self._coords==other._coords)
    
    def __ne__(self,other):
        """Return True if Vector differs from Other"""
        return not self==other
    
    def __str__(self):
        """Returns the string Representation"""
        return ('<' + str(self._coords)[1:-1] + '>')
    
X = Vector(5)
X.__setitem__(0,34)
X.__setitem__(1,89)
X.__setitem__(4,21)
X.__setitem__(3,41)
print (X.__str__())
Y = Vector(5)
Y.__setitem__(2,19)
Y.__setitem__(1,32)
Y.__setitem__(3,38)
Y.__setitem__(4,10)
print (Y.__str__())

print (Y.__mul__(X))

print (X.__mul__(10))
print (Y.__mul__(10))


