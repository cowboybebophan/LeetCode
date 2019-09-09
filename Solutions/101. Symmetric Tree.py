"""
https://leetcode.com/problems/symmetric-tree/discuss/33068/6line-AC-python

"""

# Iteratively
class Solution:
    def isSymmetric(self, root):
        level = [root]
        while level:
            values = [node.val if node else None for node in level]
            if values != values[::-1]: 
                return False
            level = [child for node in level if node for child in (node.left, node.right)]
        return True
      
# Recursively
class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        return self.helper(root.left, root.right)
    
    def helper(self, L, R):
        if L and R:
            return L.val == R.val and self.helper(L.left, R.right) and self.helper(L.right, R.left)
        else:
            return L == R
