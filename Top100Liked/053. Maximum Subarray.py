"""
This solution comes from Kadane's algorithm:
https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm

Note: this function will perform in-place modification.

We start from the second number nums[1] and check if the nums[i-1] is positive or not:
If nums[i-1] is positive we update nums[i] to nums[i] + nums[i-1], otherwise nums[i] remains nums[i].

After the modification, each element in the array represents the maximum subarray sum ending at position i.
For exmaple: [-2,1,-3,4,-1,2,1,-5,4] --> [-2,1,-2,4,3,5,6,1,5]

"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)
