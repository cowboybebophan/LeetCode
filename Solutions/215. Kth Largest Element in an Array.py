# Method 1
# Using build-in fuction sorted/sort
# list.sort() is a in-place operation,  sorted(list) returns a new sorted list

class Solution:     # Time: O(NlogN) Space:O(N)
    def findKthLargest(self, nums, k):
        return sorted(nums, reverse = True) [k-1]
Or

class Solution:     # Time: O(NlogN) Space:O(1)
    def findKthLargest(self, nums, k):
        nums.sort(reverse = True)
        return nums[k-1]

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

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.quickSort(nums, 0, len(nums) - 1, k)
        return nums[k-1]
    
    
    def partition(self, nums, low, high):
        pivot = nums[high]
        i = low - 1
        
        for j in range(low, high):
            if nums[j] > pivot:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
        
        nums[i+1], nums[high] = nums[high], nums[i+1]
        return i + 1
    
    def quickSort(self, nums, low, high, k):
        if low < high:
            p = self.partition(nums, low, high)
            if p == k - 1:
                return
            elif p > k - 1:
                self.quickSort(nums, low, p - 1, k)
            else:
                self.quickSort(nums, p + 1, high, k)

 
