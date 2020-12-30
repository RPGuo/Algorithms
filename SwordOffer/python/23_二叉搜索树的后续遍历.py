# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        if len(sequence) == 1:
            return True
        head = sequence[-1]
        index = 0
        while sequence[index] < head:
            index += 1
        for i in range(index , len(sequence)-1):
            if sequence[i] < head:
                return False
        l_is = True
        r_is = True
        if sequence[:index]:
            l_is = self.VerifySquenceOfBST(sequence[:index])
        if sequence[index:-1]:
            r_is = self.VerifySquenceOfBST(sequence[index:-1])
        return l_is and r_is