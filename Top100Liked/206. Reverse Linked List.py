"""
https://leetcode.com/problems/reverse-linked-list/discuss/140916/Python-Iterative-and-Recursive-(206)

"""

# Iteratively

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        while head:
            cur = head
            head = head.next
            cur.next = pre
            pre = cur
        return pre
        
Or

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        pre, cur = None, head        
        while cur:                  # 不移动head的reference.
            next_copy = cur.next
            cur.next = pre
            pre = cur
            cur = next_copy
        return pre

# Recursively

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverseLink(head)
    
    def reverseLink(self, head, pre = None):
        if not head:
            return pre
        next_copy = head.next
        head.next = pre
        pre = head
        
        return self.reverseLink(next_copy, pre)

