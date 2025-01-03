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
        self.map = mapGenerator.generator(self.dimension,self.bias)

    def __str__(self):
        return self.dimension
    
    def viewpoint(self,coord,range):
        mapViewer.Viewpoint(self,coord,range)
        return 0
    
    def layout(self):
        mapViewer.Layout(self)
        return 0



    #Dunder Methods

    def __add__(self,other):
        pass
    def __sub__(self,other):
        pass
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
        "dimension":(50,50),
        "bias":1
    }
    x = Map(attributes)
    x.layout()
    x.viewpoint((16,16),(3,3))


