"""
To understand this solution, you just need to ask yourself these question.
Assume the distance from head to the start of the loop is x
the distance from the start of the loop to the point fast and slow meet is y
the distance from the point fast and slow meet to the start of the loop is z
What is the distance fast moved? What is the distance slow moved? And their relationship?

1. x + y + z + y
2. x + y
3. x + y + z + y = 2 (x + y)

Thus x = z

"""
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        while head != slow:
            slow = slow.next
            head = head.next
        return head
