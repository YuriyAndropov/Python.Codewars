#Description:
#Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built with the sides of given length and false in any other case.
#(In this case, all triangles must have surface greater than 0 to be accepted).
#https://www.codewars.com/kata/56606694ec01347ce800001b

def is_triangle(a, b, c):
    a = abs(a)
    b = abs(b)
    c = abs(c)
    s = (a + b - c) * (a + c - b) * (c + b - a)
    if s > 0:
        return True
    else:
        return False
