class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = x ^ y
        count = 0
        while res:
            res = (res-1)&res
            count += 1
        return count