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

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res, stack = [], []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmpNode = stack.pop()
                res.append(tmpNode.val)
                root = tmpNode.right
        return all(res[i] < res[i+1] for i in range(len(res)-1))
