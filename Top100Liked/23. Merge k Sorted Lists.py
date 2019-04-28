"""
Problem discription:

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
Example:
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Using sort()
class Solution(object):    
    def mergeKLists(self, lists):
        l = []
        for lst in lists:
            while lst:
                l.append(lst.val)
                lst = lst.next
        l.sort()
        dummy = head = ListNode(None)
        for num in l:
            head.next = ListNode(num)
            head = head.next
        return dummy.next
      
# Using PriorityQueue      
      
