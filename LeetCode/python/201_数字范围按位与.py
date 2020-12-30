class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        i = 0
        while n > m:
            n >>= 1
            m >>= 1
            i += 1
        return m << i

## 方法2
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while n > m:
            n = n & (n - 1)
        return n