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

# BFS
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        nodeCopy = Node(node.val, [])
        q = collections.deque([node])
        visited = {node: nodeCopy}
        
        while q:
            node = q.popleft()
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    neighborCopy = Node(neighbor.val, [])
                    visited[neighbor] = neighborCopy
                    visited[node].neighbors.append(neighborCopy)
                    q.append(neighbor)
                else:
                    visited[node].neighbors.append(visited[neighbor])
        return nodeCopy
