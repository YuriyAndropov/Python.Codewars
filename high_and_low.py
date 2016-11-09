#Description:
#In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
#https://www.codewars.com/kata/554b4ac871d6813a03000035

def high_and_low(numbers):
    list = numbers.split()
    list = map(int, list)
    return str(max(list)) +" "+ str(min(list))
