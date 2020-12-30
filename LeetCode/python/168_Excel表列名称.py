class Solution:
    def convertToTitle(self, n: int) -> str:
        # A = 65
        res = ''
        while n:
            n = n - 1
            n, b = divmod(n, 26)
            res = chr(b+65) + res
        return res