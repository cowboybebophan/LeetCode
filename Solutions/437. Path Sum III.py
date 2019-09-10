# Brute Force

class Solution:
    def pathSum(self, root, sum): # Returns the total number of all valid paths started from every node in the tree.
        if root:                  
            return self.findPath(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return 0
        
    def findPath(self, node, target):   # Returns the number of all valid paths started from a certain node.
        if node:
            return int(node.val == target) + self.findPath(node.left, target - node.val) + self.findPath(node.right, target - node.val)
        return 0

# Two Sum

class Solution(object):
    def pathSum(self, root, target):
        self.result = 0
        cache = {0:1}
        
        self.dfs(root, target, 0, cache)
        return self.result
    
    def dfs(self, root, target, currPathSum, cache):
        if root is None:
            return
        currPathSum += root.val
        oldPathSum = currPathSum - target
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1
      
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        cache[currPathSum] -= 1
