class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = collections.deque([])
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r in [0, len(board) -1] or c in [0, len(board[0]) - 1]) and board[r][c] == 'O':
                    q.append((r,c))
                    
        while q:
            r, c = q.popleft()
            if  0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == 'O':
                board[r][c] = '#'
                q.extend([ (r - 1, c), (r+1, c), (r, c-1), (r, c+1) ])
            
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == '#':
                    board[r][c] = 'O'
                
