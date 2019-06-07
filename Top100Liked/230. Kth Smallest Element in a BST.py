"""
Do an inorder traversal then return the kth element.

"""
# Going through all nodes

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res, stack = [], []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            else:
                tmpNode = stack.pop()
                res.append(tmpNode.val)
                root = tmpNode.right
        return res[k-1]
        
# Not going through all nodes

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmpNode = stack.pop()
                k -= 1
                if k == 0:
                    return tmpNode.val
                root = tmpNode.right
                
