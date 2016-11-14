#Description:
#You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:
#next_bigger(12)==21
#next_bigger(513)==531
#next_bigger(2017)==2071
#If no bigger number can be composed using those digits, return -1:
#next_bigger(9)==-1
#next_bigger(111)==-1
#next_bigger(531)==-1
#https://www.codewars.com/kata/next-bigger-number-with-the-same-digits/python

import itertools
def next_bigger(n):
    s = list(str(n))
    for i in range(len(s)-2,-1,-1):
        if s[i] < s[i+1]:
            t = s[i:]
            m = min(filter(lambda x: x>t[0], t))
            t.remove(m)
            t.sort()
            s[i:] = [m] + t
            return int("".join(s))
    return -1
