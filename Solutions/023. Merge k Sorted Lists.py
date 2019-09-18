# Using sort()

# Time complexity : O(N\log N)O(NlogN) where NN is the total number of nodes.
# 1. Collecting all the values costs O(N)O(N) time.
# 2. A stable sorting algorithm costs O(N\log N)O(NlogN) time.
# 3. Iterating for creating the linked list costs O(N)O(N) time.

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

# Time complexity : O(N\log k)O(Nlogk) where \text{k}k is the number of linked lists.
# 1. The comparison cost will be reduced to O(\log k)O(logk) for every pop and insertion to priority queue. 
#    But finding the node with the smallest value just costs O(1)O(1) time.
# 2. There are NN nodes in the final linked list.

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
