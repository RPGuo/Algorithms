class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = 0 ^ n
        for i in range(n):
            res = res ^ i ^ nums[i]
        return res
### 方法二
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = n - 0
        for i in range(n):
            res += i - nums[i]
        return res