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
from heapq import heappush, heappop, heapreplace, heapify

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        h = [(node.val, index ,node) for (index, node) in enumerate(lists) if node] 
        heapify(h)  # 加入index是因为如果两个node.val相同，那么没法通过之后的node类型来排序，所以加入index方便对具有相同值的node进行排序                                    
        head = cur = ListNode(0)
        
        while h:
            val, index, node = h[0]
            cur.next = ListNode(val)
            cur = cur.next
            node = node.next
            if node:
                heapreplace(h, (node.val, index, node))
            else:
                heappop(h)
        return head.next      
