import mapGenerator,mapViewer
'''
attributes: {
                name : string
                dimension : (int,int)
                bias : int <default = 1.0>
                                            }

Class contains the following:
-Map default attributes: name/dimension/bias [Initialization]
-generated map attributes : 2 dimension array [Initialization]

-viewpoint method to see map in given coordinates with specified vision
-arithmetic method on 2 maps to result in new map
-regeneration method to create new map

'''

class Map:
    def __init__(self,attributes):
        self.name = attributes["name"]
        self.dimension = attributes["dimension"]
        self.bias = attributes["bias"]
        if "layout" in attributes.keys():
            self.map = attributes["layout"]
        else:
            self.map = mapGenerator.generator(self.dimension,self.bias)
    
    def viewpoint(self,coord,range) -> None:
        mapViewer.Viewpoint(self,coord,range)
    
    def layout(self) -> None:
        mapViewer.Layout(self.map,self.dimension)

    def regen(self) -> None:
        self.map = mapGenerator.generator(self.dimension,self.bias)

    #Dunder Methods
    def __str__(self):
        return f"Name:{self.name}\nBias:{self.bias}\nDimensions:{self.dimension}\n"

    def __add__(self,other):
        layout = mapGenerator.addition(self.map,other.map)

        attributes = {
            "name":f"{self.name}+{other.name}",
            "dimension":(len(layout[0]),len(layout)),
            "bias":(self.bias+other.bias)/2,
            "layout":layout
        }

        newMap = Map(attributes)
        return newMap


    def __eq__(self,other):
        pass
    def __ne__(self,other):
        pass
    def __lt__(self,other):
        pass
    def __gt__(self,other):
        pass
    def __ge__(self,other):
        pass

if __name__=="__main__":
    attributes = {
        "name":"Testing",
        "dimension":(7,7),
        "bias":1
    }
    attributes2 = {
        "name":"Another",
        "dimension":(8,8),
        "bias":1
    }
    x = Map(attributes)



