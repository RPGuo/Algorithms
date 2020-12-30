class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            if x == 0:
                return -1
            a = -n
        elif n == 0:
            if x == 0:
                return -1
            else:
                return 1
        else:
            a = n
        res = 1
        while a:
            if a&1 == 1:
                res *= x
            x *= x
            a = a >> 1
        return res if n > 0 else 1.0/res