class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
            
        if root.val == sum and not (root.left or root.right):
            return[[root.val]]
        
        return self.dfs(root, [], root.val, sum, [root.val])
        
        
    def dfs(self, node, res, current, target, path):
        for n in [node.left, node.right]:
            if n:
                if self.match(current, n, target):
                    res.append(path + [n.val])
                else:
                    self.dfs(n, res, current + n.val, target, path+[n.val])
        return res
    
    def match(self, current, child, target):
        if not (child.left or child.right) and current + child.val == target:
            return True
        return False
