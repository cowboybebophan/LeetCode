class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.extend(node.children)
        return res[::-1]
