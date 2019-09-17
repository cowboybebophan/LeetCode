# Solution 1 
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_sum, l2_sum = 0, 0
        while l1:
            l1_sum = l1_sum * 10 + l1.val
            l1 = l1.next
        while l2:
            l2_sum = l2_sum * 10 + l2.val
            l2 = l2.next
        
        l3_sum = l1_sum + l2_sum
        
        dummy = cur = ListNode(None)
        
        for val in str(l3_sum):
            cur.next = ListNode(val)
            cur = cur.next
        return dummy.next
