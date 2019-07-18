# Solution 1
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        value = []
        while head:
            value += [head.val]
            head = head.next
        return value == value[::-1]
             
# Solution 2
""" 
check explanation here: 
https://leetcode.com/problems/palindrome-linked-list/discuss/64500/11-lines-12-with-restore-O(n)-time-O(1)-space
"""

class Solution:
    def isPalindrome(self, head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev
