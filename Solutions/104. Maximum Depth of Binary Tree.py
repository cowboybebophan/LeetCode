"""
Solution 1:
Idea here is pretty much the same as problem 102: Binary tree level order traversal.

We create a list called level to store the nodes of different levels untill the list becomes empty.
It means that we have reached the farthest level/node.

Solution 2:
Recursion

"""

# Solution 1
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth, level = 0, [root]
        while root and level:
            depth += 1
            level = [leaf for node in level for leaf in (node.left, node.right) if leaf]
        return depth

# Solution 2
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0
