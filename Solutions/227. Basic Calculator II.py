"""
https://leetcode.com/problems/basic-calculator-ii/discuss/63076/Python-short-solution-with-stack.
"""
class Solution:
    def calculate(self, s: str) -> int:
        num, stack, sign = 0, [], "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in "+-*/" or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))  # The integer division should truncate toward zero, so we are not using a//b
                num = 0
                sign = s[i]
        return sum(stack)
