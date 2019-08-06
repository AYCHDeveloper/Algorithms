from collections import defaultdict

# This class represents a directed graph using adjancy list represntation

class Graph:
	def __init__(self,vertices):
		# No of vertices
		self.V = vertices

		#default dictionary to store graph
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)

		# A function to perform a Depth-Limited Search
		# from given 'src'
	def DLS(self, src, target, maxDepth):

		print(src, end=" ")
		if src == target:
			print(" ")
			return True

		# If reached the maximum depth, stop recursing
		if maxDepth <=0 :
			return False

		# Recur for all the vertices adjacent to this vertex
		for i in self.graph[src]:
			if(self.DLS(i,target,maxDepth-1)):
				return True

	
		return False

		


g = Graph(7);
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(2,5)
g.addEdge(2,6)

target = 6
maxDepth = 2
src = 0
print(" 							 ========================				")
print("						 	|| Depth-Limited Search ||				    ")
print(" 						  	 ========================				")
print("You can enter define vertices by adding g.addEdge(srcNode, destinationNode) function")
print("Suppose if you wish to have vertices 1,2,3 and edge from 1-->2 and 1-->3 you can write like g.addEdge(1,2) and g.addEdge(1,3) and so on ")
print("please specify the src, target and maxDepth parameters in program before running, Default setting is src=0, target=6 and maxDepth=2")
print("\n \nFollowing is Depth First Search till specified depth:")
if g.DLS(src,target,maxDepth) == True:
	print("\nTarget is reachable from source within specified depth")
else:
	print("\nTarget is NOT reachable from source within specified depth")	


