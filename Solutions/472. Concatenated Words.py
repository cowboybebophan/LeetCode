# DFS
# https://leetcode.com/problems/concatenated-words/discuss/159348/Python-DFS-readable-solution
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        new_words = set(words)  # O(N)
        
        def dfs(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                
                if prefix in new_words and suffix in new_words:  # set lookups are O(1)
                    return True
                if prefix in new_words and dfs(suffix):
                    return True
            
            return False
        
        res = []
        for word in new_words:
            if dfs(word): 
                res.append(word)
        return res
        
# Trie
