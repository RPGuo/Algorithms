# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        if not A:
            return None
        B = [1] + [None] * (len(A)-1)
        for i in range(1, len(A)):
            B[i] = B[i-1] * A[i-1]
        temp = 1
        for i in range(len(A)-2, -1, -1):
            temp = temp * A[i+1]
            B[i] = B[i] * temp
        return B