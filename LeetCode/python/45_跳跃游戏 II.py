class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        max_position = 0
        end = 0
        for i in range(len(nums) - 1):
            max_position = max(max_position, nums[i] + i)
            if i == end:
                end = max_position
                step += 1
        return step