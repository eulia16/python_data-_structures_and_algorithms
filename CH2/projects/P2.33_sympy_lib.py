#this is a much simpler implementation using the sympy library to obtain the derivative of a polynomial entered by the user
import sympy as der
import math
class PolyDerivative():
    
    def __init__(self, function):
        self.x = der.Symbol('x')
        self.function = function#self.x**5#function
        self.derivative = self.function.diff(self.x)
        print(self.derivative)
    #def derivative(self):
     #   return (self.function.diff(x));

if __name__ == "__main__":
    x = der.Symbol('x')
    poly = PolyDerivative(x**4)



