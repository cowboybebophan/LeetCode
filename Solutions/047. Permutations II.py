"""
https://leetcode.com/problems/permutations-ii/discuss/18649/Python-easy-to-understand-backtracking-solution.
"""
# DFS + Recursion / Backtracking
class Solution:
    def permuteUnique(self, nums):
        res = []
        nums.sort()
        self.dfs(nums, res, [])
        return res
    
    def dfs(self, nums, res, path):
        if not nums:
            res.append(path)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[:i] + nums[i+1:], res, path + [nums[i]])
