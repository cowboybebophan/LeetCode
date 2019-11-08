"""
The recursion solution is similar to problem 94 and problem 144.

As for the iterative way, the first one strictly follows the "Left->Right->Root" order.
For the second iterative solution, I modified the preorder traversal(right subtree first), then reverse the result.
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

# Iteratively 1 (set flag)
# You can think of [(root, False)] as root's immediate children have not been visited yet.
# If we meet a node that has a False flag, we change the flag to True and push its children into the stack.
# The next time we meet this same node, we have already visited all of its children.
# which means we have strictly followed the (Left -> Right -> root) order.

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [(root, False)]
        
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    res.append(node.val)
                else:
                    # post-order
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return res
    
# Iteratively 2 (Cheating)
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
