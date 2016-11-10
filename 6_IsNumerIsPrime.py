#Description:
#Is Prime
#Define a function isPrime that takes one integer argument and returns true or false depending on if the integer is a prime.
#Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.
#https://www.codewars.com/kata/5262119038c0985a5b00029f

def is_prime(num):
    x = abs(num)
    if x > 1:
        n = x // 2
        for i in range(2, n + 1):
            if x % i == 0:
                return False
        return True
    else:
        return False
