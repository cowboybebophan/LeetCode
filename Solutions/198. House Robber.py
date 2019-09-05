"""
The idea here is Dynamic Programming.

A robber has 2 options: a) rob current house i; b) don't rob current house.

If an option "a" is selected it means she can't rob previous i-1 house but can safely proceed to the one before previous i-2 and gets all cumulative loot that follows.
If an option "b" is selected the robber gets all the possible loot from robbery of i-1 and all the following buildings.

So it boils down to calculating what is more profitable:

a) robbery of current house + loot from houses before the previous 
b) loot from the previous house robbery and any loot captured before that

rob[i] = max(nums[i] + rob[i-2], rob[i-1])

"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        
        rob = [0 for i in range(len(nums))]
        rob[0] = nums[0]
        rob[1] = max(nums[0], nums[1])
        
        for i in range(2, len(rob)):
            rob[i] = max(nums[i] + rob[i-2], rob[i-1])
        return rob[-1]
