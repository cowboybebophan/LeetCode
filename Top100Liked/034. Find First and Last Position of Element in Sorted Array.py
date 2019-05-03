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
        def search(n):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] >= n:
                    hi = mid 
                else:
                    lo = mid + 1
            return lo
        lo = search(target)
        return [lo, search(target + 1) - 1] if target in nums[lo:lo+1] else [-1,-1]
            
