# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        if not array:
            return []
        for i in range(len(array)):
            if array[i]&1==0:
                for j in range(i+1,len(array)):
                    if array[j]&1==1:
                        temp = array[j]
                        for k in range(j, i, -1):
                            array[k] = array[k-1]
                        array[i] = temp
                        break
        return array