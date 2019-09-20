# O(n) without extra space

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in range(len(nums))]
        product = 1
        for i in range(1, len(nums)):
            product *= nums[i-1]
            res[i] *= product
        product = 1
        for i in range(len(nums) - 2, -1, -1):
            product *= nums[i+1]
            res[i] *= product
        return res

# O(n) with extra space 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        leftProduct = [1 for _ in range(len(nums))]
        rightProduct = [1 for _ in range(len(nums))]
        
        for i in range(1, len(nums)):
            leftProduct[i] = nums[i-1] * leftProduct[i-1]
        for i in range(len(nums) - 2, -1, -1):
            rightProduct[i] = nums[i+1] * rightProduct[i+1]
        
        for i in range(len(nums)):
            res.append(leftProduct[i] * rightProduct[i])
        return res
