#Description:
#Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:
#a = Vector([1,2,3])
#b = Vector([3,4,5])
#c = Vector([5,6,7,8])
#a.add(b) # should return Vector([4,6,8])
#a.subtract(b) # should return Vector([-2,-2,-2])
#a.dot(b) # should return 1*3+2*4+3*5 = 26
#a.norm() # should return sqrt(1^2+2^2+3^2)=sqrt(14)
#a.add(c) # raises an exception
#If you try to add, subtract, or dot two vectors with different lengths, you must throw an error!
#Also provide:
#a toString function, so that using the vectors from above, a.toString() === '(1,2,3)' (in Python, this is a __str__ method, so that str(a) == '(1,2,3)')
#an equals function, so that two vectors who have the same components are equal
#The test cases will utilize the user-provided equals method.
#https://www.codewars.com/kata/526dad7f8c0eb5c4640000a4

import math

class Vector:
    def __init__(self, a):
        self.a = a
    
    def add(self, b):
        try:
            return Vector(map(lambda x,y : x+y,self.a,b.a))
        except:
            return "oops!"
    
    def subtract(self, b):
        try:
            return Vector(map(lambda x,y : x-y,self.a,b.a))
        except:
            return "oops!"
    
    def dot(self, b):
        try:
            return sum(map(lambda x,y : x*y,self.a,b.a))
        except:
            return "oops!"
    
    def toString(self):
        return str(tuple(self.a)) 
        
    def norm(self):
        return math.sqrt(sum([2*x for x in self.a]))
        
    def equals(self, vector_instance):
        return True if self.a == vector_instance.a else False
        
    def __str__(self):
        return str(tuple(self.a)).replace(" ","")
