"""
https://leetcode.com/problems/k-closest-points-to-origin/discuss/220235/Java-Three-solutions-to-this-classical-K-th-problem.

This is a very classical problem, so-called K-th problem.
Generally, we have 3 approaches to this kind of problem.

I. A very naive and simple solution is to sort the list based on the priority that's given by the problem: 
   in this case, the Euclidean distance from the origin. Then we return the top k-th closest points.
   
   Time Complexity: O(NlogN)
   Advantage: short, intuitive and easy to implement.
   Disadvantage: not very efficient and have to know all of the points previously, 
                 and unable to deal with real-time(online) case, it is an off-line solution.
"""

# Solution I

class Solution(object):
    def kClosest(self, points, K):
    
        def sortDistance(point):
            return point[0] ** 2 + point[1] ** 2
        
        points.sort(key = sortDistance)
        
        return points[:K]
or 

class Solution(object):
    def kClosest(self, points, K):
        points.sort(key = lambda x: x[0] ** 2 + x[1] ** 2)
        return points[:K]
or        

class Solution(object):
    def kClosest(self, points, K):
        return sorted(points, key = lambda x: x[0] ** 2 + x[1] ** 2) [:K]

# list.sort() sorts the list in-place, mutating the list indices, and returns None (like all in-place operations).
# sorted(list) returns a new sorted list, leaving the original list unaffected.

"""
II. The second solution is based on the first one. We don't have to sort all points.
    
    Instead, we maintain a heap of size K. We keep pushing elements into the heap untill the size of the heap reaches K.
    When the heap size is K, we push a new element into the heap then pop out the largest elemnt in the heap so the heap size 
    stays K.
    
    Time Complexity: O(NlogK), Inserting an item to a heap of size k take O(logK) time and we do this for N times.
    Advantage: can deal with real-time(online) stream data. It does not have to know the size of the data previously.
    Disadvantage: not the most efficient solution.

"""
# Solution II

import heapq

class Solution:
    def kClosest(self, points, K):
        
        heap = []
        
        for (x,y) in points:
            distance = -(x**2 + y**2)      # Python's heap is implemented as a min-heap, so we take the negtive of the value
            if len(heap) == K:             # so that we pop the smallest value(the longest distance) out.
                heapq.heappushpop(heap,(distance, x, y))     # When there is K elements in heap, we push and pop in the same
            else:                                            # time to keep a size K heap.
                heapq.heappush(heap,(distance, x, y))
                
        return [(x,y) for (distance, x , y) in heap]
        
Or

import heapq

class Solution:
    def kClosest(self, points, K):
        return heapq.nsmallest(K, points, lambda x: x[0]**2 + x[1]**2)

"""
III. The last solution is based on quick sort, we can also call it quick select.
     
     Time Complexity: Average case : O(N)  | Worst case : O(N * N)
     
"""

# Solution III

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        self.quickSort(points, 0, len(points) - 1, K)
        return points[:K]
    
    
    def quickSort(self, points, l, r, K):
        if l < r:
            p = self.partition(points, l, r)
            if p == K:
                return
            elif p < K:
                self.quickSort(points, p + 1, r, K)
            else:
                self.quickSort(points, l, p - 1, K)
        
        
    def partition(self, points, l, r):
        pivot = points[r]
        i = l - 1
        
        for j in range(l, r):
            if (points[j][0]**2 + points[j][1]**2) < (pivot[0]**2 + pivot[1]**2):
                i += 1
                points[i], points[j] = points[j], points[i]
        points[i+1], points[r] = points[r], points[i+1]
        return i + 1
