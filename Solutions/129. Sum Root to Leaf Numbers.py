# Recursively

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.res = 0
        self.findPath(root, 0)
        return self.res
    
    def findPath(self, node, sum):
        if node:
            sum += node.val
            if not (node.left or node.right):
                self.res += sum
            else:
                self.findPath(node.left, 10 * sum)
                self.findPath(node.right, 10 * sum)

# Bfs + queue

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        q, res = collections.deque([[root, root.val]]), 0
        
        while q:
            node, val = q.popleft()
            if not (node.left or node.right):
                res += val
            if node.left:
                q.append([node.left, val*10 + node.left.val])
            if node.right:
                q.append([node.right, val*10 + node.right.val])
        return res

# Dfs + stack

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        q, res = [[root, root.val]], 0
        
        while q:
            node, val = q.pop()
            if not (node.left or node.right):
                res += val
            if node.right:
                q.append([node.right, val*10 + node.right.val])
            if node.left:
                q.append([node.left, val*10 + node.left.val])
        return res
