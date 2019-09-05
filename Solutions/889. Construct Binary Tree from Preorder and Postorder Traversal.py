"""
Check the idea here:
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/139414/Why-there-isn't-a-question-about-construct-Binary-Tree-from-preorder-and-postorder-Traversal

The idea is same as problem 105 and 106, the only difference is that we need to check if len(pre) == 1;
Because we need the value of the second to last number in pre so that we can find its index in post;
If len(pre) == 1, then pre[1] is invalid.

"""

# Recursively
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not (pre and post):
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        i = post.index(pre[1])
        root.left = self.constructFromPrePost(pre[1:i+2], post[:i+1])
        root.right = self.constructFromPrePost(pre[i+2:], post[i+1:-1])
        return root
                
