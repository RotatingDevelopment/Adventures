from random import randint
from math import ceil

import mapViewer
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


def addition(mapLayout1:list[list], mapLayout2:list[list]) -> list[list]:

    rank = sorted([mapLayout1,mapLayout2],key=lambda layout:len(layout),reverse=True)
    k,j = len(rank[0]),len(rank[1])
    res = []
    for y in range(k):
        res.append([])
        if y < j:
            res[y] = rank[0][y] + rank[1][y]
        elif k == j:
            break
        else:
           res[y] = rank[0][y] + [0 for _ in rank[1][0]]
    return res





if __name__=="__main__":
    dimension = (int(input("provide x")),int(input("provide y")))
    bias = float(input("provide bias"))
    layout = generator(dimension,bias)
    mapViewer.Layout(layout,dimension)
            
