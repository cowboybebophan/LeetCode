class Solution:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            odd = self.helper(s, i, i)
            even = self.helper(s, i,i+1)  # (i,i)和(i,i+1) 分别为odd和even的情况, 比如“aba”和“abba”                                                                
            res = max(odd, even, res, key = len) 
        return res                                                             
    
    def helper(self, s, l, r):
        stop = 0
        while l >= 0 and r < len(s) and s[l] == s[r]: # 对于目前所在字符，判断左右对应位置的字符是否相同
            l -= 1;r += 1
        return s[l+1:r]
