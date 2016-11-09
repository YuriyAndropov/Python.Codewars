#Description:
#At a job interview, you are challenged to write an algorithm to check if a given string, s, can be formed from two other strings, part1 and part2.
#The restriction is that the characters in part1 and part2 are in the same order as in s.
#The interviewer gives you the following example and tells you to figure out the rest from the given test cases.
#https://www.codewars.com/kata/54c9fcad28ec4c6e680011aa

def is_merge(s, part1, part2):
    order1 = True
    order2 = True
    index = 0
    if ''.join(sorted(s))==''.join(sorted(part1+part2)):
        for i in range(len(part1)):
            order1 = order1 and (s.find(part1[i],index,len(s))!=-1)
            if order1:
                index = s.find(part1[i],index,len(s))
        index = 0
        for i in range(len(part2)):
            order2 = order2 and (s.find(part2[i],index,len(s))!=-1)
            if order2:
                index = s.find(part2[i],index,len(s))
 
        return order1 and order2
    return False
