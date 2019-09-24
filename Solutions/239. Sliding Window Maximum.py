"""
https://leetcode.com/problems/sliding-window-maximum/discuss/111560/Python-O(n)-solution-using-deque-with-comments
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        res = []
        
        for i in range(len(nums)):
            if q and i - q[0] == k: 
                q.popleft()
            
            while q:
                if nums[i] > nums[q[-1]]:
                    q.pop()
                else:
                    break
            
            q.append(i)
            
            if i >= k-1:
                res.append(nums[q[0]])
        return res
