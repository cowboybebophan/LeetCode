class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pool = nums
        heapq.heapify(self.pool)
        while len(self.pool) > self.k:
            heapq.heappop(self.pool)
   
    def add(self, val: int) -> int:
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]
