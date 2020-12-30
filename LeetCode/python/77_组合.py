class Solution:
    def combine(self, n: int, k: int):
        if n < k or n < 0 or k < 0:
            return []
        res = []
        def helper(start, temp):
            if len(temp) == k:
                res.append(temp[:])
                return
            for i in range(start, n+1):
                temp.append(i)
                helper(i+1, temp)
                temp.pop()
        helper(1, [])
        return res