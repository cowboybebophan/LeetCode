class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a,b = 1,1
        for i in range(m, m+n-1):
            a = a * i
        for j in range(1, n):
            b = b * j
        return int(a/b)
