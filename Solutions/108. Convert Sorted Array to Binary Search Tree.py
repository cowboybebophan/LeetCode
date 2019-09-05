# Passin the slicing array

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        l = len(nums)
        
        if l == 1:
            return TreeNode(nums[0])
        
        root = TreeNode(nums[l//2])
        root.left = self.sortedArrayToBST(nums[:l//2])
        root.right = self.sortedArrayToBST(nums[(l//2) + 1:])
        return root


# Passin the indices

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.helper(nums, 0, len(nums)-1)
        
    def helper(self, nums, left, right):
        if left > right:
            return None
        mid = (left + right)//2
        root = TreeNode(nums[mid])
        root.left = self.helper(nums, left, mid-1)
        root.right = self.helper(nums, mid+1, right)
        return root
        
