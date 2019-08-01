# Dictionary + Heap

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        heap = []
        res = []
        
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        
        for key in dic:
            heapq.heappush(heap, [key, dic[key]])
        
        res = heapq.nlargest(k, heap, key = lambda x: x[1])
        
        return [x[0] for x in res]
        
# Dictionary + sort()

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        l = res = []
        
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for key in dic:
            l.append([key, dic[key]])
        
        l.sort(key = lambda x: x[1], reverse = True)
        res = [x[0] for x in l[:k]]
        
        return res        
