import sys


class Graph:
    def __init__(self,start_node,nodes, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
        #initialize the unvisited nodes list with the list of nodes in this case it's['A','B','C','D','E']
        self.unvisited_nodes=nodes
        #initialize the starting point with 'A' wich is the first node 
        self.start_node=start_node
        #initialize the shortest path with empty dictionary wich is filled later with keys(neigbors of the currentnode 
        # that has the shortest bath) and values(Shortest bath of each neigbor(weight))
        self.shortest_path = {}
        #initialize the visited node dictionary with empty dictionary that will be filled later with the nodes that is visited and asigned
        #  the shortest bath of its neigbors the keys of visited node dictionary is :(best neigbors that has the shorstest bath in the first case it's ('B'))
        #  and the value represent the (current node that we try to find the shortest bath from )in first case it's ('A').

        self.visited_nodes = {}
        #this value represent a large amount of number to be used to initialize the shortest bath of each nodes nodes except the first 
        # node wich has shortest bath assigned to zero 
        self.max_value = sys.maxsize
        
        

    def initializeEdge(self):
        for node in self.unvisited_nodes:
            self.shortest_path[node] = self.max_value
        # initialize the starting node's value with 0   
        self.shortest_path[self.start_node] = 0

# the purpose of this method is to use the dijiksta algorithm to find the shortest bath between any two nods in the
#  (graph of dictionary)
    def spf(self):
        #we initialize the shortest bath dictionary with infinity for all nodes since we don't know yet which is the shortest bath 
        #from the first node ('A') and assign the shortest bath of the first node'A' with zero since the path to reach 'A' from 'A' 
        #is equal to zero.
        self.initializeEdge()
        #this while loop is used the unvisited list to iterate over all nodes and once we calculate the shortest bath of each unvisited nodes 
        #we remove it from the unvisited_nodes list and at the end the unvisited _nodes become empty
        # so we can  iterate through all the nodes. 
        while self.unvisited_nodes:
            #each time we iterate through the while loop we assign the current_min_node to None so after we finish the first while loop 
            # iteration and find the current node shortest bath we ca asign anew node from unvisited_nodes to calculate the shortest bath 
            #for . and so on ....
            current_min_node = None
            #this for loop is to iterate through each unvisited node :first assign the current_min_node with the first node in 
            # the unvisited_nodes list then check the shortest bath of this node (which is zero in the first case) with 
            # the shortest bath of other unvisited nodes which are infinity in the first case. so the output of this for loop is the 
            # current_min_node (the node that has the shortest bath)  
            for node in self.unvisited_nodes:
                if current_min_node == None:
                    current_min_node = node
                elif self.shortest_path[node] < self.shortest_path[current_min_node]:
                    current_min_node = node

            #after we iterate through the loop and find the current_min_node that has the shorted bath or in other word has an min asigned 
            #value (min weight label) now we try to retreive all the neighbors of this node.
            neighbors=self.gdict[current_min_node].keys()
            #we iterate through the neighbors and calculate the shortest bath for each neighbor and then check if this neighbor bath
            #is the shortest path to reach the neighbor or no? if it's the shortest then asign the value to the shortest path dictionary 
            #as value = the path and the key =the neigbor has this path
            #also we assign the (neighbor) key in the visited_nodes dictionary with the value current_min_node that represent 
            #which label to go through to reach this point (neighbor)
            for neighbor in neighbors:
                tentative_value = self.shortest_path[current_min_node] +self.gdict[current_min_node][neighbor] 
                if tentative_value < self.shortest_path[neighbor]:
                    self.shortest_path[neighbor] = tentative_value
                     # We also update the best path to the current node
                    self.visited_nodes[neighbor] = current_min_node
            #after we iterate through  all neighbors of the current_min_node , we remove it from the unvisited_nodes list 
            # and then back to while loop to take the next node in the unvisited_nodes list until we finish all the elements 
            #in the list and then the unvisited_nodes list become empty and we get out from the while loop
            self.unvisited_nodes.remove(current_min_node)
          #  print(self.unvisited_nodes)

          #at the end we  have all the shortest paths for each node and the shorted visited_nodes labels we return those two dictionaries
        return self.visited_nodes, self.shortest_path




def print_result(visited_nodes, shortest_path, start_node, target_node):
    print(visited_nodes) #{'B': 'A', 'C': 'A', 'D': 'B', 'E': 'D'} this is the visited nodes which each value point to the node
    #that represent the shortest bath to reach the 'key'(node) for example the key node 'D' has a shortest bath through 'B' 
    # which represent the vlue of this key and so on...
    print(shortest_path) #{'A': 0, 'B': 5, 'C': 2, 'D': 8, 'E': 15} this is the shortest path which each value is the weight assigned to each 
    #key node for example the path weight to reach key node'D' is 8 and so on...
    path = []
    node = target_node
    #we iterate through all nodes in backward direction till we reach to the start node which is A
    while node != start_node:
        path.append(node)  
        node = visited_nodes[node]

    # Add the start node manually
    path.append(start_node)
    print("the shortest path  {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))



customDict = {
            'A': {'B': 5, 'C': 2},
            'B': {'C': 2, 'D': 3},
            'C': {'B': 3, 'D': 7},
            'D': {'E': 7},
            'E': {'D': 9}
            }
nodes = ['A', 'B', 'C', 'D', 'E']
current = 'A'
g = Graph(current,nodes,customDict)
visited_nodes, shortest_path=g.spf()
#to show the result in a clear way we use this print_result method it returns the shortest bath value from 'A' to 'E' which is =15
#and return the exact path from 'A' to 'E' which is A->B->D->E
print_result(visited_nodes, shortest_path, start_node="A", target_node="E")