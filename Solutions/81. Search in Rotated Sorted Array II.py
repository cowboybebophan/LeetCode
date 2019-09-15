"""
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/discuss/177150/Search-in-Rotated-Sorted-Array-I-python-code
"""
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            while lo < hi and nums[lo] == nums[hi]: #这样的目的是为了能准确判断mid位置，所以算法的最坏时间复杂度为O(n)
                lo += 1
            mid = (lo + hi) // 2
            if target == nums[mid]:
                return True
            
            elif nums[mid] >= nums[lo]: #高区
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            elif nums[mid] <= nums[hi]: #低区
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return False
