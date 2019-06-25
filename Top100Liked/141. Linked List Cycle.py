"""
1. Use two pointers, walker and runner.
2. walker moves step by step. runner moves two steps at time.
3. if the Linked List has a cycle walker and runner will meet at some point.

"""

class Solution(object):
    def hasCycle(self, head):
        walker = runner = head
        while runner and runner.next:
            runner = runner.next.next
            walker = walker.next
            if runner == walker:
                return True
        return False
