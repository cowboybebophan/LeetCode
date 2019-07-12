class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic, res = {}, []
        
        for i in nums1:
            dic[i] = dic.get(i, 0) + 1
        for j in nums2:
            if j in dic and dic[j] > 0:
                res += [j]
                dic[j] -= 1
        return res
    
