class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        def helper(start, temp):
            res.append(temp)
            if start == n:
                return
            for j in range(start, n):
                if j > start and nums[j] == nums[j-1]:
                    continue
                helper(j+1, temp + [nums[j]])
        helper(0, [])
        return res