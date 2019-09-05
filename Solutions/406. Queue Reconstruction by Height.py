"""
https://leetcode.com/problems/queue-reconstruction-by-height/discuss/89345/Easy-concept-with-PythonC%2B%2BJava-Solution
"""
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        d = {}
        res = []
        
        for h, k in people:
            if h not in d:
                d[h] = [[h, k]]
            else:
                d[h].append([h, k])
        
        for key in sorted(d, reverse = True):
            group = sorted(d[key])
            if not res:
                res += group
            else:
                for h, k in group:
                    res.insert(k, [h,k])
        return res
