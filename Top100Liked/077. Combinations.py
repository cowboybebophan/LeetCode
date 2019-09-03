"""
https://leetcode.com/problems/combinations/discuss/26990/Easy-to-understand-Python-solution-with-comments.

"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        nums = [i for i in range(1, n+1)]
        self.dfs(nums, k, 0, res, [])
        return res
    
    def dfs(self, nums, k, index, res, path):
        if k == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            self.dfs(nums, k-1, i+1, res, path+[nums[i]])
