class Solution:
    def totalNQueens(self, n: int) -> int:
        if n < 1:
            return []
        self.count = 0
        self._dfs(n, 0, 0, 0, 0)
        return self.count
    def _dfs(self, n, row, cols, pie, na):
        if row >= n:
            self.count += 1
            return
        bits = (~(cols | pie | na))&((1 << n)-1)
        while bits:
            bit = bits&(-bits)
            self._dfs(n, row+1, cols|bit, (pie|bit)<<1, (na|bit)>>1)
            bits = bits&(bits-1)