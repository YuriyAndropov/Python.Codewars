#Description:
#Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)
#https://www.codewars.com/kata/52685f7382004e774f0001f7

def make_readable(seconds):
    h= seconds // 3600
    m= seconds // 60 - (h*60)
    s= seconds - (m*60)
    hs="0"+str(h)+":"
    ms="0"+str(m)+":"
    ss="0"+str(s)
    return hs[-3:]+ ms[-3:]+ ss[-2:]
