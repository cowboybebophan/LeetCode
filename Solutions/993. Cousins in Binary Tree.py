Similar to problem 102: https://leetcode.com/problems/binary-tree-level-order-traversal/

Check explanation here: https://leetcode.com/problems/cousins-in-binary-tree/discuss/257862/Python-BFS-%2B-Hash-tm-(993)

# BFS + deque + dic

from collections import deque

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = deque([root])
        
        while queue:
            size = len(queue)
            dic = {}
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    dic[node.left.val] = node.val
                if node.right:
                    queue.append(node.right)
                    dic[node.right.val] = node.val
            if x in dic and y in dic and dic[x] != dic[y]:
                return True
        return False
