class Solution:
    def lengthOfLongestSubstring(self, s):
        usedChar = {}
        maxLength = start = 0
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max( maxLength, i - start + 1)
            usedChar[s[i]] = i
        return maxLength
        
