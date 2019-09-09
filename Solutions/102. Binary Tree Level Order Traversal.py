"""
https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/33464/5-6-lines-fast-python-solution-(48-ms)

level is a list of the nodes in the current level. Keep appending a list of the values of these nodes to ans 
and then updating level with all the nodes in the next level (kids) until it reaches an empty level. 

Python's list comprehension makes it easier to deal with many conditions in a concise manner.

"""

# BFS using deque
from collections import deque

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        
        queue, res = deque([root]), []
        while queue:
            level, size = [], len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level.append(node.val)
            res.append(level)
        return res
        
# list comprehension
class Solution:
    def levelOrder(self, root):
        res, level = [], [root]
        while root and level:
            res.append([node.val for node in level])
            level = [child for node in level for child in (node.left, node.right) if child]
        return res
        
# list comprehension
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        ans, level = [], [root]
        while level:
            ans.append([node.val for node in level])
            tmp = []
            for node in level:
                tmp += [node.left, node.right]
            level = [leaf for leaf in tmp if leaf]
        return ans

