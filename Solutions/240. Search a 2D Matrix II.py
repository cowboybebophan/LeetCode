"""
We start search the matrix from top right(or bottom left) corner, 
initialize the current position to top right(or bottom left) corner, 
if the target is greater than the value in current position, 
then the target can not be in entire row of current position because the row is sorted, 
if the target is less than the value in current position, 
then the target can not in the entire column because the column is sorted too. 
We can rule out one row or one column each time, so the time complexity is O(m+n).
"""

class Solution:
    def searchMatrix(self, matrix, target):
        
        if not matrix or target is None:
            return False
        
        row, col = len(matrix), len(matrix[0])
        i, j = row - 1, 0
        while i >= 0 and j <= col-1:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1
        return False
    
