class Solution:
    def lengthOfLongestSubstring(self, s):
        usedChar = {} # 创建一个空字典用来储存和更新遇到的字符
        maxLength = start = 0 # maxLength用来记录目前为止无重复字符的最长长度；start为起始的左指针，右指针为当前位置i
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]: # 判断i所处的字符是否已经在之前出现过：若之前出现过并且左指针start
                start = usedChar[s[i]] + 1 # 目前还在之前出现的位置或其左侧，那么将左指针start更新到之前出现的位置的右边一位
            else:
                maxLength = max( maxLength, i - start + 1) # 若i所处的字符之前从未出现过：更新maxLength为目前为止无重复字符长度的最大值
            usedChar[s[i]] = i # 无论之前是否出现过，将当前i位置的字符在字典内进行更新
        return maxLength
    
