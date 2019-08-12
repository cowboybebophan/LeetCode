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
    def isSymmetric(self, root):
        def isSym(L,R):
            if L and R and L.val == R.val: 
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return L == R   # means L == None == R
        return not root or isSym(root.left, root.right)
    
    or
  
    def isSymmetric(self, root):
        def isSym(L,R):
            if L and R and L.val == R.val: 
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            elif L == R == None:
                return True
            else:
                return False
        return not root or isSym(root.left, root.right)
