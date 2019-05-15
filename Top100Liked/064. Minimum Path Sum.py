"""
https://leetcode.com/problems/minimum-path-sum/discuss/23457/C%2B%2B-DP
https://leetcode.com/problems/minimum-path-sum/discuss/23466/Simple-python-dp-70ms

This is a typical DP problem. Suppose the minimum path sum of arriving at point (i, j) is S[i][j], 
then the state equation is S[i][j] = min(S[i - 1][j], S[i][j - 1]) + grid[i][j].

Well, some boundary conditions need to be handled. 
The boundary conditions happen on the topmost row (S[i - 1][j] does not exist) 
and the leftmost column (S[i][j - 1] does not exist).

"""

class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        for i in range(1,m):
            grid[i][0] += grid[i-1][0]
        for j in range(1,n):
            grid[0][j] += grid[0][j-1]
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]
