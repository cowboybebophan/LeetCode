class Solution:
    def subarraySum(self, nums, k):
        dic = {0:1}
        count = 0
        s = 0
        
        for num in nums:
            s += num
            count += dic.get(s - k, 0)
            dic[s] = dic.get(s, 0) + 1
        return count
