class Vertex(object):
    
    def __init__(self, x, y):
        
        self.x = x
        self.y = y
        self.is_reached = False
        
    def get_reached(self):
        
        return self.is_reached
    
    def set_reached(self):
        
        self.is_reached = True
        
    def get_x(self):
        
        return self.x
    
    def get_y(self):
        
        return self.y
    
    def __str__(self):
        return "( " + str(self.x) + ", " + str(self.y) + " )"