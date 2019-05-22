"""
Variable a tells you the number of ways to reach the current step, 
and b tells you the number of ways to reach the next step. 
So for the situation one step further up, the old b becomes the new a, and the new b is the old a+b, 
since that new step can be reached by climbing 1 step from what b represented or 2 steps from what a represented.

"""


class Solution(object):
    def climbStairs(self, n):
        if n == 1: return 1
        a, b = 1, 2
        for _ in range(n-1):
            a, b = b, a + b
        return a
