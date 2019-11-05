# DFS Recursively
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []
        self.findPath(root, res, str(root.val))
        return res
    
    def findPath(self, node, res, path):
        if not (node.left or node.right):
            res.append(path)
        if node.left:
            self.findPath(node.left, res, path + "->" + str(node.left.val))
        if node.right:
            self.findPath(node.right, res, path + "->" + str(node.right.val))
            
# DFS + stack
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res, stack = [], [(root, "")]
        
        while stack:
            node, path = stack.pop()
            if not (node.left or node.right):
                res.append(path + str(node.val))
            if node.left:
                stack.append((node.left, path + str(node.val) + "->"))
            if node.right:
                stack.append((node.right, path + str(node.val) + "->"))
        
        return res
    
# BFS + queue
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res, queue = [], collections.deque([(root, "")])
        
        while queue:
            node, path = queue.popleft()
            if not (node.left or node.right): # current node is leaf
                res.append(path + str(node.val))
            if node.left:
                queue.append((node.left, path + str(node.val) + "->"))
            if node.right:
                queue.append((node.right, path + str(node.val) + "->"))
        
        return res
