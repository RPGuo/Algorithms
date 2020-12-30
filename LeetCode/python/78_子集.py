class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)

        def helper(i, path):
            res.append(path)
            for j in range(i, n):
                helper(j + 1, path + [nums[j]])

        helper(0, [])
        return res
### 位运算
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = 1 << len(nums)
        res = []
        for i in range(n):
            temp = []
            for j in range(len(nums)):
                if i>>j&1 == 1:
                    temp.append(nums[j])
            res.append(temp)
        return res