https://leetcode.com/problems/maximal-square/discuss/164120/Python-or-DP-tm

# Dynamic Programming

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        row, col = len(matrix), len(matrix[0])
        dp = [[1 if matrix[i][j] == '1' else 0 for j in range(col)] for i in range(row)]
        
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                else:
                    dp[i][j] == 0
        
        res = max(max(rows) for rows in dp)
        return res ** 2
