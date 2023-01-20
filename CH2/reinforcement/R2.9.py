#implement __sub__ method in the vector class-R2.9
#implement __neg__ method in vector class-R2.10
#implement __mul__ method in vector class-R2.12
#implement __dot_product__ method in vector class-R2.12
#modify the constructor of the Vectot class to allow for iterable types to be inserted in the construction of a Vector object and allow its values to be automatically initialized about those passed numbers R2.15
class Vector():
    """Represent a Vector in Multi-Dimensional Space"""
    #original constructor

#    def __init__(self,d):
#        """Initializes a d-dimensional vector"""
#        self._coords = [0]*d

    #updated constructor for R2.15
    def __init__(self, d):
        if(isinstance(d, int)):
            self._coords = [0]*d
        elif(isinstance(d, (list, tuple))):
            __vec = Vector(len(d))
            for i in range(len(d)):
                __vec[i] = d[i]
            self._coords = __vec 
            
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
    def __eq__(self,other):
        """Returns the boolean value if equal/not equal"""
        return (self._coords==other._coords)
    
    def __ne__(self,other):
        """Return True if Vector differs from Other"""
        return not self==other
    
    def __str__(self):
        """Returns the string Representation"""
        return ('<' + str(self._coords)[1:-1] + '>')

    def __sub__(self, vector_to_sub):
        if(len(vector_to_sub) != len(self)):
            raise ValueError("Dimensins must match!")
        temp = Vector(len(self))
        for i in range(len(self)):
            temp[i] = self._coords[i] - vector_to_sub[i]
        return temp;
    
    def __neg__(self):
        for i in range(len(self)):
            self._coords[i] *= -1
        return self;

    def __mul__(self, num):
        for i in range(len(self)):
            self._coords[i] *= num
        return self;

    def dot_product(self, num):
        scalar_product=0
        for i in range(len(self)):
            scalar_product += self._coords[i] * num[i]
        return scalar_product;

u = Vector(5)
anotherOne = Vector([1,2,3,4])
u.__setitem__(3,41)
u.__setitem__(2,31)
u.__setitem__(4,10)
print (u.__str__())
print (u.__sub__([7,1,23,2,1]))
print(u.__neg__())
print(u.__mul__(3))

s = [4,1,7,2,8]
print(s)
print(u.__str__())
print(anotherOne.__str__())
print (u.dot_product(s)) 
