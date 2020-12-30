class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        i = 1
        for j in range(2, n):
            if nums[i - 1] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1