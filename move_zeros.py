#Description:
#Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
#https://www.codewars.com/kata/52597aa56021e91c93000cb0

def move_zeros(array):
    z = []
    n = []
    for i in array:
        if isinstance(i, str) is False:
            t = ""+str(i)
            if t == "0" or t =="0.0" or t =="": 
                z.append(i)
            else:
                n.append(i)
        else:
            n.append(i)
    return n + z
