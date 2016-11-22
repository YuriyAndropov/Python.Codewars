#Description:
#Given a number, return a string with dash'-'marks before and after each odd integer, but do not begin or end the string with a dash mark.
#https://www.codewars.com/kata/dashatize-it/python

import re # kata error. I solved this task without regular expressions, but they still need to be imported 
def dashatize(num):
    res =""
    try:
        num=abs(num)
    except:
        return str(num)
    for i in str(num):
        if len(res) >0:
            if int(i)%2!=0 and res[-1]!="-":
                res+="-"+i+"-"
            elif int(i)%2!=0 and res[-1]=="-":
                res+=i+"-"    
            else:
                res+=i
        else:
            if int(i)%2!=0:
                res+=i+"-"
            else:
                res+=i
    if res[0] =="-":
        res=res[1:]
    elif res[-1] =="-":
        res=res[:-1]
    return res
