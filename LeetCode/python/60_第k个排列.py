class Solution:
    def getPermutation(self, n, k):

        def helper(n):
            res = 1
            for i in range(2, n + 1):
                res = res * i
            return res

        res = ""
        nums = [i + 1 for i in range(n)]
        while n:
            jc = helper(n - 1)
            idx = (k - 1) // jc
            res += str(nums.pop(idx))
            n -= 1
            k -= (idx + 1) * jc
        return res