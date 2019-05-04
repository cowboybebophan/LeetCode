"""
Use backtracking here, idea is similar to 039.Combination Sum.

"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(nums, t):
            if not nums:
                res.append(t)
                return
            for i, num in enumerate(nums):
                helper(nums[:i]+nums[i+1:], t + [num])
        helper(nums, [])
        return res
        
        
