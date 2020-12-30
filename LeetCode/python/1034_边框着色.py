class Solution(object):
    def colorBorder(self, grid, r0, c0, color):
        """
        :type grid: List[List[int]]
        :type r0: int
        :type c0: int
        :type color: int
        :rtype: List[List[int]]
        """
        oldcolor = grid[r0][c0]
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        self.fill(grid, r0, c0, visited, oldcolor, color)
        return grid
    def fill(self, grid, x, y, visited, oldcolor, color):
        if x<0 or x>=len(grid) or y<0 or y>=len(grid[0]):
            return 0
        if visited[x][y]:
            return 1
        if grid[x][y] != oldcolor:
            return 0
        visited[x][y] = True
        count = self.fill(grid, x+1, y, visited, oldcolor, color) + self.fill(grid, x-1, y, visited, oldcolor, color) + self.fill(grid, x, y+1, visited, oldcolor, color) + self.fill(grid, x, y-1, visited, oldcolor, color)
        if count < 4:
            grid[x][y] = color
        return 1