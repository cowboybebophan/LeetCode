class Solution:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            res = max(self.helper(s, i, i), self.helper(s, i,i+1), res, key = len) # (i,i)和(i,i+1) 分别为odd和even的情况
        return res                                                                 # 比如“aba”和“abba”
    
    def helper(self, s, l, r):
        stop = 0
        while l >= 0 and r < len(s) and s[l] == s[r]: # 对于目前所在字符，判断左右对应位置的字符是否相同
            l -= 1;r += 1
        return s[l+1:r]
