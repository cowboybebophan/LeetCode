"""
Treat the 2D matrix as a long sorted list.
We set low and high as the first and last index, then we get the number of the middle index by using
num = matrix[mid//cols][mid%cols]

"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target is None:
            return False
        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, (rows * cols - 1)
        while low <= high:
            mid = (low + high) // 2
            num = matrix[mid//cols][mid%cols]
            if target == num:
                return True
            elif target > num:
                low = mid + 1
            else:
                high = mid - 1
        return False
