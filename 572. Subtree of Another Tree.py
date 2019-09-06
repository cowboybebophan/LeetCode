class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if self.isSametree(s, t):
            return True
        if not s:
            return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def isSametree(self, p, q):
        if not (p and q):
            return p == q
        return p.val == q.val and self.isSametree(p.left, q.left) and self.isSametree(p.right, q.right)
