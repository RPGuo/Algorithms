class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        res, n =[], len(nums)
        nums.sort()
        for k in range(n - 2):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            if nums[k] + nums[k+1] + nums[k+2] > 0:
                break
            if nums[k] + nums[n-1] + nums[n-2] < 0:
                continue
            i, j = k+1, n-1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s == 0:
                    res.append([nums[k], nums[i], nums[j]])
                    while i < j and nums[i] == nums[i+1]:
                        i += 1
                    while i < j and nums[j] == nums[j-1]:
                        j -= 1
                    i += 1
                    j -= 1
                elif s > 0:
                    j -= 1
                else:
                    i += 1
        return res