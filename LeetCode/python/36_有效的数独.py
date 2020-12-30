class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board:
            return
        self.row = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        self.col = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        self.box = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    nums = int(board[i][j]) - 1
                    box_index = i // 3 * 3 + j // 3
                    if self.row[i][nums] or self.col[j][nums] or self.box[box_index][nums]:
                        return False
                    else:
                        self.row[i][nums] = True
                        self.col[j][nums] = True
                        self.box[box_index][nums] = True
        return True