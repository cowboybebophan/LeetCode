"""
https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/31381/Python-recursive-and-iterative-solutions.

We are asked to return the inorder traversal here.

However, if we are asked to return a preorder traversal or a postorder traversal, we only need to change 
the order of our statements: check problem 144 and 145.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Iteratively
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmpNode = stack.pop()
                res.append(tmpNode.val)
                root = tmpNode.right
        return res
 
 # Recursively
 class Solution:
    def inorderTraversal(self, root):
        res = []
        self.helper(root, res)
        return res
    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)
 
 
    
