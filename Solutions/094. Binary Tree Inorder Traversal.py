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

# 1 line solution
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

# Iteratively
# 1. Everytime we meet a node, we traverse to its deepest left child, untill there is no left child for the current node.
# 2. Meanwhile, we push the node we visited to the stack.
# 3. If the current node doesn't have a left child, we add the value to the answer and check if it has a right child. 
#    If so, we do step 1 for the current node.

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        curr = root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                tmpNode = stack.pop()
                res.append(tmpNode.val)
                curr = tmpNode.right
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
 
 
    
