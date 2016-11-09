#Description:
#Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.
#The binary number returned should be a string.
#https://www.codewars.com/kata/551f37452ff852b7bd000139

def add_binary(a,b):
    r = str(bin(a+b))
    return r[2:]
