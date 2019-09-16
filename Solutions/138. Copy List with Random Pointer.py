"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        self.visited = {}
        return self.deepCopy(head)
    
    def deepCopy(self, node):
        if not node:
            return None
        if node in self.visited:
            return self.visited[node]
        
        copy = Node(node.val, None, None)
        self.visited[node] = copy 
        
        copy.next = self.deepCopy(node.next)
        copy.random = self.deepCopy(node.random)
        
        return copy
