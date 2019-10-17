"""
https://leetcode.com/problems/word-ladder-ii/discuss/40482/Python-simple-BFS-layer-by-layer
"""
class Solution:
    def findLadders(self, beginWord, endWord, wordList) -> List[List[str]]:
        res = []
        wordList = set(wordList)
        alpha = string.ascii_lowercase
        layer = {beginWord:[[beginWord]]}
        
        while layer:
            newLayer = collections.defaultdict(list)
            for word in layer:
                if word == endWord:
                    res.extend(l for l in layer[word])
                    return res 
                for i in range(len(word)):
                    for ch in alpha:
                        newWord = word[:i] + ch + word[i+1:]
                        if newWord in wordList:
                            newLayer[newWord] += [path + [newWord] for path in layer[word]]
            wordList -= set(newLayer.keys())
            layer = newLayer
        return res
