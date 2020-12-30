class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        return self.lis([i[1] for i in envelopes])

    def lis(self, nums):
        dp, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                mid = (i + j) // 2
                if dp[mid] < num:
                    i = mid + 1
                else:
                    j = mid
            dp[i] = num
            if j == res:
                res += 1
        return res