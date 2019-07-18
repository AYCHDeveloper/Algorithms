# This is a python program to implement Breadth First Search from Artificial intelligence Course
from collections import defaultdict

class Graph:

	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)


	def DFS_tree(self,graph, start):

		DFS_Stack = []

		explored = []
		
		DFS_Stack.append(start)
		#explored.append(start)

		# keep looping until there are nodes still to be checked
		while DFS_Stack:
			print("Stack: ",DFS_Stack)
			# pop shallowest  node (first node) from queue
			node = DFS_Stack.pop()
			print("Node popped from Stack: ",node)
			if node not in explored:
				# add node to list of checked nodes
				explored.append(node)
				#print("Node added into explored List: ", node)
				neighbours = graph[node]
				


				# add neighbours of node to queue
				tempArray = []
				for neighbour in neighbours:
					tempArray.append(neighbour)

				tempArray.reverse()	

				for leftNeighbour in tempArray:
					if leftNeighbour not in DFS_Stack and leftNeighbour != node:			
						DFS_Stack.append(leftNeighbour)
					#print("Neighbours added into the queue: ", neighbour)
			print("-----------------Iteration END--------------------")	
		return explored			 				


if __name__ == '__main__':

	print("					Depth First Search				")
	print(">> Here we represent the traversal of a graph using depth first search")
	print(">> You can enter edges something like following suppose you want an edge from A-->S and A-->B, you will write 'A':['S','B'], if B is leaf node"+
		" then B should have edge to itself such as 'B':['B'] in order program to work correctly! ")
	print(">> Current Items in Stack plus What item is popped from stack currently are shown below step by step..")
	print()
	print()
	print("--------------------------------------------------")


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

	graph = {'A':['S', 'B'],'B':['B'],'S':['G','C'],'G':['H','F'],'H':['H'],'C':['F','E','D'],'F':['F'],'E':['E'],'D':['D']}

	res = g.DFS_tree(graph,'A')

	print("Final order of traversing: ")
	for i in res:
		print(i, end=" ")

