"""
Credit goes to StefanPochmann: https://leetcode.com/problems/jump-game/discuss/20907/1-6-lines-O(n)-time-O(1)-space

Going forwards. max_reach tells the maximum index we can reach so far.

"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i,n in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + n)
        return True

""" 
Going backwards:
"""
class Solution:
    def canJump(self, nums):
        goal = len(nums) - 1
        for i in range(len(nums))[::-1]:
            if i + nums[i] >= goal:
                goal = i
        return not goal

 
 
