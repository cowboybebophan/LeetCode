"""
The recursion solution is similar to problem 94 and problem 144.

As for the iterative way, I modified the preorder traversal(right subtree first), then reverse the result.
(feels like cheating haha) 

"""

# 1 line solution
class Solution:
    def postorderTraversal(self, root):
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []

# Recursively
class Solution:
    def postorderTraversal(self, root):
        res = []
        self.helper(root, res)
        return res
    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            self.helper(root.right, res)
            res.append(root.val)
            
# Iteratively (Cheating)
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res[::-1]

