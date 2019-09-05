"""
https://leetcode.com/problems/word-search/discuss/27660/Python-dfs-solution-with-comments.

"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                if self.dfs(board, word, 0, i, j):
                    return True
        return False
    
    def dfs(self, board, word, pos, i, j):
        if pos == len(word):
            return True
        if not (0<= i < len(board)) or not (0<= j < len(board[0])) or board[i][j] != word[pos]:
            return False
        tmp = board[i][j]
        board[i][j] = '#'
        res = self.dfs(board, word, pos + 1, i + 1, j) or \
              self.dfs(board, word, pos + 1, i - 1, j) or \
              self.dfs(board, word, pos + 1, i, j + 1) or \
              self.dfs(board, word, pos + 1, i, j - 1)
        board[i][j] = tmp
        return res
