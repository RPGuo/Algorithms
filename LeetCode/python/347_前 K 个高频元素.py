### 桶排序
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp_dict = {}
        for num in nums:
            temp_dict[num] = temp_dict.get(num, 0) + 1
        temp_list = [[] for _ in range(len(nums)+1)]
        for key, value in temp_dict.items():
            temp_list[value].append(key)
        res = []
        for j in range(len(nums), -1, -1):
            if not temp_list[j]:
                continue
            if k:
                res += temp_list[j]
                k -= len(temp_list[j])
        return res