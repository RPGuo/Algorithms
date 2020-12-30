# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        numbers = list(map(str, numbers))
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                temp0 = int(numbers[i] + numbers[j])
                temp1 = int(numbers[j] + numbers[i])
                if temp1 < temp0:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
        return ''.join(numbers)