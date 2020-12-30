class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hash_map:
                return [hash_map[another_num], index]
            hash_map[num] = index
        return []