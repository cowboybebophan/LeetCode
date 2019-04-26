"""
Solution 1:
首先创建一个包含对应括号的字典，注意要将右括号创建为key(因为是在遍历到右括号时做判断).
然后开始遍历s中的字符，遇到左括号时放入栈，
遇到右括号时：1，检查此时栈是否为空，返回False若为空；2，对比右括号与栈中最后放入的字符是否为一对(同时栈中的左括号也在一个个被pop出来).
当遍历完成，return stack == [].(为了避免类似与“{[(”这种情况, 这种情况下s是invalid的，但是不判断stack是否为空就判断不了s是否valid)

"""

class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
        return stack == []

"""
Solution 2:(效率没有stack好，但是直接易懂)
先判断s长度，为0返回True，为奇数返回False。
为偶数时，将s中的'()','[]','{}'替换为空。
最后检验s是否为空。

"""

class Solution(object):
    def isValid(self, s):
        n = len(s)
        if n == 0:
            return True
        
        if n % 2 != 0:
            return False
            
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('{}','').replace('()','').replace('[]','')
        
        return s == ''


