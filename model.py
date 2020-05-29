import networkx as nx
import matplotlib.pyplot as plt
import random

class Population:
	def __init__(self, numvertices, numedges):
		self.adj_matrix

	def simulate():
		pass

	def simulate_day():
		pass

class Graph(object):
	def __init__(self, n, edge_prob):
		self.n = n

		### makes sure the graph is connected
		self.isconnected = False
		while (not isconnected):
			self.graph = nx.fast_gnp_random_graph(n=n, p=edge_prob)
			isconnected = nx.is_connected(self.graph)

		nx.set_node_attributes(self.graph, 0, 'state')

		self.avg_deg_cen = self.avg_degree_centrality()
		#self.avg_com_cen = self.avg_communicability_centrality()
		self.avg_ecc = self.avg_eccentricity()
		self.diameter = nx.diameter(self.graph)

		self.infected_vertices = []
		self.num_infected = 0
		self.color_map = []
		self.rand_infect()
		self.frac_infect = self.frac_infected()

	def rand_infect(self):
		for i in range(self.n):
			flip = random.randint(0, 1)
			if flip:
				self.graph.nodes[i]['state'] = 1
				self.infected_vertices.append(i)
				self.num_infected+=1
				self.color_map.append('red')
			else:
				self.color_map.append('green')

	def avg_degree_centrality(self):
		"""
		The degree centrality for a node v is the fraction of nodes it is connected to.
		"""
		return sum(nx.degree_centrality(self.graph).values())/self.n

	def avg_communicability_centrality(self):
		"""
		Communicability centrality, also called subgraph centrality, of a node n is the sum of closed walks of all lengths starting and ending at node n.
		"""
		return sum(nx.communicability_centrality(self.graph).values())/self.n

	def avg_eccentricity(self):
		"""
		The eccentricity of a node v is the maximum distance from v to all other nodes in G.
		"""
		return sum(nx.eccentricity(self.graph).values())/self.n

	def frac_infected(self):
		return self.num_infected/self.n

	def node_state(self, node):
		state = self.graph.nodes[node]['state']
		if state == 0:
			print ("Not infected")
		elif state == 1:
			print ("Infected")
		else:
			print ("Recovered")

def test():
	G = Graph(50, 0.3543539)

	plt.subplot(121)
	nx.draw(G.graph, with_labels=True, font_weight='bold', node_color=G.color_map)
	plt.show()

if __name__ == '__main__':
	test()

