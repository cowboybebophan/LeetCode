# Iteratively using stack

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        stack = [(root, sum, [])]
        
        while stack:
            node, target, path = stack.pop()
            if node:
                if node.val == target and not (node.left or node.right):
                    res.append(path + [node.val])
                stack.append((node.left, target - node.val, path + [node.val]))
                stack.append((node.right, target - node.val, path + [node.val]))
        return res

# Recursivly using dfs

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        self.dfs(root, sum, [], res)
        return res
    
    def dfs(self, node, target, path, res):
        if node:
            if node.val == target and not (node.left or node.right):
                res.append(path + [node.val])
            self.dfs(node.right, target - node.val, path + [node.val], res)
            self.dfs(node.left, target - node.val, path + [node.val], res)
         
 # Solution 3

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
