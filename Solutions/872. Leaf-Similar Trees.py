# Iteratively
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.findLeaf(root1) == self.findLeaf(root2)
    
    def findLeaf(self, root):
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not (node.left or node.right): # leaf found
                res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

# Recursively
class Solution(object):
    def leafSimilar(self, root1, root2):
        return self.findLeaf(root1) == self.findLeaf(root2)
        
    def findLeaf(self, root):
        if not root:
            return []
        if not (root.left or root.right):
            return [root.val]
        return self.findLeaf(root.left) + self.findLeaf(root.right)
