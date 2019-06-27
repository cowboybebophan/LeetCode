"""
Check some different solutions from caikehe:
https://leetcode.com/problems/majority-element/discuss/51712/Python-different-solutions-(dictionary-bit-manipulation-sorting-divide-and-conquer-brute-force-etc).

"""

class Solution(object):
    def majorityElement(self, nums):
        
        for num in set(nums):
            if nums.count(num) > len(nums)/2:
                return num
