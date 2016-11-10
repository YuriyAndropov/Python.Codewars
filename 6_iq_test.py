#Description:
#Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.
#! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)
#https://www.codewars.com/kata/552c028c030765286c00007d

def iq_test(numbers):
    list = numbers.split()
    list = map(int,list)
    even = []
    odd = []
    for i in list:
        if (i % 2) == 0:
            even.append(i)
        else:
            odd.append(i)
    if len(even) > len(odd):
        return list.index(odd[0]) + 1
    else:
        return list.index(even[0]) + 1
