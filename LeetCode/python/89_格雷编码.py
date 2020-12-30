class Solution:
    def grayCode(self, n: int) -> List[int]:
        res, head = [0], 1
        for i in range(n):
            length = len(res)
            for j in range(length - 1, -1, -1):
                res.append(head + res[j])
            head <<= 1
        return res