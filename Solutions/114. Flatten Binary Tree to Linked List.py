"""
https://www.youtube.com/watch?v=NHdrzNpt1ZI&list=LLFMFwZhJPiOjNGDHQTAKqwg&index=3&t=0s

这题有点抽象，主要思想是：
先用recursion分别flatten Root的左右子树, 其实这时候我们还不知道函数的具体算法，
但是我们知道我们函数功能是flatten一个二叉树为链表，所以我们姑且认为这时候根的左右子树已经被flatten。
然后我们先用一个tmpNode储存右子树，并把左子树移到右边同时清空根的左子树，然后将保存的右子树链接到之前左子树的最后面，完成转换。

反之亦然：先将右子树移到左子树的末尾，然后一起移动到根的右子树处。

“”“

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        if not root: 
            return None        
        
        self.flatten(root.left)    # 先flatten根的左右子树
        self.flatten(root.right)
        tmpNode = root.right       # 将右子树保存
        root.right = root.left     # 将左子树移到右边
        root.left = None           # 将根的左子树清空
        while root.right:          # 找到原左子树的leaf（最后一个节点）
            root = root.right      
        root.right = tmpNode       # 将保存的右子树嫁接上去
