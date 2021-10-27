

class Graph():
    def __init__(self) -> None:
        self.number_of_nodes = 0
        self.adjacent_list = {}
    
    def add_vertex(self, node):
        self.adjacent_list[node] = []
    
    def add_edge(self, node1, node2):
        #undirected
        if node1 in self.adjacent_list.keys() and node2 in self.adjacent_list.keys():
            if node2 not in self.adjacent_list[node1]:
                self.adjacent_list[node1].append(node2)
            if node1 not in self.adjacent_list[node2]:
                self.adjacent_list[node2].append(node1)
            
        
    def print_tree(self):
        print(self.adjacent_list)

obj = Graph()

obj.add_vertex(0)
obj.add_vertex(1)
obj.add_vertex(2)
obj.add_vertex(3)
obj.add_vertex(4)
obj.add_vertex(5)
obj.add_vertex(6)

obj.add_edge(0,1)
obj.add_edge(0,2)
obj.add_edge(1,2)
obj.add_edge(1,3)
obj.add_edge(2,4)
obj.add_edge(3,4)
obj.add_edge(4,5)
obj.add_edge(5,6)

obj.add_edge(1,3)
obj.add_edge(2,4)
obj.add_edge(3,4)

obj.add_edge(3,1)
obj.add_edge(4,2)
obj.add_edge(4,3)

obj.print_tree()