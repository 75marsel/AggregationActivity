from Prototype import IProtoType
from Shape import Shape
import copy         
           
class Circle(IProtoType,Shape):
    
    def __init__(self,x,y,color,radius):
        super().__init__(color)
        self.set_x(x)
        self.set_y(y)
        self.set_color(color)
        self.__radius = radius
    
    def __str__(self): # circle function
        return f"{id(self)}\tX: {self.get_x()} Y: {self.get_y()}\tColor: {self.get_color()}\tRadius: {self.__radius}"
    
    def clone(self): # can also be copy.deepcopy(self) or return(self)(self.get_color(),..)
        return copy.copy(self)