class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        flag = [False for _ in range(len(nums))]
        res, path = [], []
        return self.sol(flag, nums, res, path)
    def sol(self, flag, nums, res, path):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if flag[i]:
                continue
            flag[i] = True
            path.append(nums[i])
            self.sol(flag, nums, res, path)
            flag[i] = False
            path.pop()
        return res