# Dictionary + quickSelect

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        count = list(count.items())
        
        self.quickSelect(count, 0, len(count) - 1, k)
        
        return [c[0] for c in count[:k]]
        
    
    def quickSelect(self, count, low, high, k):
        if low < high:
            p = self.partition(count, low, high)
            if p == k - 1:
                return 
            elif p > k - 1:
                self.quickSelect(count, low, p-1, k)
            else:
                self.quickSelect(count, p+1, high, k)
        
    
    def partition(self, count, low, high):
        pivot = count[high][1]
        i = low
        
        for j in range(low, high):
            if count[j][1] > pivot:
                count[j], count[i] = count[i], count[j]
                i += 1
                
        count[i], count[high] = count[high], count[i]
        return i

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
