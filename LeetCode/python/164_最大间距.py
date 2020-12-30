class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        max_num = max(nums)
        min_num = min(nums)
        gap = math.ceil((max_num-min_num)/(n-1))
        bucket = [[float('inf'), float('-inf')] for _ in range(n-1)]
        for num in nums:
            if num == max_num or num == min_num:
                continue
            idx = (num-min_num) // gap
            bucket[idx][0] = min(bucket[idx][0], num)
            bucket[idx][1] = max(bucket[idx][1], num)
        pre_min = min_num
        res = float('-inf')
        for x, y in bucket:
            if x == float('inf'):
                continue
            res = max(res, x - pre_min)
            pre_min = y
        res = max(res, max_num - pre_min)
        return res