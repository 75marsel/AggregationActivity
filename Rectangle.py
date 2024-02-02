from Prototype import IProtoType
from Shape import Shape
import copy       
           
class Rectangle(IProtoType,Shape):
    
    def __init__(self,x,y,color,width,height):
        super().__init__(color)
        self.set_x(x)
        self.set_y(y)
        self.set_color(color)
        self.__width = width
        self.__height = height
    
    def __str__(self): # Rectangle() function
        return f"""{id(self)}\tX: {self.get_x()} Y: {self.get_y()}\tColor: {self.get_color()}\tWidth = {self.__width}\tHeight: {self.__height}"""
    
    def clone(self): # can also be copy.deepcopy(self) or return(self)(self.get_color(),..)
        return copy.copy(self)