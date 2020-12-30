class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums) < 4:
            return []
        nums.sort()
        res, n = [], len(nums)
        for m in range(n - 3):
            if m > 0 and nums[m] == nums[m-1]:
                continue
            if nums[m] + nums[m+1] + nums[m+2] + nums[m+3] > target:
                break
            if nums[m] + nums[n-1] + nums[n-2] + nums[n-3] < target:
                continue
            for k in range(m+1, n-2):
                if k-m > 1 and nums[k] == nums[k-1]:
                    continue
                if nums[m] + nums[k] + nums[k+1] + nums[k+2] > target:
                    break
                if nums[m] + nums[k] + nums[n-1] + nums[n-2] < target:
                    continue
                i, j = k + 1, n-1
                while i < j:
                    s = nums[m] + nums[k] + nums[i] + nums[j]
                    if s == target:
                        res.append([nums[m], nums[k], nums[i], nums[j]])
                        while i < j and nums[i] == nums[i+1]:
                            i += 1
                        while i < j and nums[j] == nums[j-1]:
                            j -= 1
                        i += 1
                        j -= 1
                    elif s > target:
                        j -= 1
                    else:
                        i += 1
        return res