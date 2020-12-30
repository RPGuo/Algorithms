# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        if rows < 1 or cols < 1 or threshold < 0:
            return 0
        flag = [[False for _ in range(cols)] for _ in range(rows)]
        self.sol(0, 0, threshold, flag)
        return sum(map(sum, flag))
    def sol(self, i, j, threshold, flag):
        if i<0 or i>=len(flag) or j<0 or j>=len(flag[0]):
            return
        if flag[i][j] or self.check(i)+self.check(j) > threshold:
            return
        flag[i][j] = True
        self.sol(i-1, j, threshold, flag)
        self.sol(i+1, j, threshold, flag)
        self.sol(i, j-1, threshold, flag)
        self.sol(i, j+1, threshold, flag)
    def check(self, n):
        res = 0
        while n:
            res += n%10
            n = n/10
        return res