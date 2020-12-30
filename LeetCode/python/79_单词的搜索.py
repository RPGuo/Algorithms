class Solution:
    def exist(self, board: List[List[str]], words: str) -> bool:
        if not board or not board[0]:
            return []
        if not words:
            return []
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == words[0] and self.dfs(board, i, j, words[1:]):
                    return True
        return False

    def dfs(self, board, x, y, cur_word):
        if not cur_word:
            return True
        c = board[x][y]
        board[x][y] = '#'
        for i in range(4):
            nx, ny = x + self.dx[i], y + self.dy[i]
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == cur_word[0] and \
                    self.dfs(board, nx, ny, cur_word[1:]):
                return True
        board[x][y] = c
        return False