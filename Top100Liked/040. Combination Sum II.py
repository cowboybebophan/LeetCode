https://leetcode.com/problems/combination-sum-ii/discuss/17020/Easy-to-understand-Python-solution-(backtracking).

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, res, [])
        return res
    
    def dfs(self, candidates, target, index, res, path):
        if target == 0:
            res.append(path)
            return
        for i in range(index,len(candidates)):
            if i > index and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] <= target:
                self.dfs(candidates, target - candidates[i], i+1, res, path + [candidates[i]])
                       
