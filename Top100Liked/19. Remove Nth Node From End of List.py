# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        
        return head
        
"""

Note:
这道题让我们移除链表倒数第n个节点，限定n一定是有效的，即n不会大于链表中的元素总数.
还有题目要求我们一次遍历解决问题，那么就得想些比较巧妙的方法了。

我们首先要考虑的是，如何找到倒数第N个节点。由于只允许一次遍历，所以我们不能用一次完整的遍历来统计链表中元素的个数，
而是遍历到对应位置就应该移除了。那么我们需要用两个指针来帮助我们解题，fast和slow指针。

首先fast指针先向前走n步，如果此时fast指向空，说明n为链表的长度，则需要移除的为首元素，那么此时我们返回head->next即可。
如果fast存在，我们再继续往下走，此时slow指针也跟着走，直到fast为最后一个元素时停止，

此时slow指向要移除元素的前一个元素，我们再修改指针跳过需要移除的元素即可。

"""
