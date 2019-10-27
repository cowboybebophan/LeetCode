# Same idea as problem 138.Copy List with Random Pointer
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.visited = {}
        return self.deepCopy(node)

    def deepCopy(self, node):
        if not node:
            return None
        if node in self.visited:
            return self.visited[node]
        
        copy = Node(node.val, [])
        self.visited[node] = copy
        
        for i in node.neighbors:
            if i in self.visited:
                copy.neighbors.append(self.visited[i])
            else:
                copy.neighbors.append(self.deepCopy(i))
        
        return copy
