"""
在传统的二分搜索的基础上做一些改进：对于什么时候移动lo和hi指针做一个细致的场景区分。
"""
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
From comment section in https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14419/Pretty-short-C%2B%2BJavaRubyPython

Conidtion 1 represents when target is on the left side of mid, but target is not necessarily smaller that nums[mid]); 
Therefore, we update hi to the left side of mid.  

Condition 2 represents when target is on the right side of mid, here we update lo to the right side of mid.

"""
Or

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] <= nums[hi]:
                if nums[mid] < target <= nums[hi]: # 挑选简单的condition先写，把复杂的留到else里
                    lo = mid + 1
                else:
                    hi = mid - 1
            elif nums[mid] >= nums[lo]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
        return -1
