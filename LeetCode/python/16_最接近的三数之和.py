class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) < 3:
            return 0
        nums.sort()
        close_num = nums[0] + nums[1] + nums[2]
        for k in range(len(nums)-2):
            l, r = k+1, len(nums)-1
            while l < r:
                temp = nums[k] + nums[l] + nums[r]
                if abs(temp - target) < abs(close_num - target):
                    close_num = temp
                if temp < target:
                    l += 1
                elif temp > target:
                    r -= 1
                else:
                    return temp
        return close_num