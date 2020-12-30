class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s or numRows < 2:
            return s
        res = ['' for _ in range(numRows)]
        i, flag = 0, -1
        for char in s:
            res[i] += char
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag
        return ''.join(res)