"""
https://leetcode.com/problems/subsets/discuss/27301/Python-easy-to-understand-solutions-(DFS-recursively-Bit-Manipulation-Iteratively).
"""

# DFS + Recursion

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, 0, res, [])
        return res
        
    def dfs(self, nums, index, res, path):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, res, path + [nums[i]])

# Iteratively
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [item+[num] for item in res]
        return res
    
"""
For example, {1,2,3} intially we have an emtpy set as result [ [ ] ]
Considering 1, if not use it, still [ ], if use 1, add it to [ ], so we have [1] now
Combine them, now we have [ [ ], [1] ] as all possible subset

Next considering 2, if not use it, we still have [ [ ], [1] ], if use 2, just add 2 to each previous subset, we have [2], [1,2]
Combine them, now we have [ [ ], [1], [2], [1,2] ]

Next considering 3, if not use it, we still have [ [ ], [1], [2], [1,2] ], if use 3, just add 3 to each previous subset, we have [ [3], [1,3], [2,3], [1,2,3] ]
Combine them, now we have [ [ ], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3] ]

"""
