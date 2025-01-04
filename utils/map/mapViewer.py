'''
Functions:
Viewpoint: Vision of player depending on coordinates, range(n) -> map[y-n:y+n][x-n:x+n]
Layout: Neat layout of entire map structure for CLI based viewing

class Map:
    def __init__(self,attributes):
        self.name = attributes["name"]
        self.dimension = attributes["dimension"]
        self.bias = attributes["bias"]
        self.map = mapGenerator.generator(self.dimension,self.bias) -> 2 dimension array
'''

def Layout(mapLayout:list[list],dimension:tuple) -> None:
    for y in mapLayout:
        print(f"{"\n"}{"-"*(dimension[0]*2)}{"\n"}")
        output = ""
        for x in y:
            output+=f"|{x}"
        output+="|"
        print(output)


'''
coord: (X,Y) -> represents coordinates for viewpoint
range: ((VX0,VX1),(VY0,VY1)) -> vision range for each axis
'''

def Viewpoint(mapLayout,coord:tuple,range:tuple) -> None:
    range = ((range[0],range[0]),(range[1],range[1]))

    #Fixing view range in both dimensions, Depending on boundaries of map
    #If coord + range = outofbounds: lower range until its within bounds

    if coord[0] - range[0][0] < 0:
        range[0][0] -= abs(coord[0] - range[0][0])
    if coord[0] - range[0][1] < 0:
        range[0][1] -= abs(coord[0] - range[0][1])
    if coord[1] - range[1][0] < 0:
        range[1][0] -= abs(coord[1] - range[1][0])
    if coord[1] - range[1][1] < 0:
        range[1][1] -= abs(coord[1] - range[1][1])

    #With range within bounds, We can start string formatting for visual layout relative to coordinates

    for j,y in enumerate(mapLayout[coord[1] - range[1][0]: (coord[1] + range[1][1])+1]):
        print(f"{"\n"}{"-"*(((range[0][0]+range[0][1]+1)*2)+1)}{"\n"}")
        output = ""
        for i,x in enumerate(y[coord[0] - range[0][0]: (coord[0] + range[0][1])+1]):
            if (i,j) == (0+range[0][0],0+range[1][0]):
                output+=f"|P"
            else:
                output+=f"|{x}"
        output+="|"
        print(output)
    print(f"{"\n"}{"-"*(((range[0][0]+range[0][1]+1)*2)+1)}{"\n"}")
    