class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res, level = [], [root]
        while root and level:
            res.append([node.val for node in level])
            level = [child for node in level for child in node.children if child]
        return res
