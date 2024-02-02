class Shape():
    def __init__(self,color):
        self.__x = 0
        self.__y = 0
        self.__color = color
    
    def set_x(self,new_x):
        self.__x = new_x
        
    def get_x(self):
        return self.__x
    
    def set_y(self,new_y):
        self.__y = new_y
        
    def get_y(self):
        return self.__y
    
    def set_color(self,new_color):
        self.__color = new_color
        
    def get_color(self):
        return self.__color