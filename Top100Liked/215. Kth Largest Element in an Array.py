# Method 1  O(NlogN)
# Using build-in fuction sorted/sort

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse = True) [k-1]

# Method 2
# Using bulid-in fuction heapq.nlargest

import heapq
class Solution:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]

# Method 3  O(N + kLogN)
# Using a Min-Heap to implemente a Max-Heap

import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        nums = [-num for num in nums]
        heapq.heapify(nums)
        res = float('inf')
        for _ in range(k):
            res = heapq.heappop(nums)
        return -res
        
 # Method 4
 # Using quickSelect/quickSort
 
