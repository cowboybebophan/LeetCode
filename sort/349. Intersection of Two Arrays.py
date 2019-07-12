# One-line 
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

# Brute Force
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            if i not in res and i in nums2:
                res.append(i)
        return res
        
# Dictionary
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic, res = {}, []
        
        for i in nums1:
            dic[i] = dic.get(i, 0) + 1
        for i in nums2:
            if i in dic and i not in res:
                res.append(i)
        return res
