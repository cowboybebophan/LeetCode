# DFS + Recursion

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs(n, n, res, '')
        return res
    
    def dfs(self, left, right, res, path):
        if left:
            self.dfs(left - 1, right, res, path + '(')
        if left < right:
            self.dfs(left, right - 1, res, path + ')')
        if not right:
            res.append(path)
            
# Solution 2
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(p, left, right, parens = []):
            if left:
                generate(p + '(', left - 1, right)
            if left < right:
                generate(p + ')', left, right - 1)
            if not right:
                parens += [p] # or "parens.append(p)", if you write "parens += p",  
            return parens     # parens will be something like ["(","(","(",")",")",")","(","(",".........]
        
        return generate('', n, n)

"""
Note: 
The most import trick is that the default argument value (parens = []) is execute at define time, not runtime.
So, in this case, every changes to parens in each recursive call, 
will change the same list, that's why the parena will includes all the possible result.

check this out: https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments

"""

