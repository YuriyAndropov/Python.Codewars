#Description:
#This time no story, no theory. The examples below show you how to write function accum:
#accum("abcd")    # "A-Bb-Ccc-Dddd"
#accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
#accum("cwAt")    # "C-Ww-Aaa-Tttt"
#https://www.codewars.com/kata/5667e8f4e3f572a8f2000039

def accum(s):
    c = 0
    result = ""
    l = len(s)
    for i in s:
        result += i.upper() + (i.lower()*c)
        c += 1
        if c < l:
            result += "-"
    return result   
