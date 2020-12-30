class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        total, cur, index = 0, 0, 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            cur += gas[i] - cost[i]
            if cur < 0:
                index = i + 1
                cur = 0
        return -1 if total < 0 else index