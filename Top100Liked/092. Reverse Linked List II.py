"""
https://leetcode.com/problems/reverse-linked-list-ii/discuss/30672/Python-one-pass-iterative-solution
"""
class Solution(object):
    def reverseBetween(self, head, m, n):
        dummy = ListNode(0)
        dummy.next = head
        
        cur, pre = head, dummy
        for _ in range(m - 1):
            cur = cur.next
            pre = pre.next
        
        for _ in range(n - m):
            temp = cur.next
            cur.next = temp.next
            temp.next = pre.next
            pre.next = temp

        return dummy.next
        
