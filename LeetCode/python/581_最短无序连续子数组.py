class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        _max = float("-inf")
        _min = float("inf")
        left, right = 0, 0
        for i in range(len(nums)):
            if nums[i] >= _max:
                _max = nums[i]
            else:
                right = i
        for i in range(len(nums)-1, -1, -1):
            if nums[i] <= _min:
                _min = nums[i]
            else:
                left = i
        return right - left + 1 if left < right else 0