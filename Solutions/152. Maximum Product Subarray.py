"""
Using dynamic programming, full credit goes to:
https://leetcode.com/problems/maximum-product-subarray/discuss/48230/Possibly-simplest-solution-with-O(n)-time-complexity

"""

# DP
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return None
        # maxProd stores the max product we have found so far
        # imax / imin stores the max / min product of
        # subarray that ends with the current number nums[i]
        
        maxProd = imax = imin = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] < 0:                 # multiplied by a negative makes big number smaller, small number bigger
                imax, imin = imin, imax     # so we redefine the extremums by swapping them
            
            imax = max(nums[i], imax * nums[i])    # max/min product for the current number is either the current number itself
            imin = min(nums[i], imin * nums[i])    # or the max/min by the previous number times the current one
            maxProd = max(maxProd, imax)           # the newly computed max value is a candidate for our global result
        return maxProd
