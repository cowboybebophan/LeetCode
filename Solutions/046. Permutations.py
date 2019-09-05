"""
https://leetcode.com/problems/permutations/discuss/18296/Simple-Python-solution-(DFS).
"""
# DFS + Recursion
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, res, [])
        return res
    
    def dfs(self, nums, res, path):
        if not nums:
            res.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[:i]+ nums[i+1:], res, path + [nums[i]])
        
        
