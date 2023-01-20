#assuming arithmetic progression class is already defined, how many calls to 'next' can we make before we reach an int > 2^63



#assuming all other code is right(im not gonna right out the entire class and its subclasses for one fucking function, look back at the book on page 90 if you wanna see how the base class and its subclasses work, its 1:20 am rn im not typing all that shiiiii out

#would include parent class in method declaration, but will throw error in this case cause it technically doesnt exist here
#def num_less_2to63(num):

#nvm dont even need method, just some code but it wont run, again cause all the other clases dont exist 
arithmetic_prog = ArithmeticProgression(128, 0)
C=0
while(num < 2**63):
    C+=1 
    num = arithmetic_prog.advance()
print(C)













