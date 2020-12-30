class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for char in s:
            res = res*26 + ord(char) - 64
        return res