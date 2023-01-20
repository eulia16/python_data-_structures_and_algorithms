#program that inputs a polynomial in standard algebraic notation and outputs the first derivative of that polynomial
#we will import the polynomial as a string and use regex to split the polynomial into its seperate parts, then perform individual operations in the list it is appended to
import re 

class PolyDerivative():
    def __init__(self, degree, polynomial):
        """Constructor takes in the degree of the polynomial that will be derived"""
        self._degree = degree
        self.polynomial = polynomial
        self.derived_value = ''
        self._addToList()

    def _addToList(self):
        #print(self.polynomial)
        string = "hello+I+am+a+cool+persion"
        self.polynomial = re.sub(r"\s+","", self.polynomial)#removes whitespace from polynomial(if any)
        self.listOfInputs = re.split(r'\+|\-', self.polynomial)# splits polynomial into seperate functions
 
        #print(self.listOfInputs)
    def derive_poly(self):
        for i in self.listOfInputs:#for each value in the list, we must seperate the values, change them to ints, and pass them to the _derive method
                 
               
    
    def get_list(self):
        return self.listOfInputs;

       
    def _derive(self, degree, coefficient):
        if(degree == 1):
            return coefficient;#if the polynomial passed only has an exp of 1, return the coeff
        elif(degree == 0):
            return 0;#if only a number is passed, return 0
        else:#if there is actually an exponent(even negative), we can actually derive(you known what I mean)
            self.coefficient = coefficient * degree
            self.degree = degree - 1
            return self.coefficient, self.degree 
   
    def get_degree(self):#returns degree before derivation
        return self._degree;    
        



     
if __name__ == "__main__":#unit testing, if this is called as a lone program and not imported, these tests will be conducted
    polynomial = PolyDerivative(3, 'x^3 + 2x - 1')
    print(polynomial.get_degree()) 
    print(polynomial.get_list())             
