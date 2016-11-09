#Description:
#Count the number of Duplicates
#Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphanumeric characters, including digits, uppercase and lowercase alphabets.
#https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1

import collections
def duplicate_count(text):
    word = text.lower()
    c = 0
    cnt = collections.Counter(word)
    for i in cnt:
        if cnt[i] > 1:
            c += 1
    return c
