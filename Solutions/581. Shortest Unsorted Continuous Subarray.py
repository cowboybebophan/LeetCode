"""
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/discuss/103067/Python-O(N)-with-O(1)-space-complexity.-No-sorting
"""

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        l, r = 0, len(nums) - 1
        
        while l < len(nums) - 1 and nums[l] <= nums[l+1]:
            l += 1
        while r > 0 and nums[r] >= nums[r-1]:
            r -= 1
        
        if l >= r:
            return 0
        
        tmp = nums[l:r+1]
        tmpMax, tmpMin = max(tmp), min(tmp)
        
        while l > 0  and nums[l-1] > tmpMin:
            l -= 1
        
        while r < len(nums) - 1 and nums[r+1] < tmpMax:
            r += 1
        
        return r - l + 1
