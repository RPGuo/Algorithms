class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def helper(nums):
            pre, cur = 0, 0
            for num in nums:
                pre, cur = cur, max(cur, pre + num)
            return cur
        return max(helper(nums[:-1]), helper(nums[1:]))