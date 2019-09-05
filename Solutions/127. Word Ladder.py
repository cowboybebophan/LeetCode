class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        wordList = set(wordList)    # Avoid TLE 为避免超时使用set比较方便
        q = collections.deque([(beginWord, 1)])
        alpha = string.ascii_lowercase
        # 为何是queue而不是stack，因為先进來的字找到继任者后就要排除
        # 下一个选项是根据新找到的字所衍伸的，而不是根据最早的
        while q:
            word, length = q.popleft()
            if word == endWord:
                return length
            
            for i in range(len(word)):
                # hit-> *it 或 h*t 或 hi*
                # 用轮流的字元來替换
                for ch in alpha:
                    # alpha中含有abcd.....z，每个字元都换换看
                    newWord = word[:i] + ch + word[i+1:]
                    # 替换掉某个字元产生的新字，例如說i=0,ch='a'，新字就是'ait'
                    if newWord in wordList:
                        # 如果该新字在list內，则加入q，加入之后将新字从list中移除
                        q.append((newWord, length + 1))
                        wordList.remove(newWord)
        return 0
