"""
https://leetcode.com/problems/validate-binary-search-tree/discuss/32112/Learn-one-iterative-inorder-traversal-apply-it-to-multiple-tree-questions-(Java-Solution)

Do an inorder traversal and then check if the traversal array is in an ascending order.

"""
# Recursively

class Solution:
    def isValidBST(self, root):

        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)

        return helper(root)

# Iteratively
# While doing inorder traversal, we check if the tree is valid.

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res, stack = [], []
        curr = root
        
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                node = stack.pop()
                if res and node.val <= res[-1]: # Check curr node value with the last value we push into result.
                    return False
                else:
                    res.append(node.val)
                curr = node.right
        return True
