“”“
https://leetcode.com/problems/unique-binary-search-trees/discuss/31666/DP-Solution-in-6-lines-with-explanation.-F(i-n)-G(i-1)-*-G(n-i)
https://www.geeksforgeeks.org/construct-all-possible-bsts-for-keys-1-to-n/

“”“

class Solution:
    def numTrees(self, n: int) -> int:
        res = [0 for i in range(n+1)]
        res[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                res[i] += res[j] * res[i-1-j]
        return res[n]
            
