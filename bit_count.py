#Description:
#Write a function that takes an (unsigned) integer as input, and returns the number of bits that are equal to one in the binary representation of that number.
#https://www.codewars.com/kata/526571aae218b8ee490006f4

def countBits(n):
    return bin(n).count("1")
