class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.infect(grid, i, j)
                    res += 1
        return res
    def infect(self, grid, i, j):
        if 0<= i <=len(grid)-1 and 0<= j <=len(grid[0])-1 and grid[i][j] == '1':
            grid[i][j] = '0'
            self.infect(grid, i+1, j)
            self.infect(grid, i-1, j)
            self.infect(grid, i, j+1)
            self.infect(grid, i, j-1)