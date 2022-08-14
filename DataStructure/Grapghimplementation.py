import traceback


class Graph:
    def __init__(self,gdict=None):
        if gdict==None:
            self.gdict=gdict
    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)

        
#bfs Example: Breadth First Traversal (Or Level Order Traversal)


    def bfs(self,vertex):
        visited=[vertex]
        queue=[vertex]
        while queue:
            deVertex=queue.pop(0)
            for i in self.gdict[deVertex]:
                if i not in visited:
                    visited.append(i)
                    queue.append(i)
        return visited

#dfs Example:Depth First Traversals
#Inorder Traversal (Left-Root-Right)
#Preorder Traversal (Root-Left-Right)
#Postorder Traversal (Left-Right-Root)

    def bfs(self,vertex):
        visited=[vertex]
        Stacktraceback=[vertex]
        while Stacktraceback:
            deVertex=Stacktraceback.pop()
            for i in self.gdict[deVertex]:
                if i not in visited:
                    visited.append(i)
                    Stacktraceback.append(i)
                    Stacktraceback=[vertex]

        return visited




    dictionary1={'a':["b","c","d"],
                "b":["a","d","e"],
                "c":["d","e"]}


    