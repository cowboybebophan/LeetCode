# Recursively

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []
        self.findPath(root, res, str(root.val))
        return res
    
    def findPath(self, node, res, path):
        if not (node.left or node.right):
            res.append(path)
        if node.left:
            self.findPath(node.left, res, path + "->" + str(node.left.val))
        if node.right:
            self.findPath(node.right, res, path + "->" + str(node.right.val))
            
