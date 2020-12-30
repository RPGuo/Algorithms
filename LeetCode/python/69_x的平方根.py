### 牛顿法
class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        while r * r> x:
            r = (r + x // r) // 2
        return r
### 二分法
class Solution:
    def mySqrt(self, x):
        if x == 1:
            return 1
        conf = 1e-3
        l, r = 0, x
        while r - l > conf:
            mid = (l+r)/2
            if mid > x / mid:
                r = mid
            else:
                l = mid
        return l