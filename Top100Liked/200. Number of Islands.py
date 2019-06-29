"""
Using recursive DFS:

We use two for-loop to iterate all the elements in grid
If the element is '1', we mark it as '#'(any other symbol will be fine) so we know that we have already visited here.

Then we explore the four neighbor elements: up/down/left/right to see if they are '1's.
Return when we reach the edges or the element is not '1',

When self.dfs(i,j) returns, we know that we have explored the island that grid[i][j] is in.
Therefore, count += 1 and we go to the next element.

"""

class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count
    
    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
