#Description:
#Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized.
#https://www.codewars.com/kata/517abf86da9663f1d2000003

import re
def to_camel_case(text):
    word = ""
    print text
    g = re.split("\W+|_",text)
    if len(text) <= 1:
        return text
    else:
        for i in range(0,len(g)):
            if i ==0:
                word +=g[i]
            else:
                word +=g[i].capitalize()
        return word        
