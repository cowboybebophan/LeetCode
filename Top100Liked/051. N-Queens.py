"""
https://leetcode.com/problems/n-queens/discuss/19971/Python-recursive-dfs-solution-with-comments.
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        nums = [-1 for _ in range(n)]
        self.dfs(nums, 0, res, [])
        return res
    
    def dfs(self, nums, row, res, path):
        if row == len(nums):
            res.append(path)
            return 
        for i in range(len(nums)):
            nums[row] = i
            if self.valid(nums, row):
                tmp = '.' * len(nums)
                self.dfs(nums, row + 1, res, path + [tmp[:i] + 'Q' + tmp[i+1:]])
    
    def valid(self, nums, row):
        for i in range(row):
            if abs(nums[row] - nums[i]) == row - i or nums[row] == nums[i]:
                return False
        return True
