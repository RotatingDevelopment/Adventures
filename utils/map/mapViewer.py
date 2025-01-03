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

def Layout(mapObj) -> None:
    mapLayout = mapObj.map
    for y in mapLayout:
        print(f"{"\n"}{"-"*(mapObj.dimension[0]*2)}{"\n"}")
        output = ""
        for x in y:
            output+=f"|{x}"
        output+="|"
        print(output)


'''
coord: (X,Y) -> represents coordinates for viewpoint
range: ((VX0,VX1),(VY0,VY1)) -> vision range for each axis
'''

def Viewpoint(mapObj,coord:tuple,range:tuple) -> None:
    mapLayout = mapObj.map
    #print(mapLayout)
    range = ((range[0],range[0]),(range[1],range[1]))


    #print(f"{range}:{coord}")


    if coord[0] - range[0][0] < 0:
        range[0][0] -= abs(coord[0] - range[0][0])
    if coord[0] - range[0][1] < 0:
        range[0][1] -= abs(coord[0] - range[0][1])
    if coord[1] - range[1][0] < 0:
        range[1][0] -= abs(coord[1] - range[1][0])
    if coord[1] - range[1][1] < 0:
        range[1][1] -= abs(coord[1] - range[1][1])


    #print(f"{coord}:{range}")
    #print(f"{coord[1] - range[1][0]}:{coord[1] + range[1][1]}")
    #print(f"{mapLayout[coord[1] - range[1][0]: (coord[1] + range[1][1])+1]}")

    for j,y in enumerate(mapLayout[coord[1] - range[1][0]: (coord[1] + range[1][1])+1]):
        print(f"{"\n"}{"-"*(max(range[0][0],range[0][1])*2)}{"\n"}")
        output = ""
        for i,x in enumerate(y[coord[0] - range[0][0]: (coord[0] + range[0][1])+1]):
            if (i,j) == coord:
                output+=f"|P"
            else:
                output+=f"|{x}"
        output+="|"
        print(output)
    