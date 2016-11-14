class Edge(object):
    
    def __init__(self, first_point, second_point):
        
        self.first_point = first_point
        self.second_point = second_point
        
        self.weight = (
            (self.first_point.get_x() - self.second_point.get_x())**2 +\
            (self.first_point.get_y() - self.second_point.get_y())**2)**0.5
        
    def get_second_point(self):
        
        return self.second_point
        
    def get_weight(self):
        
        return self.weight
    
    def __str__(self):
        
        return "From: " + self.first_point.__str__() + " To: " + self.second_point.__str__() + " Weight: " + str(self.weight)
