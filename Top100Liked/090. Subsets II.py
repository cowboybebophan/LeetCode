"""
https://leetcode.com/problems/subsets-ii/discuss/30305/Simple-python-solution-(DFS).
"""
# DFS + Recursion

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums, 0, res, [])
        return res
    
    def dfs(self, nums, index, res, path):
        res.append(path)
        
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, i + 1, res, path + [nums[i]])
         
"""
The difference between Subsets II and Subsets is that nums might contain duplicates.

We sort the list first making sure that duplicates are adjacent. 

The intuition here is that when we meet a duplicate which we can check by the condition (if nums[i] == nums[i-1]),
we only add the duplicate to all the new subsets that are created by the previous duplicate:

For example: nums = [1,2,2], res = [[]]

For nums[0] = 1, we add 1 to [] then append it to res. So we have res = [[], [1]] now;
For nums[1] = 2, we add 2 to both [] and [1] then append them to res. We have res = [[], [1], [2], [1,2]] now.
For nums[2] = 2, we only add 2 to those subsets that are created by the previous '2': [2] and [1,2], because if add 2 to all
the subsets in res we will have duplicates subsets in res. 

There are two ways to do so:
///
In the first solution:
we use { for j in range(len(res) - l, len(res)) } to get the subsets that are created by nums[i-1].

When {i == 0 or nums[i] != nums[i - 1]} :
we update l = len(res), where we are actually adding the number to all the subsets in res;

In the duplicate case(nums[i] == nums[i-1]):
we keep l as the length of res before we add the duplicate number so that we can get the subsets that are created by nums[i-1]

/// 
In the second solution:
we created a list called cur to store all the NEW subsets that are created by nums[i - 1],
then update res to (res + cur).

For nums[i], 
If nums[i] == nums[i-1]:
we only add nums[i] to the subsets in cur;

If nums[i] != nums[i-1] or i ==0:
we add nums[i] to all the subsets in res.

"""

class Solution:
    def subsetsWithDup(self, nums):
        res = [[]]
        nums.sort()
        
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [nums[i]])
        return res
        

class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        res, cur = [[]], []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                cur = [item + [nums[i]] for item in cur]
            else:
                cur = [item + [nums[i]] for item in res]
            res += cur
        return res
        
