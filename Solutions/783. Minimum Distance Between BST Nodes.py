# The idea is to use an in-order traversal and find the difference between the current node and the node previously checked.
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/discuss/238404/100-Python-Solution-%2B-Detailed-Explanation
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        
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
