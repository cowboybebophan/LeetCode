"""
The idea is quite similar to Permutation II. I guess you can call it Backtraking too.
There are two things we should focus on:
1. Avoid duplicates.
2. Find squareful permutations.

Avoid Duplicates:

First, we sort the list so that same numbers in A are adjacent.
When we recurse through the list, we skip the recursion for the same numbers.
For example: [2,2,7], we only do recursion for the first '2' and the result will be res = [[2,7,2]] instead of [[2,7,2],[2,7,2]]

Find squareful permutations:

My first thought is to find all regular permutations for A, then check one by one if they are squareful permutation or not.
It turns out to be Time Limit Exceeded. :(
And then I get inspired by this: https://leetcode.com/problems/number-of-squareful-arrays/discuss/238612/4msC%2B%2B-Simple-Backtracking-like-Permutations-II

lisali2019:
"The only difference is that by calling the recursion every time, the program would check whether the sum of the number on current index and the previous is a square number or not, 
to make sure the sub array from 0 to current index satisfys the Squareful definition."

That really helps! It beats 99% of python solutions.

Thanks lisa!
"""

class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        res = []
        A.sort()
        self.dfs(A, res, [])
        return len(res)
            
    def dfs(self, A, res, path):
        if not A:
            res.append(path)
            return
        
        for i in range(len(A)):
            if len(path) == 0:
                if i > 0 and A[i] == A[i-1]:
                    continue
                self.dfs(A[:i] + A[i+1:], res, path + [A[i]])
            else:
                if i > 0 and A[i] == A[i-1]:
                    continue
                square = (A[i] + path[-1])**(0.5)
                if square.is_integer():
                    self.dfs(A[:i] + A[i+1:], res, path + [A[i]])
