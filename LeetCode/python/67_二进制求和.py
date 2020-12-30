class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a or not b:
            return 0
        res, temp = '', 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0:
            if i >= 0:
                temp += ord(a[i]) - ord('0')
            if j >= 0:
                temp += ord(b[j]) - ord('0')
            res += str(temp % 2)
            temp = temp // 2
            i -= 1
            j -= 1
        if temp == 1:
            res += '1'
        return res[::-1]