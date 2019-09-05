“”“
Check the idea here: http://fisherlei.blogspot.com/2012/12/leetcode-next-permutation.html

"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Use two pointers starting from the back
        # Pointer i stops at the digit that violets the increase trend
        # Pointer j stops and nums[j] > nums[i]
        # Swap i and j and reverse the increasing part behind original i
        i = j = len(nums) - 1 
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
        if i == 0: return self.reverse(0, len(nums)-1, nums)
        
        for x in range(len(nums)-1, i-1, -1):
            if nums[x] > nums[i-1]:
                nums[x], nums[i-1] = nums[i-1], nums[x]
                self.reverse(i, len(nums)-1, nums)
                return
        
    def reverse(self, l, r, nums):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
