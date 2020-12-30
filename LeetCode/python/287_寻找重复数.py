### 二分法
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l, r = 1, len(nums) - 1
        while l < r:
            mid = l + r >> 1
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                r = mid
            else:
                l = mid + 1
        return l

### 快慢指针
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0, 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        temp = 0
        while True:
            slow = nums[slow]
            temp = nums[temp]
            if slow == temp:
                break
        return slow