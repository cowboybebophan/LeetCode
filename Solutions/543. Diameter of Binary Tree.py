# Basically, we find the longest path between two nodes while traversing through the tree.

# The depth() function returns the longest path started from a certain node down to a leaf, and the depth of a certain node is 
# defined as 1 + max(depth of node.left, depth of node.right) 

# While we traverse through the tree and record the depth of every node, we update the longest diameter by doing
# self.longest = max(self.longest, L + R)

class Solution:
    def diameterOfBinaryTree(self, root):
        self.longest = 0
        
        def depth(node):
            if not node:
                return 0
            L, R = depth(node.left), depth(node.right)
            self.longest = max(self.longest, L + R)
            return 1 + max(L, R)
        depth(root)
        
        return self.longest
