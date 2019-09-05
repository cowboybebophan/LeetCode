class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left
    
    def next(self) -> int:
        """
        @return the next smallest number
        """
        tmpNode = self.stack.pop()
        x = tmpNode.right
        while x:
            self.stack.append(x)
            x = x.left
        return tmpNode.val
            
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0 
