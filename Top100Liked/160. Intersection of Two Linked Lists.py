"""
https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49798/Concise-python-code-with-comments

# the idea is if you switch head, the possible difference between length would be countered. 
# On the second traversal, they either hit or miss. 
# if they meet, pa or pb would be the node we are looking for, 
# if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them is the same.

"""

# Two pointers

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        
        if not headA or not headB:
            return None
        
        pa, pb = headA, headB       # 2 pointers
        
        while pa != pb:
            pa = pa.next if pa else headB      # if either pointer hits the end, switch head and continue the second traversal, 
            pb = pb.next if pb else headA      # if not hit the end, just move on to next
            
        
        return pa     # only 2 ways to get out of the loop, they meet or the both hit the end = None

