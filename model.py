import networkx as nx

class Population:
	def __init__(numvertices, numedges):
		self.adj_matrix

	def simulate():
		pass

	def simulate_day():
		pass

	def regularness():
		pass

	def frac_infected():
		pass


class Graph(object):
	def __init__(numvertices, numedges):
		self.numvertices = numvertices
		self.graph = nx.gnp_random_graph(numvertices, numedges)

"""class Graph(object):

    def __init__(self, adj_matrix, numvertices):
        self.numvertices = numvertices
        self.graph_dict = {}
        self.adj_matrix = adj_matrix
        self.generate_edges()

    def vertices(self):

        return list(self.graph_dict.keys())
      
    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = Node(vertex)

    def add_edge(self, vertex1, vertex2):
        self.graph_dict[vertex1].add_neighbor(graph_dict[vertex2])

    def generate_edges():
    	n = self.numvertices
    	for i in range(n):
    		for j in range(n):
    			if adj_matrix[i][j]:
    				self.add_edge(i, j)

    def __str__(self):
        res = "vertices: "
        for k in self.graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res
"""
