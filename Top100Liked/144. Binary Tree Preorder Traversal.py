"""
Similar to problem 94 and 145.
"""
# 1 line solution
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []

# Iterratively
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
                
# Recursively
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        return res
    
    def helper(self, root, res):
        if root:
            res.append(root.val)
            self.helper(root.left, res)
            self.helper(root.right, res)
                   
