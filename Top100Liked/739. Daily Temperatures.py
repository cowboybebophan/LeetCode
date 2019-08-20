class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        res, stack = [], []
        
        for i in range(len(T)):
            
            while stack and stack[-1][1] < T[i]:
                j = stack.pop()[0]
                res[j] = i - j
            stack.append([i, T[i]])
            res.append(0)
        
        return res
