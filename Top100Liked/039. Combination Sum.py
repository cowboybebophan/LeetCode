"""
Credit goes to: https://leetcode.com/problems/combination-sum/discuss/237525/Python-simple-Bactracking-solution-beats-99

We use backtracking and recursion here.

Backtracking is a more general purpose algorithm.
Depth-First search is a specific form of backtracking related to searching tree structures. 

"""

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        def helper(candidates, target, t):
            if not target:
                res.append(t)
                return
            for i, num in enumerate(candidates):
                if target >= num:
                    helper(candidates[i:], target - num, t + [num]) 
                else: break
        helper(candidates, target, [])
        return res  
        
        # Use candidates[i:] to avoid duplicate combinations like [2,2,3] and [2,3,2]

        
# Solution 2
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        for i, num in enumerate(candidates):
            if num <= target:
                self.helper(candidates[i:], target - num, res, [num])
        return res
    
    def helper(self, candidates, target, res, path):
        if target == 0:
            res.append(path)
        for i, num in enumerate(candidates):
                if num <= target:
                    self.helper(candidates[i:], target - num, res, path + [num])
