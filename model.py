import networkx as nx
import matplotlib.pyplot as plt

class Population:
	def __init__(self, numvertices, numedges):
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
	def __init__(self, n, edge_prob):
		self.n = n
		self.graph = nx.fast_gnp_random_graph(n=n, p=edge_prob)
		self.avg_deg_cen = avg_degree_centrality()

	def rand_infect():
		pass

	def avg_degree_centrality():
		"""
		The degree centrality for a node v is the fraction of nodes it is connected to.
		"""
		return sum(nx.degree_centrality(self.graph).values())/self.n

	def avg_communicability_centrality():
		"""
		Communicability centrality, also called subgraph centrality, of a node n is the sum of closed walks of all lengths starting and ending at node n.
		"""
		return sum(nx.communicability_centrality(self.graph).values())/self.n


def test():
	G = Graph(50, 0.3543539)
	print (nx.degree_centrality(G.graph))
	print (sum(nx.degree_centrality(G.graph).values())/50)


	plt.subplot(121)
	nx.draw(G.graph, with_labels=True, font_weight='bold')
	plt.show()

if __name__ == '__main__':
	test()

