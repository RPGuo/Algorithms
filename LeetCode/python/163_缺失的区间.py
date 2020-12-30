class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        low = lower - 1
        nums.append(upper + 1)
        for num in nums:
            dif = num - low
            if dif == 2:
                res.append(str(low+1))
            if dif > 2:
                res.append(str(low+1) + '->' + str(num-1))
            low = num
        return res