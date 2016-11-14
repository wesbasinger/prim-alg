from decimal import Decimal
from edge import Edge

class Graph(object):
    
    def __init__(self, vertex_list):
        
        # initialized with every vertex, as graph is constructed, this list is emptied
        self.vertex_list = vertex_list
        
        # array of edges
        self.min_span_tree = []
        
    def check_all_reached(self):
        
        for vertex in self.vertex_list:
            if not vertex.get_reached():
                return False
        return True
        
        
    
    def get_reached_and_unreached_nodes(self):
        
        reached = []
        unreached = []
        
        for node in self.vertex_list:
            
            if node.get_reached():
                
                reached.append(node)
                
            else:
                
                unreached.append(node)
        
        return (reached, unreached)
    
    
        
    def make_tree(self):
      
        self.vertex_list[0].set_reached()
                        
        while not self.check_all_reached():
                        
            reached_and_unreached = self.get_reached_and_unreached_nodes()
            
            reached = reached_and_unreached[0]
            unreached = reached_and_unreached[1]
                        
            possible_edges = []
            
            for reached_node in reached:
                
                for unreached_node in unreached:
                    
                    possible_edges.append(Edge(reached_node, unreached_node))
            
            winning_weight = Decimal("Infinity")
            winning_edge = None
            
            for edge in possible_edges:
                                
                if edge.get_weight() < winning_weight:
                    
                    winning_weight = edge.get_weight()
                    winning_edge = edge
                    
            
            new_reached_point = winning_edge.get_second_point()
            new_reached_point.set_reached()
            
            self.min_span_tree.append(winning_edge)
            
    def print_tree(self):
        
        total_weight = 0
        
        for e in self.min_span_tree:
            
            try:
                total_weight += e.get_weight()
            except AttributeError:
                pass
            print(e.__str__())
        print("Total Weight: " + str(total_weight))