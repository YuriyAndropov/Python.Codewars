#Description:
#Longest Palindrome
#Find the length of the longest substring in the given string s that is the same in reverse.
#As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.
#If the length of the input string is 0, return value must be 0.
#https://www.codewars.com/kata/54bb6f887e5a80180900046b

def longest_palindrome (s):
    s = s.lower()
    list = enumerate(s)
    word = ""
    temp = []
    if len(s) == 1:
        return 1
    elif len(s) == 0:
        return 0
    else:
        for item,value in list:
            c = 1
            for i in range(item):
                if i != item + 1:
                    word = s[i:item+1]
                    if word == word[::-1]:
                        temp.append(len(word))
    if len(temp) == 0:
        return 1
    else:
        return max(temp) 
