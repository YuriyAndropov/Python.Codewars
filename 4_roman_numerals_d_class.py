#Create a RomanNumerals helper that can convert a roman numeral to and from an integer value. The class should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.
#Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.
#Examples:
#RomanNumerals.to_roman(1000) # should return 'M'
#RomanNumerals.from_roman('M') # should return 1000
#https://www.codewars.com/kata/roman-numerals-helper/python

class RomanNumerals:
    x = [1 ,4 ,5 ,9 ,10 ,40 ,50 ,90 ,100 ,400 ,500 ,900, 1000]
    y = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
    @classmethod
    def to_roman(self,n):
        out = ""
        for i in reversed(range(0,len(self.x))):
            if n // self.x[i] > 0:
                out+=str(self.y[i] * (n//self.x[i]))
                n = n - self.x[i]*(n//self.x[i])
        return out     
    @classmethod    
    def from_roman(self,r):
        res = 0
        last = 0
        for i in r[::-1]:
            if self.x[self.y.index(i)]>=last:
                res+=self.x[self.y.index(i)]
            else:
                res-=self.x[self.y.index(i)]
            last = self.x[self.y.index(i)]
        return res 
