class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.maxDepth(root.left) - self.maxDepth(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
            
    
    def maxDepth(self, node):
        if not node:
            return 0
        return 1 + max(self.maxDepth(node.left), self.maxDepth(node.right))
