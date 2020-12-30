# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix or not path or len(path) > rows*cols:
            return False
        flag = [[False for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                res = self.is_path(matrix, rows, cols, i, j, flag, path, 0)
                if res:
                    return True
        return False
    def is_path(self, matrix, rows, cols, i, j, flag, path, index):
        if index == len(path):
            return True
        if i<0 or i>=rows or j<0 or j>=cols:
            return False
        if flag[i][j]:
            return False
        if path[index] != matrix[i*cols+j]:
            return False
        flag[i][j] = True
        index += 1
        left = self.is_path(matrix, rows, cols, i, j-1, flag, path, index)
        right = self.is_path(matrix, rows, cols, i, j+1, flag, path, index)
        up = self.is_path(matrix, rows, cols, i-1, j, flag, path, index)
        down = self.is_path(matrix, rows, cols, i+1, j, flag, path, index)
        res = left or right or up or down
        if not res:
            flag[i][j] = False
            index -= 1
        return res