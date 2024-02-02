"""
Gappi, Jeric Marcel L.
BSCpE - BE401A
Software Design
"""

from Circle import Circle
from Rectangle import Rectangle


class Application():
    def __init__(self,circle,rect):
        self.circle = circle         # circle object
        self.rect = rect             # rectangle object

    def create_circle(self):
        print(f"CIRCLE #1 ID: {self.circle}")
        circle2 = self.circle.clone()         
        circle2.set_color("Rose")
        print(f"CIRCLE #2 ID: {circle2}")
        
    def create_rect(self):
        print(f"RECTANGLE #1 ID: {self.rect}")
        rect2 = self.rect.clone()
        rect2.set_y(12)
        rect2.set_color("Dark Orange")
        print(f"RECTANGLE #2 ID: {rect2}")
  
        
if __name__ == "__main__":
    circ =  Circle(16,16,"Pink",16) 
    rect = Rectangle(0,0,"Living Coral",64,64)
    
    app = Application(circ,rect) # aggregation
    
    app.create_circle()
    print()
    app.create_rect()