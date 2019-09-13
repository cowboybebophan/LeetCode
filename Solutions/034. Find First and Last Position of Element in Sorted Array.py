"""
Credit goes to StefanPochmann on LeetCode: 
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/14707/9-11-lines-O(log-n)

Here, my helper function is a simple binary search, telling me the first index 
where I could insert a number n into nums to keep it sorted. 
Thus, if nums contains target, I can find the first occurrence with search(target).
I do that, and if target isn't actually there, then I return [-1, -1]. 
Otherwise, I ask search(target+1), which tells me the first index where I could insert target+1, 
which of course is one index behind the last index containing target, so all I have left to do is subtract 1.

"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = self.binarySearch(nums, target)
        high = self.binarySearch(nums, target + 1)
        return [low, high - 1] if target in nums[low:low+1] else [-1, -1]
    
    def binarySearch(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        return low
        
        # Here, we write (target in nums[lo:lo+1]) instead of (target == nums[lo])
        # to avoid the cases when lo is outside [0, len(nums)-1]; for example: search(5) in [2,3,4], returns lo = 3. 
        # The condition 'target in nums[lo:lo+1]' is valid even when lo exceeds the length of nums, it returns False.
        # For example: nums = [1,2,3] , ' 1 in nums[4:5] ' returns False. 
        # Works for when nums=[] as well.
