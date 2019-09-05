"""
https://leetcode.com/problems/n-queens-ii/discuss/20147/Python-recursive-dfs-solution.
"""

class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        nums = [-1 for _ in range(n)]
        self.dfs(nums, 0)
        return self.count
    
    def dfs(self, nums, row):
        if row == len(nums):
            self.count += 1
            return
        for i in range(len(nums)):
            nums[row] = i
            if self.valid(nums, row):
                self.dfs(nums, row +1)
    
    def valid(self, nums, row):
        for i in range(row):
            if abs(nums[i] - nums[row]) == row - i or nums[row] == nums[i]:
                return False
        return True
