# DFS Recursively
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if root.val == sum and not (root.left or root.right):
            return True
        sum -= root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
        
Or

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if root.val == sum and not (root.left or root.right):
            return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
        
# DFS Iteratively using Stack

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        stack = [(root, sum)]
        while stack:
            node, value = stack.pop()
            if node:
                if not (node.right or node.left) and node.val == value:
                    return True
                stack.append((node.left, value - node.val))
                stack.append((node.right, value - node.val))
            else:
                continue
        return False
