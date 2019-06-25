"""
Solution 1 uses list.sort(key = ,reverse =), here we create our own key 'sortDistance' : square of the distance between 
a point and the origin.

Solution 2 is of the same idea.

Solution (3 and 4) uses the heapq.nsmallest(k, iterable, key = ) function in the heapq module. 
Check https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/

"""

# Solution 1

class Solution(object):
    def kClosest(self, points, K):
    
        def sortDistance(point):
            return point[0] ** 2 + point[1] ** 2
        
        points.sort(key = sortDistance)
        
        return points[:K]
        
# Solution 2

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

# Solution 3

import heapq

class Solution:
    def kClosest(self, points, K):
        def distance(point):
            return point[0]**2 + point[1]**2
        return heapq.nsmallest(K, points, key = distance)
        
Or

import heapq

class Solution:
    def kClosest(self, points, K):
        return heapq.nsmallest(K, points, lambda (x,y): x**2 + y**2)
        
# Solution 4

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
