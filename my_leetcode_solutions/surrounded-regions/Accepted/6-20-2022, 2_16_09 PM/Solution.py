// https://leetcode.com/problems/surrounded-regions

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        q = deque()
        rows, cols = len(board), len(board[0])
        for r in [0, rows - 1]:
            for c in range(cols):
                if board[r][c] == 'O':
                    q.append((r, c))
                    board[r][c] = '.'
        for c in [0, cols - 1]:
            for r in range(rows):
                if board[r][c] == 'O':
                    q.append((r, c))
                    board[r][c] = '.'
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        while q: 
            r, c = q.popleft()
            for direction in directions: 
                dr, dc = direction 
                newr, newc = r + dr, c + dc
                if (rows > newr >=0) and (cols > newc >= 0) and board[newr][newc] == 'O':
                    board[newr][newc] = '.'
                    q.append((newr, newc))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '.':
                    board[r][c] = 'O'
        