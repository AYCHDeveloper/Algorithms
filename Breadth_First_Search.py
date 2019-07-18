# This is a python program to implement Breadth First Search from Artificial intelligence Course
from collections import defaultdict

class Graph:

	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)


	def BFS_tree(self,graph, start):
		# keep track of all the visited nodes
		explored = []
		# keep track of nodes to be checked
		queue = [start]
		# keep looping until there are nodes still to be checked
		while queue:
			# pop shallowest  node (first node) from queue
			print("Q_unexplored:  ",queue)
			#for i in queue:

			node = queue.pop(0)
			print("Node popped from Queue: ",node)
			if node not in explored:
				# add node to list of checked nodes
				explored.append(node)
				print("adding node into explored: ",node)
				print("Q_explored: ",explored)
				#print("Node added into explored List: ", node)
				#print("Node popped from Queue: "),print(node)
				neighbours = graph[node]


				# add neighbours of node to queue
				for neighbour in neighbours:
					if neighbour not in explored and  neighbour not in queue:
						queue.append(neighbour)
					#print("Neighbours added into the queue: ", neighbour)
			print("-----------------Iteration END--------------------")	
		return explored			 				


if __name__ == '__main__':

	g = Graph()
	res = []
	# graph = {'A': ['B', 'C'],
	#  'C': ['F','G'],
 #     'B': ['D', 'E'],
 #     'D': ['D'],
 #     'E': ['E'],
 #     'F': ['F'],
 #     'G': ['G']
 #     }

 	# There are 3 graphs in this program you can comment one and uncomment other you will be able to see the results. Also change starting point parameter in 
 	# g.BFS_Tree so that from where algorithm should start

	graph = {'A':['S', 'B'],'B':['B'],'S':['G','C'],'G':['H','F'],'H':['H'],'C':['F','E','D'],'F':['F'],'E':['E'], 'D':['D']}


					# The graph is given below for visual depiction
					#		  A
					#		/   \
					#	   S     B
					#    /  \
					#   G    C
					#  / \  /|\
					# H	   F E D


	#graph = {'1':['2', '8','6'],'2':['1','3'],'8':['1','3'],'6':['1','7'],'3':['2','9','4'],'7':['6','9','5'],'9':['3','7','5'],'4':['3','5'],'5':['4','9','7']}

	res = g.BFS_tree(graph,'A')

	print("Final Order of Breadth First Search: ")
	for i in res:
		print(i, end = " ")

