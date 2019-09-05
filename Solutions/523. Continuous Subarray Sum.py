"""
https://leetcode.com/problems/continuous-subarray-sum/discuss/99566/Simple-Python-(10-lines)-with-Explanation-58ms-O(n)-time-O(k)-space
"""

class Solution(object):
    def checkSubarraySum(self, nums, k):
        if k == 0:
            return any(nums[i] == 0 and nums[i + 1] == 0 for i in range(len(nums) - 1))
        
        dic, mod = {0: -1}, 0
        for i, n in enumerate(nums):
            mod = (mod + n) % k
            if mod not in dic:
                dic[mod] = i
            if mod in dic and i - dic[mod] > 1:
                return True
        return False 
        
