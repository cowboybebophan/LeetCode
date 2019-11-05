# Similar to Problem 783
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.res = float("inf")
        self.pre = -float("inf")
        
        def inorderTraverse(node):
            if not node:
                return 
            inorderTraverse(node.left)
            self.res = min(self.res, node.val - self.pre)
            self.pre = node.val
            inorderTraverse(node.right)
        
        inorderTraverse(root)
        return self.res
