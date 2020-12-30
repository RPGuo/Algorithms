class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n < 1:
            return []
        self.res = []
        self._dfs(n, [], [], [])
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in res] for res in self.res]

    def _dfs(self, n, path, pie, na):
        row = len(path)
        if row == n:
            self.res.append(path)
        for col in range(n):
            if col not in path and row + col not in pie and row - col not in na:
                self._dfs(n, path + [col], pie + [row + col], na + [row - col])