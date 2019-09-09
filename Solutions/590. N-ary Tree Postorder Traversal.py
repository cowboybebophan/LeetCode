# Solution 1
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
    
# Solution 2
class Solution(object):
    def postorder(self, root):
        stack, res = [root], []
        
        while stack and root:
            n = stack.pop()
            res.insert(0, n.val)
            stack += n.children
        return res
