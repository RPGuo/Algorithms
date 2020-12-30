class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return []
        if not words:
            return []
        self.end_of_word = '#'
        self.res = set()
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node[self.end_of_word] = self.end_of_word

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie:
                    self.dfs(board, i, j, '', trie)
        return self.res

    def dfs(self, board, x, y, cur_word, cur_dict):
        cur_word += board[x][y]
        cur_dict = cur_dict[board[x][y]]
        if self.end_of_word in cur_dict:
            self.res.add(cur_word)
        temp = board[x][y]
        board[x][y] = '#'
        for i in range(4):
            nx, ny = x + self.dx[i], y + self.dy[i]
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] in cur_dict and board[nx][ny] != '#':
                self.dfs(board, nx, ny, cur_word, cur_dict)
        board[x][y] = temp