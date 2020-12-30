class Solution:
    def findDisappearedNumbers(self, nums):
        def swap(nums, index1, index2):
            if index1 == index2:
                return
            nums[index1] = nums[index1] ^ nums[index2]
            nums[index2] = nums[index1] ^ nums[index2]
            nums[index1] = nums[index1] ^ nums[index2]

        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                swap(nums, i, nums[i] - 1)
        return [i + 1 for i, num in enumerate(nums) if num != i + 1]