"""
https://leetcode.com/problems/letter-case-permutation/discuss/342024/Python3-recursive-solution-beats-98-with-explanation
"""

# DFS + Recursion

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        self.dfs(S, 0, res, '')
        return res
    
    def dfs(self, S, index, res, path):
        if index == len(S):
            res.append(path)
            return
        if S[index].isalpha():
            self.dfs(S, index + 1, res, path + S[index].lower())
            self.dfs(S, index + 1, res, path + S[index].upper())
        if not S[index].isalpha():
            self.dfs(S, index + 1, res, path + S[index])
            
# Solution 2

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = ['']
        for ch in S:
            if ch.isalpha():
                res = [i + j for i in res for j in [ch.lower(), ch.upper()]]
            else:
                res = [i + ch for i in res ]
        return res
