class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        h1 = l1 = ListNode(0)
        h2 = l2 = ListNode(0)
        
        while head:
            if head.val < x:
                l1.next = ListNode(head.val)
                l1 = l1.next
            else:
                l2.next = ListNode(head.val)
                l2 = l2.next
            head = head.next
        l1.next = h2.next
        return h1.next
