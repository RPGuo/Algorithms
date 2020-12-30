class Solution:
    def __init__(self):
        self.dirt = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                isEdge = (i == 0 or i == m - 1 or j == 0 or j == n - 1)
                if (isEdge and board[i][j] == 'O'):
                    self.dfs(board, i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'

    def dfs(self, board, x, y):
        board[x][y] = '#'
        for i in range(4):
            nextx, nexty = x + self.dirt[i][0], y + self.dirt[i][1]
            if 0 <= nextx < len(board) and 0 <= nexty < len(board[0]) and board[nextx][nexty] == 'O':
                self.dfs(board, nextx, nexty)