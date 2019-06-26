"""
Solution 1 uses dynamic programming. Same idea as problem 152. Maximum Product subarray.

Solution 2 comes from Kadane's algorithm:
https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm

Note: this function will perform in-place modification.

We start from the second number nums[1] and check if the nums[i-1] is positive or not:
If nums[i-1] is positive we update nums[i] to nums[i] + nums[i-1], otherwise nums[i] remains nums[i].

After the modification, each element in the array represents the maximum subarray sum ending at position i.
For exmaple: [-2,1,-3,4,-1,2,1,-5,4] --> [-2,1,-2,4,3,5,6,1,5]

"""

# Solution 1

class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return None
        # maxSum stores the max sum we have found so far
        # imax stores the max sum of subarray that ends with 
        # the current number nums[i]
        
        maxSum = imax  = nums[0]
        
        for i in range(1, len(nums)):
            imax = max (nums[i], imax + nums[i] )
            maxSum = max(maxSum, imax)
        return maxSum

# Solution 2

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)


"""
If we want to find out the starting and ending index of the maximum subarray as well, 
we could write the code like this: 

"""

class Solution:
    def maxSubArray(self, nums):
        max_ending_here = nums[0]
        start_old = start = end = max_so_far = 0
        for i, x in enumerate(nums[1:], 1):
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
            if max_ending_here < 0:
                start = i + 1
            elif max_ending_here == max_so_far:
                start_old = start
                end = i
        return (max_so_far , start_old, end)
