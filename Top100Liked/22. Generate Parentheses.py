# recursively

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
