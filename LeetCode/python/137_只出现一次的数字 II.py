class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos, threes = 0, 0, 0
        for n in nums:
            twos = twos | (ones & n)
            ones = ones ^ n
            threes = ones & twos
            ones = ones & (~threes)
            twos = twos & (~threes)
        return ones