'''
Functions:
Viewpoint: Vision of player depending on coordinates, N = Vision range -> map[y-n:y+n][x-n:x+n]
Layout: Neat layout of entire map structure for CLI based viewing

class Map:
    def __init__(self,attributes):
        self.name = attributes["name"]
        self.dimension = attributes["dimension"]
        self.bias = attributes["bias"]
        self.map = mapGenerator.generator(self.dimension,self.bias) -> 2 dimension array
'''

def Layout(mapObj):
    mapLayout = mapObj.map
    for y in mapLayout:
        print(f"{"\n"}{"-"*(mapObj.dimension[0]*2)}{"\n"}")
        output = ""
        for x in y:
            output+=f"|{x}"
        output+="|"
        print(output)