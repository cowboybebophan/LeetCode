"""
If we want to rotate the matrix by 90 degrees(clockwise), we can transpose the matrix first.

Transposing a metrix exchanges the row and column of the same index: 1st row becomes 1st column, 2nd row becomes 2nd column etc.
Rotating the matrix by 90 degree(clockwise) puts the 1st row to the last column, 2nd row to the 2nd-to-last column.

so we reverse each row after transposing the matrix.

For example: [1,2,3] will become [1,4,7] after transpose. Then we reverse every rows so we get:[7,4,1]
             [4,5,6]             [2,5,8]                                                       [8,5,2]
             [7,8,9]             [3,6,9]                                                       [9,6,3]

If we want to rotate the matrix counterclockwise, we can exchange the corresponding rows after we transpose the matrix.
(1st row becomes the last row, 2nd row becomes the 2nd-to-last row etc.)

"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if i < j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for l in matrix:
            l.reverse()
