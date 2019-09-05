"""
Using dynamic programming, res[i] represents if the subword s[:i] can be segmented into the words in the dictionary.

"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = [False for i in range(len(s) + 1)]
        res[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if res[j] and s[j:i] in wordDict:
                    res[i] = True
        return res[-1]
