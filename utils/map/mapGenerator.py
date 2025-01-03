from random import randint
from math import ceil
'''
dimensions: (X axis (N), Y axis (M))
            N x M 
            7 <= N == M <= 10^3

bias:   Int <default = 1.0>
        0 < bias <= 2.0

return: 2 dimensional array with each tile value
        49 <= size <= 10^6
        1 <= value <= 9
'''

def generator(dimension:tuple, bias:int) -> list[list[int]]:

    if (dimension[0] > 10**3 or dimension[0] < 7) or (dimension[1] > 10**3 or dimension[1] < 7):
        raise IndexError(f"{dimension} dimension out of bounds")
    if bias <= 0 or bias > 2:
        raise IndexError(f"{bias} bias out of bounds")
    

    mp = []
    for y in range(dimension[1]):
        mp.append([])
        for x in range(dimension[0]):
            z = randint(1,9)*bias
            if z > 9:
                mp[y].append(9)
            else:
                mp[y].append(ceil(z))
    return mp


if __name__=="__main__":
    dimension = (int(input("provide x")),int(input("provide y")))
    bias = float(input("provide bias"))
    print(generator(dimension,bias))

    #testcases:
    #print(generator((6,6),1))
    #print(generator(((10**3)+1,(10**3)+1),1))
    #print(generator((8,8),2))
    #print(generator((8,8),0.1))
            
