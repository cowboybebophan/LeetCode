"""
https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/33464/5-6-lines-fast-python-solution-(48-ms)

level is a list of the nodes in the current level. Keep appending a list of the values of these nodes to ans 
and then updating level with all the nodes in the next level (kids) until it reaches an empty level. 

Python's list comprehension makes it easier to deal with many conditions in a concise manner.

"""

# Solution 1
class Solution:
    def levelOrder(self, root):
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            LRpair = [(node.left, node.right) for node in level]
            level = [leaf for LR in LRpair for leaf in LR if leaf]
        return ans
        
# Solution 2
class Solution:
    def levelOrder(self, root):
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            level = [leaf for node in level for leaf in (node.left, node.right) if leaf]
        return ans
        
# Solution 3
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
    
