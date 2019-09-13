class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        sums = {}
        self.dfs(root, sums)
        max_val = max(sums.values())
        
        return [s for s in sums if sums[s] == max_val]
        
    def dfs(self, node, sums):
        if not node:
            return 0
        s = node.val + self.dfs(node.left, sums) + self.dfs(node.right, sums)
        sums[s] = sums.get(s, 0) + 1 
        return s
