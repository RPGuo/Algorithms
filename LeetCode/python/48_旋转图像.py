class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        for x in range(row):
            for y in range(x):
                matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]
        for x in range(row):
            for y in range(col//2):
                matrix[x][y], matrix[x][col-1-y] = matrix[x][col-1-y], matrix[x][y]
        return matrix