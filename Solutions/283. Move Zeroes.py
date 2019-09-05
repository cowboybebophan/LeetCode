# Two Pointers
class Solution(object):
    def moveZeroes(self, nums):
        i = j = 0
        while i < len(nums):
            if nums[i] != 0 :
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            i += 1

# Sort
class Solution(object):
    def moveZeroes(self, nums):
        nums.sort(key = lambda x: x == 0)

# 
