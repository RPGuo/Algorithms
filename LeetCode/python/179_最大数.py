class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        nums = list(map(str, nums))
        for i in range(len(nums) - 1):
            for j in range(1, len(nums)):
                str1 = nums[j - 1] + nums[j]
                str2 = nums[j] + nums[j - 1]
                if str1 < str2:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
        return ''.join(nums).lstrip('0') or '0'