"""
This link explains all three problems related to constructing binary tree from preorder or inorder or postorder traversal.

https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/139414/Why-there-isn't-a-question-about-construct-Binary-Tree-from-preorder-and-postorder-Traversal

"""
# Recursively
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not (inorder and postorder):
            return None
        root = TreeNode(postorder[-1])
        i = inorder.index(root.val)
        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i+1:], postorder[i:-1])
        return root
        
# Recursively
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not (inorder and postorder):
            return None
        root = TreeNode(postorder.pop())
        i = inorder.index(root.val)
        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i+1:], postorder[i:])
        return root
