"""
When pushing a value into stack, together we store a value that tells the min value in the stack so far. 

(x, min_so_far)

"""

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.stack.append([x,x])
        else:
            self.stack.append([x, min(x, self.stack[-1][1])])
    
    def pop(self) -> None:
        self.stack.pop()
    
    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]
