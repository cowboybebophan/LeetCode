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
    
Note: 如何理解 start <= usedChar[s[i]] ：
    例如 “tmmzuxta”，在i = 2时因为之前出现过‘m’所以此时将start更新为2，当i = 6时，此时‘t’虽然已经在之前出现过，
    但是此时start已经在之前一个‘t’的右侧，所以不用进入if循环更新start，而是进入else更新maxLength。
    如果去掉这个判断，结果为len(‘mzuxt’) = 5；加上判断 结果为len(‘mzuxta’) = 6.
