"""
Similar to 153. Find Minimum in Rotated Sorted Array.
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            while lo < hi and nums[lo] == nums[hi]:
                lo += 1
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[hi]
