# Same idea as problem 138.Copy List with Random Pointer
class Solution:
    def cloneGraph(self, node):
        self.visited = {}
        return self.deepCopy(node)
    
    def deepCopy(self, node): # input is the node, returns the copy of the node
        if not node:
            return None
        
        if node in self.visited:
            return self.visited[node]
        
        copy = Node(node.val, [])
        self.visited[node] = copy
        
        for n in node.neighbors:
            if n in self.visited:
                copy.neighbors.append(self.visited[n])
            else:
                copy.neighbors.append(self.deepCopy(n))
        self.visited[node] = copy
        return copy
