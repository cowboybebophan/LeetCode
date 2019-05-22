"""
This is a dutch partitioning problem: https://en.wikipedia.org/wiki/Dutch_national_flag_problem

We are classifying the array into four groups: red(0), white(1), unclassified, and blue(2). 

Initially we group all elements into unclassified. 
We iterate from the beginning as long as the scanner pointer p is less than the blue pointer p2.

If nums[p] == 0, we swap nums[p] and nums[p1] then move both p and p1 pointer forward. 

If nums[p] == 1, the element is already in correct place, so we don't have to swap, 
just move the p pointer forward. 

If nums[p] == 2, we swap nums[p] and nums[p2] then ONLY move p2 backward. Because we don't know whats the original nums[p2]
so we need to scan it after swaping the values.

"""

class Solution(object):
    def sortColors(self, nums):
        p, p1, p2 = 0, 0, len(nums) -1
        while p <= p2:
            if nums[p] < 1:
                nums[p], nums[p1] = nums[p1], nums[p]
                p += 1
                p1 += 1
            elif nums[p] > 1:
                nums[p], nums[p2] = nums[p2], nums[p]
                p2 -= 1
            else:
                p += 1
        
