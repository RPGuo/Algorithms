class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return None
        return self.solve(board)
    def solve(self, board):
        if not board:
            return None
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for k in range(1, 10):
                        if self.is_valid(board, i, j, str(k)):
                            board[i][j] = str(k)
                            if self.solveSudoku(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True
    def is_valid(self, board, row, col, c):
        for i in range(9):
            if board[row][i] != '.' and board[row][i] == c:
                return False
            if board[i][col] != '.' and board[i][col] == c:
                return False
            if board[3*(row//3) + i//3][3*(col//3) + i%3] != '.' and board[3*(row//3) + i//3][3*(col//3) + i%3] == c:
                return False
        return True