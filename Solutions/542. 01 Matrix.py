class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows , cols = len(matrix), len(matrix[0])
        res = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] != 0:
                    res[i][j] = self.bfs(matrix, res, i, j)
        return res
    
    def bfs(self, matrix, res, i, j):
        q = collections.deque([[i, j, 0]])
        while q:
            r, c, dist = q.popleft()
            if 0<= r < len(matrix) and 0 <= c < len(matrix[0]):
                if matrix[r][c] == 0:
                    return dist
                else:
                    q.extend([(r+1, c, dist+1),(r-1, c ,dist+1),(r, c+1, dist+1),(r, c-1, dist+1)])
