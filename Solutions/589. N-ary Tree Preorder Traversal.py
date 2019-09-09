class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res, stack = [], [root]
        while stack:
            node = stack.pop()    
            res.append(node.val)
            stack.extend(reversed(node.children))
        return res
