from queue import PriorityQueue

class BestFirstSearch:

    def __init__(self):
        print("Welcome to Greedy Best First (Heuristic) Search.")
        print("This Program assumes no cycles in search tree else it can show unpredictable results or might crash!")


    def findPath(self,graph, start, end):
        
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0) # get the first path into the queue
            node = path[-1]  # get the last node from path
            node = node[-1]
            
        
            if node == end:
                print("path found! Showing the Path from: ",start,"  to  ", end)
                return path
            for adjacent in graph.get(node,[]):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)    




    def Greedy_Best_First_Search(self, graph_dict, startNode, goal):
        path_found = False
        currentNode = startNode
        visited = []   # list of covered nodes
        pq = PriorityQueue()
        distanceTravelled = 0   # distance travelled in visited
        dict_object = (0,currentNode)
        pq.put(dict_object)

        while not pq.empty():   
            
            pick_from_list = pq.get()
            currentNode = pick_from_list[1]

            if currentNode == goal:
                print("We found the goal: ", currentNode)
                visited.append(currentNode)
                print("Traveresed Nodes: ",visited)
                print(self.findPath(graph_dict,startNode,goal))
                path_found = True
                break
            else:
                for (distance, neighbourCity) in graph_dict.get(currentNode, []):    
                    #print("printing neighbours")
                    if currentNode not in visited:
                        visited.append(currentNode)
                    dict_d = (distance, neighbourCity)
                    pq.put(dict_d)             
        if not path_found:
            print("After searching greedy search could not reach from: ",startNode,"  to  ",goal)


if __name__ == '__main__':

        
    print("Greedy Best First takes next step by taking the most promising path in the current scenario."+
        "\n The Greedy_Best_First_Search search method takes 3 arguments the first one is graph in dictionary \n format, second is start node"
        +"and finally the goal node")
    print("Best First search is not always optimal and it can stuck while searching the goal. ")
    print("If you wish to add an Edge from S to A,B,C S-->A, S-->B, S-->C then \'S\': [(3,\'A\'),(6,\'B\'),(5,\'C\')] keep on adding until you are done.")
    print()
    print()
    bfs = BestFirstSearch()                                       # creating an instance of BestFirstSearch class
    print("---------------------------------------------------")
    problem_graph = {'S': [(3,'A'), (6,'B'), (5,'C')], 
                  'B': [(14,'G'), (12,'F')], 
                  'A': [(8,'E'), (9,'D')], 
                  'C':[(7,'H')],
                  'H':[(6,'J'), (5,'I')], 
                  'I':[(2,'J'), (10,'K'),(1,'L')]}                # Representing graph as dictionary  
    bfs.Greedy_Best_First_Search(problem_graph,'S','I')           # calling greedy best first search method
    
    
