"""
https://leetcode.com/problems/decode-string/discuss/87563/Share-my-Python-Stack-Simple-Solution-(Easy-to-understand)
"""
class Solution(object):
    def decodeString(self, s):
        stack = [["", 1]]
        num = ""
        
        for ch in s:
            if ch.isdigit(): # or (if ch in '0123456789')
                num += ch
            elif ch == "[":
                stack.append(["", int(num)])
                num = ""
            elif ch == "]":
                c, k = stack.pop()
                stack[-1][0] += c * k
            else:
                stack[-1][0] += ch
        return stack[0][0]
        
