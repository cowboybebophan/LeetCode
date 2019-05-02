class Solution:
    def search(self, nums, target):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= target < nums[mid] or nums[mid] < nums[0] <= target or target < nums[mid] < nums[0]: # Condition 1    
                hi = mid - 1
            else: # Condition 2
                lo = mid + 1
        return -1

"""
Conidtion 1 represents when target is on the left side of mid, but target is not necessarily smaller that nums[mid]); 
Therefore, we update hi to the left side of mid.  

Condition2 represents when target is on the right side of mid, here we update lo to the right side of mid.

"""
