# one line

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        return sorted([ (i,j) for i in range(R) for j in range(C)], key = lambda x: abs(x[0]- r0) + abs(x[1] - c0))
        
# 
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        def distance(point):
            (x, y) = point
            return abs(r0 - x) + abs(c0 - y)
        points = [(i, j) for i in range(R) for j in range(C)]
        
        return sorted(points, key = distance)
    
