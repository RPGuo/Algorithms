class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l, tmp, res = 0, 0, float('inf')
        for r in range(len(nums)):
            tmp += nums[r]
            while tmp >= s:
                res = min(res, r-l+1)
                tmp -= nums[l]
                l += 1
        return res if res != float('inf') else 0