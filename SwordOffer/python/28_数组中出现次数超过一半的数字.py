# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        cur = numbers[0]
        count = 1
        for i in numbers[1:]:
            if count == 0:
                cur = i
                count = 1
            elif cur == i:
                count += 1
            else:
                count -= 1
        count = 0
        for i in numbers:
            if cur == i:
                count += 1
        return cur if 2*count > len(numbers) else 0